# TodoManager

A clean, fast, and intuitive task management app built with Django and PostgreSQL.

![TodoManager Dashboard](todo_manager/static/image/homepage.jpg)

## Features

- **Task CRUD** — Create, read, update, and delete tasks
- **Status tracking** — Mark tasks as completed or pending
- **Filtering** — View all, completed, or pending tasks
- **Pagination** — 5 tasks per page for a clean experience
- **User authentication** — Register, login, and logout
- **Dark / light theme** — Toggle with persistent preference
- **Responsive design** — Works on desktop and mobile
- **Toast notifications** — Instant feedback on actions

## Tech Stack

- **Python** 3.14
- **Django** 6.0.4
- **PostgreSQL** (psycopg2-binary)
- **Tabler Icons** — UI icons
- **CSS custom properties** — Theming

## Prerequisites

- Python 3.12+
- PostgreSQL running on `localhost:5432`

## Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/Todo_Manager_Django.git
cd Todo_Manager_Django

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install django psycopg2-binary

# Create the database
psql -U postgres -c "CREATE DATABASE django_todo;"

# Update database password in todo_manager/todo_manager/settings.py
#   PASSWORD: 'your_postgres_password'

# Run migrations
python todo_manager/manage.py migrate

# Create a superuser (optional, for admin)
python todo_manager/manage.py createsuperuser

# Run the development server
python todo_manager/manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

## Routes

| Route | Page |
|---|---|
| `/` | Home / landing page |
| `/todolist/` | Task board (requires login) |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/users/register/` | Register |
| `/users/login/` | Login |
| `/users/logout/` | Logout |
| `/admin/` | Django admin |

## Project Structure

```
Todo_Manager_Django/
├── todo_manager/
│   ├── manage.py
│   ├── static/                     # Static assets (images, icons)
│   ├── todo_manager/               # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── templates/base.html     # Base layout + theme toggle
│   ├── todolist/                   # Main todo app
│   │   ├── models.py               # Task model
│   │   ├── views.py                # Task CRUD views
│   │   ├── forms.py                # TaskForm
│   │   ├── urls.py
│   │   └── templates/
│   └── users/                      # Auth app
│       ├── views.py                # Register, login, logout
│       ├── forms.py                # RegisterForm
│       └── templates/
└── README.md
```

## License

MIT
