# 👗 Fashion Recommendation System Using Social Media Website

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange.svg)
![Keras](https://img.shields.io/badge/Keras-NeuralNetwork-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🧠 Overview
The **Fashion Recommendation System** leverages **AI and Deep Learning** to analyze user images from **social media platforms** (like Instagram) and recommend matching fashion styles.  
It uses **CNN** and **DenseNet121** models to identify fashion attributes such as **color, pattern, and clothing category**, achieving **99.2% accuracy** in experiments.

---

## 🚀 Features
- 👕 Image-based fashion recommendation  
- 📸 Integration with Instagram profile pictures  
- 🧠 CNN & DenseNet121 for feature extraction and classification  
- 📊 Graphical visualization of accuracy and loss  
- 🔐 User authentication (Register/Login)  
- 💾 Model saving for production (`.h5` / `.pkl`)  

---

## 🧩 System Architecture
The system combines the **DenseNet121** and **CNN** architectures to improve image recognition and classification efficiency.

- **DenseNet121**: Ensures maximum feature reuse and reduces vanishing gradients  
- **CNN**: Learns hierarchical patterns for fashion recognition  
- **Outcome**: More accurate and faster recommendations  

---

## ⚙️ Methodology

### 🔹 Steps Involved
1. **Dataset Preparation**
   - Collected fashion classification & product recommendation datasets  
   - Resized all images to 200×200 pixels  

2. **Data Preprocessing**
   - Converted images to NumPy arrays  
   - Split data: 80% training, 20% testing  

3. **Model Building**
   - Built CNN using Keras Sequential API  
   - Used **DenseNet121** for recommendation tasks  
   - Libraries: `TensorFlow`, `Keras`, `NumPy`, `Scikit-learn`, `PIL`

4. **Training & Evaluation**
   - Compiled and trained using `fit()`  
   - Visualized **accuracy** and **loss** curves  
   - Achieved **99.2% training accuracy**

5. **Deployment**
   - Model saved as `.h5` / `.pkl`  
   - Integrated with a web app (Socket Server + HTML/CSS frontend)

---

## 🧠 Algorithms Used

| Algorithm | Purpose |
|------------|----------|
| **CNN** | For fashion classification and image feature extraction |
| **DenseNet121** | Enhances accuracy through dense connections and feature reuse |

---

## 💻 Tech Stack
**Languages:** Python, HTML, CSS  
**Libraries:** TensorFlow, Keras, NumPy, Pandas, Matplotlib, Scikit-learn, PIL  
**Tools:** Jupyter Notebook, PyCharm  
**Server:** Python Socket Programming  
**Dataset:** Fashion & product image datasets  

---

## 🌐 Application Screens
- 🏠 **Home Page:** Entry point for users  
- 🧾 **Registration Page:** Create new accounts  
- 🔑 **Login Page:** Secure authentication  
- 📸 **Instagram Page:** Profile picture downloader  
- 🖼️ **Input Page:** Upload photo for recommendations  
- 📊 **Result Page:** Display similar fashion items  

---

## 📈 Results
- ✅ **99.2% training accuracy** achieved  
- 🔍 Improved image recognition and recommendation performance  
- 👗 Delivers visually accurate fashion suggestions  

---

## 🔮 Future Enhancements
- 📈 Add real-time fashion data  
- 🧵 Integrate additional visual/textual features  
- 📱 Develop a mobile-friendly UI  
- 🛍️ Connect with e-commerce APIs for outfit purchasing  

---

## 👨‍💻 Authors
- **P. Anusha** – Assistant Professor, Dept. of CSE  
- **Kandula Nikhil Saradhi** – Student, Dept. of CSE  
- **Kokkirala Sravan Kumar** – Student, Dept. of CSE  
- **Marisetty Tejesh** – Student, Dept. of CSE  
- 🏫 *Guru Nanak Institute of Technology, Hyderabad, Telangana, India*

---

## 🏁 Citation
📘 Published in **International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)**  
📅 Volume 4, Issue 1, November 2024  
🔗 DOI: [10.48175/IJARSCT-22093](https://doi.org/10.48175/IJARSCT-22093)

---

## 🪄 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/Fashion-Recommendation-System.git

# Navigate to the folder
cd Fashion-Recommendation-System

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py

