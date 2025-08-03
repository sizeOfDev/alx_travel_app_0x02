# ALX Travel App

**ALX Travel App** is a Django-based backend project for a travel listings platform. It follows industry-standard practices with environment-based configuration, MySQL database integration, and automated API documentation via Swagger.

---

## 🚀 Project Features

- RESTful API built with Django REST Framework
- Swagger UI for live API documentation (`/swagger/`)
- CORS headers configured for frontend integration
- MySQL as the primary relational database
- Modular app structure with `listings` app
- Environment variable management using `django-environ`
- Git version control for collaborative development

---

## 🛠️ Tech Stack

- Python 3.10+
- Django
- Django REST Framework
- MySQL
- Swagger (drf-yasg)
- Celery (future use)
- RabbitMQ (future use)
- django-environ

---

## 📁 Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Django project settings
│   └── settings.py
├── listings/                # Core application for travel listings
│   └── models.py, views.py, urls.py
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not committed)
├── manage.py                # Django management script
├── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:your-username/alx_travel_app.git
cd alx_travel_app
```

### 2. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=your_db
DATABASE_USER=root
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access Swagger API docs

Visit: `http://localhost:8000/swagger/`

---

## 📦 Future Improvements

- Implement user authentication (JWT)
- Add Celery for background tasks (e.g., booking confirmation emails)
- Dockerize the project
- Add unit and integration tests

---

## 🧑‍💻 Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin new-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
