# **Encryption and Decryption App with QR Code Generation**  

This project is a **Flask-based web application** that provides **encryption and decryption functionality** for multiple file types. It also includes a **QR code generator** for quick access to the app.  

---

## **Features:**  
✅ **Encrypt & Decrypt Files** – Uses **Fernet encryption** from the `cryptography` module to secure various file formats.  
✅ **Automatic Key Management** – Generates a unique encryption key and stores it securely.  
✅ **File Selection & Processing** – Scans the system for common file types, excluding critical files.  
✅ **Web-Based Interface** – A simple **HTML front-end** allows users to start encryption or decryption.  
✅ **QR Code Generation** – Generates a QR code linking to the app's web interface.  

---

## **Supported File Types:**  
- **Documents:** `.txt`, `.docx`, `.pptx`, `.pdf`, `.xls`, `.xlsx`  
- **Images & Media:** `.jpg`, `.jpeg`, `.png`, `.mp3`, `.mp4`, `.avi`, `.mov`, `.mkv`  
- **Code & Web Files:** `.cpp`, `.html`, `.xml`  
- **Compressed & Others:** `.zip`, `.flv`, `.webm`, `.mpeg`, `.3gp`  

---

## **How It Works:**  
1. **User visits the web interface** (`index.html`).  
2. **Selects "Encrypt Files" or "Decrypt Files"** – Triggers file processing.  
3. **Files are scanned, encrypted, or decrypted** using a secure key.  
4. **QR Code Generator** allows easy access to the web app.  

---

## **Technology Stack:**  
- **Backend:** Flask (Python)  
- **Encryption:** Cryptography (Fernet)  
- **Frontend:** HTML & Flask Templates  
- **QR Code:** `qrcode` Python module  

---

## **How to Run the Project:**  
1. **Install dependencies:**  
   ```bash
   
   pip install flask cryptography qrcode
   ```  
2. **Run the Flask app:**  
   ```bash
   
   python app.py
   ```  
3. **Open in browser:**

   ```
   http://localhost:5000/
   ```  

---

## **Contact for Freelance Work**  
📩 **Email:** abh200529@gmail.com  

ONLY FOR LEARNING , HOW THINGS ARE WORKING.
