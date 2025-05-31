# 🛍️ BuyBuddy – Price Comparison Web App

**BuyBuddy** is a Django-based web application that enables users to compare product prices across **Amazon**, **Flipkart**, and **Myntra**. It features category-wise product listings, thumbnail previews, and direct purchase links.

---

## 🧰 Tech Stack

- **Backend**: Django 2.2.6  
- **Frontend**: HTML, CSS  
- **Database**: SQLite3  
- **Language**: Python 3.x  
- **Admin Panel**: Django Admin  
- **Virtual Environment**: `venv` (recommended)

---

## 🚀 Features

- 🗂️ View products by category  
- 💰 Compare prices from Amazon, Flipkart, and Myntra  
- 🔗 Clickable links to buy from each store  
- 🔧 Admin panel to manage products, users, and prices  

---

## ⚙️ Project Setup Instructions

### 🔐 Admin Credentials

- **Username**: `ramon`  
- **Password**: `create123`  
- Admin Login: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/your-username/price-comparison-project.git
cd price-comparison-project/SuperMarkIt
```

---

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# source venv/bin/activate # For Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django==2.2.6
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Collect Static Files

```bash
python manage.py collectstatic
# Type 'yes' when prompted
```

---

### 6️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000/admin)[for admin access]

---

## 📁 Project Structure

```
SuperMarkIt/
├── accounts/          # User authentication
├── basket/            # Shopping cart logic
├── products/          # Product data & scraping results
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── media/             # Uploaded thumbnails
├── db.sqlite3         # SQLite database
├── manage.py          # Django command-line utility
├── requirements.txt   # Python packages
└── README.md          # Project documentation
```

---

## 📝 Notes

- If CSS doesn’t load:
  - Ensure `STATICFILES_DIRS` is set in `settings.py`
  - Run `collectstatic` after changes
  - Verify file paths in your HTML templates

- All thumbnails must be either uploaded via the Django admin or stored in the `media/` directory.

---

## 👨‍💻 Author

Made with ❤️ by the **BuyBuddy Team**
