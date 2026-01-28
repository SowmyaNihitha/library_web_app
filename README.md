# 📚 Library Management Web Application

## 🔍 Overview

This is a **server-rendered Library Management System** built using **Flask**, **JWT-based authentication**, and **SQLite3**. The application supports **role-based access control** with two roles:

* **Admin** – manages books and views library data
* **Member** – views available books and borrows/returns them



---

## 🛠 Technology Stack

* Python 
* Flask
* Flask-JWT-Extended (JWT stored in HTTP-only cookies)
* SQLite3 (raw SQL, no ORM)
* Jinja2 Templates
* HTML + CSS

---

## 👥 User Roles & Permissions

### 🔑 Admin

* Login to admin dashboard
* Add new books
* View all books (available & issued)
* View borrowed history

### 👤 Member

* Login to member dashboard
* View available books
* Borrow books
* Return books

> Role-based authorization is enforced at the **route level**, not just UI.

---

## 🔐 Authentication & Authorization

* Users login using **username & password**
* Passwords are **hashed using Werkzeug security**
* On successful login:

  * A **JWT token** is issued
  * Stored securely in **HTTP-only cookies**
* All routes except `/login` and `/register` require authentication
* Unauthorized access:

  * Redirects to login page OR
  * Shows 403 error

---

## 🗄 Database Schema

### users

| Column   | Type    | Description    |
| -------- | ------- | -------------- |
| id       | INTEGER | Primary Key    |
| username | TEXT    | Unique         |
| password | TEXT    | Hashed         |
| role     | TEXT    | admin / member |

### books

| Column    | Type    | Description               |
| --------- | ------- | ------------------------- |
| id        | INTEGER | Primary Key               |
| title     | TEXT    | Book title                |
| author    | TEXT    | Author name               |
| available | INTEGER | 1 = available, 0 = issued |

### borrowed_books

| Column      | Type      | Description   |
| ----------- | --------- | ------------- |
| id          | INTEGER   | Primary Key   |
| user_id     | INTEGER   | Borrower      |
| book_id     | INTEGER   | Borrowed book |
| borrowed_at | TIMESTAMP | Borrow date   |

---

## 📄 Application Pages

### Public Pages

* `/login` – Login page
* `/register` – User registration
* `/logout` – Logout

### Admin Pages

* `/admin/dashboard` – Admin dashboard
* `/admin/books` – Add & view books (single page)

### Member Pages

* `/member/dashboard` – Member dashboard
* `/member/books` – View available books
* `/member/borrow/<book_id>` – Borrow book
* `/member/return/<book_id>` – Return book

---

## 📁 Project Structure

```
library-web-app/
├── app.py
├── auth.py
├── admin.py
├── member.py
├── database.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── admin/
│   │   ├── dashboard.html
│   │   └── books.html
│   └── member/
│       ├── dashboard.html
│       └── books.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

Open browser and visit:

```
http://127.0.0.1:5000/login
```

---

## 🧪 Default Admin Credentials

You can create an admin user manually from the database or modify the registration logic.

Example:

* Username: `admin`
* Password: `admin123`
* Role: `admin`