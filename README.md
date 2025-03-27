# Chatbot Project with Google Gemini AI

This project is a chatbot application that utilizes the **Google Gemini AI** API to generate responses based on user input. The chatbot can be used for various purposes, such as customer support, FAQs, or any other conversational use case.

---

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

---

## **Prerequisites**

Before setting up the project, make sure you have the following installed on your machine:

- **Python 3.12** or higher
- **Django** 5.1 or higher
- **Google Gemini API** credentials (API Key)

---

## **Setup Instructions**

### 1. **Clone the Repository**
Clone the project repository to your local machine.

```bash
git clone https://github.com/your-username/Chatbot_LLM.git

```
### 2. **Set Up the Virtual Environment**
Navigate to the project directory and install the required dependencies.



``` python -m venv env
    source env/bin/activate  # for MacOS/Linux
    env\Scripts\activate  # for Windows
```    

---
### Running the Application

To start the development server, use the following command:

 ```bash

python manage.py runserver

```



📌 Visit the following URLs:
http://127.0.0.1:8000/ai/chat/ → Chatbot

http://127.0.0.1:8000/ai/book_appointment/ → Book Appointment

http://127.0.0.1:8000/ai/user_details/ → Submit Contact Details

```
Below are some screenshots of the chatbot in action:
### **Chatbot Output 1**

![alt text](image.png)

### **Book_Appointment 2**

![alt text](image-1.png)

### **User Details 3**

![alt text](image-2.png)