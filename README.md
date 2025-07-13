# 🚀 Sarva Suvidhan Backend Assignment

This project contains the implementation of two RESTful APIs (`/api/login/` and `/api/uploadKycForm/`) using **Django REST Framework** and **MySQL**. It demonstrates user authentication and KYC form submission with file upload functionality.

---

## 🛠 Tech Stack

- **Backend**: Django 5.2, Django REST Framework
- **Database**: MySQL
- **Language**: Python 3.10+

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mohamed-Afzal-Nandolia/Sarva-Suvidhan-Assignment.git
cd Sarva-Suvidhan-Assignment
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Databse Configuration

-> '**.eve**' **file**:

```bash
DB_NAME=sarva_suvidhan
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=3306
```

### 5. Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

<br>

# Key Features Implemented

- User login with phone and password validation.

- Upload KYC form with documents and save to media directory.

- API routing via Django REST Framework.

- MySQL integration with environment variables for secure credentials.

- Postman tested APIs for correct response format.<br><br>

# Limitations / Assumptions

- Passwords are compared in plain text without hashing/encryption.

- No token/session authentication is implemented.

- Minimal custom validation beyond serializer-level checks.
