from flask import Flask, render_template,request,redirect,url_for
import os
from werkzeug.utils import secure_filename
import pickle
import numpy as np
import tensorflow as tf
from numpy.linalg import norm
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
import cv2
import instaloader

import mysql
import mysql.connector

app = Flask(__name__)


# Create an instance of the Instaloader class
loader = instaloader.Instaloader(dirname_pattern='downloads/{target}/{profile}')

#mysql connection
sql=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="instadata"
    )
cur = sql.cursor()

#cur.execute("CREATE TABLE register (Username varchar(30), phone bigint, email varchar(30), password varchar(20))")
#cur.close()

############### main page ###################################

@app.route('/')
def home():
    return render_template('index.html')            


################# User Register ##############################

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["text"]
        useremail = request.form["email"]
        password = request.form["password"]
        phn = request.form["number"]
        cur.execute("INSERT INTO register VALUES (%s, %s, %s, %s)",(username, phn, useremail, password))
        sql.commit()
        return render_template('contact.html')
    return render_template('contact.html')

################ User Login #################################
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        useremail = request.form["email"]
        userpass = request.form["password"]
        #cur = sql.cursor()
        cur.execute('SELECT * FROM register WHERE email = %s AND password = %s', (useremail, userpass))
        user = cur.fetchone()

        if user:
            return render_template("blog.html")
        else:
            return "Invalid credentials or user not found"

    return render_template('login.html')


############# About Page ####################################

@app.route('/about')
def about():
    return render_template('about.html')

############# serch Page ####################################

@app.route('/search')
def search():
    return render_template('blog.html',similar_images=None)

#----------------------------------------------------------------------------#
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
STATIC_FOLDER = 'static'
app.config['STATIC_FOLDER'] = STATIC_FOLDER

@app.route('/search', methods=["GET", "POST"])
def search_user():
    similar_image_filenames = None
    if request.method == "POST":
        # Check if the POST request has the file part
        if 'image' not in request.files:
            return "No file part"

        file = request.files['image']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return "No selected file"

        if file:
            # Save the uploaded file to the UPLOAD_FOLDER
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the uploaded image
            similar_image_filenames = process_uploaded_image(file_path)

    # Render the blog.html template with or without similar images
    return render_template('blog.html', similar_images=similar_image_filenames)

def process_uploaded_image(file_path):
    # Load precomputed features and filenames
    feature_list = np.array(pickle.load(open('savemodels.pkl','rb')))
    filenames = pickle.load(open('filenames.pkl','rb'))

    model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
    model.trainable = False

    model = tf.keras.Sequential([
        model,
        GlobalMaxPooling2D()
    ])

    img = image.load_img(file_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / np.linalg.norm(result)

    neighbors = NearestNeighbors(n_neighbors=7, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)

    distances, indices = neighbors.kneighbors([normalized_result])

    similar_image_filenames = []
    for file_idx in indices[0][1:7]:
        # Get the filename relative to the static directory
        filename = os.path.relpath(filenames[file_idx], 'static')
        similar_image_filenames.append(filename)

    return similar_image_filenames

#-------------------------------------------------------------------------#
###############service page #################################

@app.route('/service')
def service():
    return render_template('service.html')


###################INSTA PAGE #####################################
@app.route('/instaprofile', methods=['GET', 'POST'])
def instaprofile():
    if request.method == 'POST':
        username = request.form['username']
        try:
            # Download the profile picture of the user
            loader.download_profile(username, profile_pic_only=True)
            return f"Profile picture for {username} downloaded successfully!"
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('instaprofile.html') 



if __name__ == '__main__':
    app.run()