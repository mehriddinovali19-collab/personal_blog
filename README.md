# Django Personal Blog

## Django + PostgreSQL + uv

Bu loyiha orqali Django'ni **0 dan boshlab real project qurish orqali** o‘rganamiz.

Loyihaning oxirida quyidagilar ishlaydi:

* Home page
* Blog
* Post detail
* Category
* Search
* Pagination
* Post CRUD
* Image upload
* Admin panel
* Register
* Login
* Logout
* Profile
* Comments
* PostgreSQL
* Static files
* Media files
* Testing
* Git/GitHub
* AWS deployment
* Nginx
* Gunicorn
* systemd
* HTTPS
* Domain

---

# 1. Loyiha qanday bo‘ladi?

Biz quyidagi **Personal Blog** yaratamiz:

```text
Personal Blog

├── Home
│   ├── Latest Posts
│   ├── Featured Posts
│   └── About me
│
├── Blog
│   ├── All Posts
│   ├── Categories
│   └── Search
│
├── Post
│   ├── Title
│   ├── Image
│   ├── Content
│   ├── Author
│   ├── Category
│   ├── Published date
│   └── Comments
│
├── About
│   ├── My information
│   ├── Skills
│   └── Experience
│
├── Contact
│   └── Contact form
│
└── Admin
    ├── Create post
    ├── Edit post
    ├── Delete post
    ├── Manage categories
    └── Manage comments
```

Keyinchalik:

```text
User
├── Register
├── Login
├── Logout
└── Profile
```

ham qo‘shamiz.

---

# 2. Final project architecture

Oxirida project taxminan shunday ko‘rinishda bo‘ladi:

```text
personal-blog/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   │
│   ├── static/
│   │   └── blog/
│   │       ├── css/
│   │       ├── js/
│   │       └── images/
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   │
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── static/
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

---

# 3. Django'dagi eng muhim flow

Django'da mana shu flow'ni yaxshi tushunib ol:

```text
Browser
   ↓
URL
   ↓
urls.py
   ↓
views.py
   ↓
models.py
   ↓
PostgreSQL
   ↓
Template
   ↓
HTML
   ↓
Browser
```

Masalan:

```text
http://127.0.0.1:8000/posts/django-tutorial/
```

kelganda:

```text
URL
 ↓
urls.py
 ↓
post_detail()
 ↓
Post.objects.get(...)
 ↓
PostgreSQL
 ↓
post_detail.html
 ↓
Browser
```

---

# 4. Project yaratish

Sen `uv` ishlatayotganing uchun hamma commandlar `uv` bilan bo‘ladi.

Terminal:

```bash
mkdir personal-blog
cd personal-blog
```

Virtual environment:

```bash
uv venv
```

Git Bash'da:

```bash
source .venv/Scripts/activate
```

Windows CMD'da:

```bash
.venv\Scripts\activate
```

---

# 5. Django o‘rnatish

Django va PostgreSQL uchun kerakli package'larni boshidanoq o‘rnatamiz:

```bash
uv add django psycopg python-dotenv pillow
```

Bu yerda:

```text
django
```

→ Django framework

```text
psycopg
```

→ Django ↔ PostgreSQL connection

```text
python-dotenv
```

→ `.env` fayldagi environment variable'larni o‘qish

```text
pillow
```

→ ImageField bilan image ishlatish

Tekshirish:

```bash
uv run django-admin --version
```

---

# 6. Django project yaratish

```bash
uv run django-admin startproject config .
```

Natija:

```text
personal-blog/
│
├── manage.py
│
└── config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# 7. Blog app yaratish

Project va app bir xil narsa emas.

### Project

Butun website.

```text
config
```

### App

Website ichidagi alohida functionality.

```text
blog
users
```

Blog app:

```bash
uv run manage.py startapp blog
```

Keyin:

```text
personal-blog/
├── config/
├── blog/
└── manage.py
```

---

# 8. users app yaratish

Keyin authentication uchun:

```bash
uv run manage.py startapp users
```

Project:

```text
personal-blog/
├── config/
├── blog/
├── users/
└── manage.py
```

---

# 9. INSTALLED_APPS

`config/settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "blog",
    "users",
]
```

Bu Django'ga:

```text
blog
users
```

bizning projectdagi app'lar ekanligini bildiradi.

---

# 10. PostgreSQL — boshidanoq

MUHIM:

Bu projectda **SQLite ishlatmaymiz**.

Boshidanoq:

```text
Django
   ↓
PostgreSQL
```

bo‘ladi.
---

# 11. PostgreSQL database yaratish

PostgreSQL o‘rnatilgan bo‘lishi kerak.

PostgreSQL ichida database yaratamiz:

```text
personal_blog
```

Database:

```text
personal_blog
```

User:

```text
postgres
```

Port:

```text
5432
```

Masalan:

```text
Database name: personal_blog
Username: postgres
Password: YOUR_PASSWORD
Host: localhost
Port: 5432
```

---

# 12. .env yaratish

Project root'da:

```text
personal-blog/
├── .env
├── manage.py
├── config/
├── blog/
└── users/
```

`.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=personal_blog
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Passwordni real password bilan almashtirasan.

---

# 13. .env ni settings.py'da o‘qish

`config/settings.py`

tepada:

```python
from pathlib import Path
from dotenv import load_dotenv
import os
```

Keyin:

```python
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
```

SECRET_KEY:

```python
SECRET_KEY = os.getenv("SECRET_KEY")
```

DEBUG:

```python
DEBUG = os.getenv("DEBUG") == "True"
```

---

# 14. PostgreSQL DATABASES

`config/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
```

Endi Django:

```text
Django
   ↓
psycopg
   ↓
PostgreSQL
```

orqali ishlaydi.

---

# 15. Birinchi migration

Django'ning default migrationlarini database'ga qo‘llaymiz:

```bash
uv run manage.py migrate
```

Agar hammasi to‘g‘ri bo‘lsa, PostgreSQL ichida Django jadvallari paydo bo‘ladi.

---

# 16. Serverni ishga tushirish

```bash
uv run manage.py runserver
```

Browser:

```text
http://127.0.0.1:8000/
```

---

# 17. Model yaratish

Blogning asosiy qismi — `models.py`.

`blog/models.py`:

```python
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

# 18. Model fieldlarini tushunish

### CharField

Qisqa text:

```python
title = models.CharField(max_length=200)
```

Masalan:

```text
Django Beginner Guide
```

---

### TextField

Uzun text:

```python
content = models.TextField()
```

---

### SlugField

URL uchun ishlatiladi:

```python
slug = models.SlugField(unique=True)
```

Masalan:

```text
Django Beginner Guide
```

→

```text
django-beginner-guide
```

URL:

```text
/posts/django-beginner-guide/
```

---

### BooleanField

True / False:

```python
published = models.BooleanField(default=False)
```

---

### DateTimeField

Sana va vaqt:

```python
created_at = models.DateTimeField(auto_now_add=True)
```

---

# 19. Model → PostgreSQL

Har safar `models.py` o‘zgarganda:

```bash
uv run manage.py makemigrations
```

keyin:

```bash
uv run manage.py migrate
```

Yodlab ol:

```text
models.py
   ↓
makemigrations
   ↓
migration file
   ↓
migrate
   ↓
PostgreSQL
```

### Juda muhim

Faqat:

```bash
makemigrations
```

yetarli emas.

Database'ga qo‘llash uchun:

```bash
migrate
```

ham kerak.

---

# 20. Admin panel

`blog/admin.py`:

```python
from django.contrib import admin
from .models import Post, Category


admin.site.register(Post)
admin.site.register(Category)
```

Superuser:

```bash
uv run manage.py createsuperuser
```

Keyin:

```bash
uv run manage.py runserver
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

Bu orqali:

```text
Category yaratish
Post yaratish
Post edit
Post delete
```

qilish mumkin.

---

# 21. URL system

`blog/urls.py`:

```python
from django.urls import path

from .views import (
    home,
    post_list,
    post_detail,
)


urlpatterns = [
    path("", home, name="home"),
    path("posts/", post_list, name="post-list"),
    path(
        "posts/<slug:slug>/",
        post_detail,
        name="post-detail",
    ),
]
```

---

# 22. Dynamic URL — juda muhim

Mana buni yaxshi tushun:

```python
path(
    "posts/<slug:slug>/",
    post_detail,
)
```

Bu bitta URL emas.

U:

```text
/posts/python-for-beginners/
/posts/django-tutorial/
/posts/my-first-project/
```

kabi URL'larni qabul qiladi.

### Qoidasi:

```text
<converter:name>
```

Masalan:

```python
<int:id>
```

```python
<slug:slug>
```

```python
<str:name>
```

---

# 23. Dynamic URL qanday ishlaydi?

Masalan:

```text
/posts/django-tutorial/
```

Django:

```text
URL
 ↓
posts/<slug:slug>/
 ↓
slug = "django-tutorial"
 ↓
post_detail(request, slug)
```

View:

```python
def post_detail(request, slug):
    ...
```

Shuning uchun URL'dagi:

```text
<slug:slug>
```

va view'dagi:

```python
slug
```

bir-biriga bog‘langan.

---

# 24. View yaratish

`blog/views.py`:

```python
from django.shortcuts import (
    get_object_or_404,
    render,
)

from .models import Post


def home(request):
    posts = (
        Post.objects
        .filter(published=True)
        .order_by("-created_at")[:5]
    )

    return render(
        request,
        "blog/home.html",
        {"posts": posts},
    )


def post_list(request):
    posts = (
        Post.objects
        .filter(published=True)
        .order_by("-created_at")
    )

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts},
    )


def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        published=True,
    )

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
```

---

# 25. Project URL

`config/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
```

Natija:

```text
/
    → home

/posts/
    → post list

/posts/my-first-post/
    → post detail
```

---

# 26. URL'ni qanday tekshirish kerak?

Agar:

```python
path("", home)
```

bo‘lsa:

```text
http://127.0.0.1:8000/
```

Agar:

```python
path("posts/", post_list)
```

bo‘lsa:

```text
http://127.0.0.1:8000/posts/
```

Agar:

```python
path(
    "posts/<slug:slug>/",
    post_detail,
)
```

bo‘lsa:

```text
http://127.0.0.1:8000/posts/django/
```

### Muhim xato

Agar `config/urls.py`:

```python
path("", include("blog.urls"))
```

bo‘lsa, `blog/urls.py` ichiga yana:

```python
path("blog/posts/", ...)
```

deb yozib yubormaysan.

Chunki prefix allaqachon project URL'dan kelishi mumkin.

---

# 27. Templates

Folder:

```text
blog/
└── templates/
    └── blog/
        ├── base.html
        ├── home.html
        ├── post_list.html
        └── post_detail.html
```

---

# 28. base.html

`blog/templates/blog/base.html`:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <title>
        {% block title %}
            Personal Blog
        {% endblock %}
    </title>
</head>

<body>

<header>
    <nav>
        <a href="{% url 'home' %}">
            Home
        </a>

        <a href="{% url 'post-list' %}">
            Blog
        </a>
    </nav>
</header>

<main>
    {% block content %}
    {% endblock %}
</main>

<footer>
    <p>© 2026 My Personal Blog</p>
</footer>

</body>
</html>
```

---

# 29. Template inheritance

`home.html`:

```html
{% extends "blog/base.html" %}


{% block title %}
    Home
{% endblock %}


{% block content %}

<h1>Welcome to my blog</h1>

{% for post in posts %}

<article>

    <h2>
        <a href="{% url 'post-detail' post.slug %}">
            {{ post.title }}
        </a>
    </h2>

    <p>
        {{ post.content|truncatewords:30 }}
    </p>

</article>

{% empty %}

<p>No posts yet.</p>

{% endfor %}

{% endblock %}
```

---

# 30. Django template syntax

Django template'da 3 ta asosiy syntax bor.

### Variable

```html
{{ post.title }}
```

### Tag

```html
{% for post in posts %}
```

### Comment

```html
{# comment #}
```

---

# 31. Post detail

`post_detail.html`:

```html
{% extends "blog/base.html" %}


{% block title %}
    {{ post.title }}
{% endblock %}


{% block content %}

<article>

    <h1>{{ post.title }}</h1>

    <p>
        {{ post.created_at }}
    </p>

    {% if post.image %}
        <img
            src="{{ post.image.url }}"
            alt="{{ post.title }}"
        >
    {% endif %}

    <div>
        {{ post.content|linebreaks }}
    </div>

</article>

{% endblock %}
```

---

# 32. Static files

CSS va JavaScript uchun:

```text
blog/
└── static/
    └── blog/
        ├── css/
        │   └── style.css
        │
        └── js/
            └── main.js
```

Template:

```html
{% load static %}

<link
    rel="stylesheet"
    href="{% static 'blog/css/style.css' %}"
>
```

---

# 33. Media files

Postga image yuklash uchun:

`settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

`config/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
```

Pastga:

```python
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
```

---

# 34. Image upload

Model:

```python
image = models.ImageField(
    upload_to="posts/",
    blank=True,
    null=True,
)
```

Pillow oldindan o‘rnatilgan:

```bash
uv add pillow
```

Model o‘zgargandan keyin:

```bash
uv run manage.py makemigrations
```

```bash
uv run manage.py migrate
```

---

# 35. CRUD

CRUD — Django'da juda muhim concept.

```text
C — Create
R — Read
U — Update
D — Delete
```

Ya'ni:

```text
Create → Post yaratish
Read   → Post ko‘rish
Update → Post edit qilish
Delete → Post o‘chirish
```

---

# 36. PostForm

`blog/forms.py`:

```python
from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "slug",
            "content",
            "image",
            "category",
            "published",
        ]
```

---

# 37. Create Post View

`blog/views.py`:

```python
from django.shortcuts import redirect, render

from .forms import PostForm


def post_create(request):

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()

            return redirect("post-list")

    else:
        form = PostForm()

    return render(
        request,
        "blog/post_form.html",
        {"form": form},
    )
```

---

# 38. Form template

`post_form.html`:

```html
{% extends "blog/base.html" %}


{% block content %}

<h1>Create Post</h1>

<form
    method="POST"
    enctype="multipart/form-data"
>

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Create
    </button>

</form>

{% endblock %}
```

### Juda muhim:

```html
enctype="multipart/form-data"
```

Image upload qilish uchun kerak.

---

# 39. Update Post

Keyingi CRUD bosqichida:

```text
/posts/<slug>/edit/
```

orqali postni edit qilamiz.

Logic:

```text
GET
 ↓
Formni ko‘rsat

POST
 ↓
Formni tekshir
 ↓
Database'ni update qil
 ↓
Redirect
```

---

# 40. Delete Post

Delete:

```text
/posts/<slug>/delete/
```

Logic:

```text
POST
 ↓
Post topiladi
 ↓
Delete
 ↓
Redirect
```

Delete uchun odatda GET emas, POST ishlatish xavfsizroq.

---

# 41. Authentication

Keyingi bosqich:

```text
Register
Login
Logout
Profile
```

Django authentication tizimi allaqachon mavjud:

```python
django.contrib.auth
```

Shuning uchun authenticationni noldan yozmaymiz.

---

# 42. User

Keyinchalik:

```text
users/
├── forms.py
├── views.py
├── urls.py
└── templates/
    └── users/
        ├── login.html
        ├── register.html
        └── profile.html
```

qilamiz.

---

# 43. Authorization

Authentication:

```text
Sen kimsan?
```

Authorization:

```text
Sen nima qilishga ruxsatlisan?
```

Masalan:

```text
Anonymous user
→ post o‘qishi mumkin

Logged-in user
→ comment yozishi mumkin

Admin/owner
→ post yaratishi mumkin

Owner
→ o‘z postini edit/delete qilishi mumkin
```

---

# 44. Comments

Keyinchalik:

```python
class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
```

Natija:

```text
Post
 ├── Comment
 ├── Comment
 └── Comment
```

---

# 45. Category

Category misollari:

```text
Python
Django
Backend
AWS
Programming
University
Career
```

URL:

```text
/category/python/
```

yoki keyinchalik:

```text
/category/django/
```

---

# 46. Search

Masalan user:

```text
Search: Django
```

qiladi.

View'da:

```python
Post.objects.filter(
    title__icontains=query
)
```

ishlatish mumkin.

Keyinchalik:

```text
title
+
content
+
category
```

bo‘yicha search qilamiz.

---

# 47. Pagination

100 ta postni bitta sahifada chiqarish yaxshi emas.

Masalan:

```text
Page 1

1 2 3 4 5
```

Django:

```python
from django.core.paginator import Paginator
```

orqali pagination beradi.

---

# 48. PostgreSQL bilan ishlash

Bizning project boshidanoq PostgreSQL ishlatadi:

```text
Django
   ↓
psycopg
   ↓
PostgreSQL
```

`.env`:

```env
DB_NAME=personal_blog
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Database configuration environment orqali boshqariladi.

---

# 49. .env va security

Secret ma'lumotlarni GitHub'ga yubormaymiz.

`.env`:

```env
SECRET_KEY=...
DEBUG=True

DB_NAME=personal_blog
DB_USER=postgres
DB_PASSWORD=...
DB_HOST=localhost
DB_PORT=5432
```

`.gitignore`:

```gitignore
.venv/
.env
__pycache__/
*.pyc
media/
```

SQLite ishlatmaganimiz uchun:

```text
db.sqlite3
```

ham kerak emas.

---

# 50. Production security

Productionga chiqqanda:

```python
DEBUG = False
```

bo‘ladi.

`ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS = [
    "yourdomain.com",
    "www.yourdomain.com",
]
```

Secret key `.env` ichida qoladi.

---

# 51. Testing

Keyinchalik testlar:

```text
tests/
├── test_models.py
├── test_views.py
└── test_urls.py
```

Masalan:

```python
def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
```

Test qilishimiz kerak:

```text
Models
Views
URLs
Forms
Authentication
CRUD
```

---

# 52. Git

Har bir katta feature'dan keyin:

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "add post model"
```

```bash
git push
```

Branchlar:

```text
main
│
├── feature/blog-model
├── feature/auth
├── feature/comments
└── feature/search
```

---

# 53. Deployment

Oxirida AWS serverga deploy qilamiz.

Architecture:

```text
User
 ↓
Domain
 ↓
Nginx
 ↓
Gunicorn
 ↓
Django
 ↓
PostgreSQL
```

Static:

```text
Nginx → static/
```

Media:

```text
Nginx → media/
```

Process manager:

```text
systemd
```

HTTPS:

```text
Let's Encrypt
```

---

# 54. Final production architecture

```text
                  INTERNET
                     │
                     ▼
                  DOMAIN
                     │
                     ▼
                   NGINX
                     │
                     ▼
                 GUNICORN
                     │
                     ▼
                  DJANGO
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        BLOG       USERS     COMMENTS
          │          │          │
          └──────────┼──────────┘
                     ▼
                POSTGRESQL
```

---

# 55. Django'da o‘rganadigan topics

Bu project davomida:

```text
01. Django project
02. Django app
03. settings.py
04. URL routing
05. Views
06. Templates
07. Template inheritance
08. Models
09. Migrations
10. Django ORM
11. Admin
12. Forms
13. ModelForms
14. CRUD
15. Static files
16. Media files
17. Authentication
18. Authorization
19. Relationships
20. ForeignKey
21. Search
22. Filtering
23. Pagination
24. Messages
25. PostgreSQL
26. Environment variables
27. Security
28. Testing
29. Git/GitHub
30. Deployment
31. Nginx
32. Gunicorn
33. systemd
34. HTTPS
35. Domain
```

---

# 56. Eng muhim Django mental model

Mana buni reference qilib yur:

```text
                 USER
                   │
                   ▼
                Browser
                   │
              HTTP Request
                   │
                   ▼
                urls.py
                   │
                   ▼
                views.py
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
       models.py         forms.py
          │                 │
          ▼                 ▼
     PostgreSQL          HTML Form
          │                 │
          └────────┬────────┘
                   ▼
                Template
                   │
                   ▼
             HTTP Response
                   │
                   ▼
                Browser
```

Agar biror narsa ishlamasa, shu tartibda tekshir:

```text
1. URL to‘g‘rimi?
       ↓
2. View chaqirilyaptimi?
       ↓
3. Model/database to‘g‘rimi?
       ↓
4. Context to‘g‘rimi?
       ↓
5. Template to‘g‘rimi?
       ↓
6. Static/media to‘g‘rimi?
```

---

# 57. Projectni qanday ketma-ket quramiz?

MUHIM.

Hamma narsani birdan yozmaymiz.

Quyidagi tartibdan chiqmaymiz:

```text
PHASE 1
Django Setup
       ↓
PHASE 2
PostgreSQL Setup
       ↓
PHASE 3
URLs + Views
       ↓
PHASE 4
Templates + CSS
       ↓
PHASE 5
Models + PostgreSQL
       ↓
PHASE 6
Admin
       ↓
PHASE 7
CRUD
       ↓
PHASE 8
Authentication
       ↓
PHASE 9
Comments + Categories
       ↓
PHASE 10
Search + Pagination
       ↓
PHASE 11
Testing
       ↓
PHASE 12
Git/GitHub
       ↓
PHASE 13
AWS Deployment
       ↓
PHASE 14
Nginx + Gunicorn + systemd
       ↓
PHASE 15
HTTPS + Domain
```

---

# 58. PHASE 1 — Django Setup

Birinchi bosqichda faqat:

```text
Project
Virtual environment
Django
blog app
users app
settings
```

qilamiz.

Commandlar:

```bash
mkdir personal-blog
cd personal-blog
```

```bash
uv venv
```

Git Bash:

```bash
source .venv/Scripts/activate
```

```bash
uv add django psycopg python-dotenv pillow
```

```bash
uv run django-admin startproject config .
```

```bash
uv run manage.py startapp blog
```

```bash
uv run manage.py startapp users
```

---

# 59. PHASE 2 — PostgreSQL

PostgreSQL database:

```text
personal_blog
```

`.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=personal_blog
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

`settings.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv(BASE_DIR / ".env")
```

Database:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
```

Keyin:

```bash
uv run manage.py migrate
```

---

# 60. PHASE 3 — URLs + Views

Avval:

```text
/
```

Home.

Keyin:

```text
/posts/
```

Post list.

Keyin dynamic:

```text
/posts/<slug>/
```

Post detail.

---

# 61. PHASE 4 — Templates + CSS

Yaratamiz:

```text
base.html
home.html
post_list.html
post_detail.html
```

Keyin:

```text
style.css
```

Template inheritance:

```text
base.html
    ↓
home.html
post_list.html
post_detail.html
```

---

# 62. PHASE 5 — Models + PostgreSQL

Models:

```text
Category
Post
```

Keyin:

```bash
uv run manage.py makemigrations
```

```bash
uv run manage.py migrate
```

Database:

```text
PostgreSQL
```

---

# 63. PHASE 6 — Admin

Admin:

```text
Category
Post
```

Superuser:

```bash
uv run manage.py createsuperuser
```

Admin:

```text
/admin/
```

---

# 64. PHASE 7 — CRUD

Quriladi:

```text
Create
Read
Update
Delete
```

Post:

```text
Create Post
Edit Post
Delete Post
View Post
```

Image upload ham shu bosqichda ishlaydi.

---

# 65. PHASE 8 — Authentication

Quriladi:

```text
Register
Login
Logout
Profile
```

Keyin authorization:

```text
Kim nima qila oladi?
```

---

# 66. PHASE 9 — Comments + Categories

Category:

```text
Python
Django
Backend
AWS
Career
```

Comments:

```text
User
 ↓
Comment
 ↓
Post
```

---

# 67. PHASE 10 — Search + Pagination

Search:

```text
Django
```

Pagination:

```text
1 2 3 4 5
```

---

# 68. PHASE 11 — Testing

Test qilamiz:

```text
Models
Views
URLs
Forms
Authentication
CRUD
```

---

# 69. PHASE 12 — Git/GitHub

Repository:

```text
personal-blog
```

Branchlar:

```text
main
feature/blog
feature/auth
feature/comments
feature/search
```

---

# 70. PHASE 13 — AWS

Local project:

```text
Windows
   ↓
GitHub
   ↓
AWS Ubuntu
```

Serverga project olib chiqamiz.

---

# 71. PHASE 14 — Production

Production architecture:

```text
Nginx
 ↓
Gunicorn
 ↓
Django
 ↓
PostgreSQL
```

systemd orqali Django processni doimiy ishlatamiz.

---

# 72. PHASE 15 — HTTPS + Domain

Oxirida:

```text
https://yourdomain.com
```

qilamiz.

HTTPS:

```text
Let's Encrypt
```

Nginx bilan ishlaydi.

---

# 73. Eng muhim commandlar — QUICK REFERENCE

### Environment

```bash
uv venv
```

```bash
source .venv/Scripts/activate
```

### Package

```bash
uv add django psycopg python-dotenv pillow
```

### Project

```bash
uv run django-admin startproject config .
```

### App

```bash
uv run manage.py startapp blog
```

```bash
uv run manage.py startapp users
```

### Server

```bash
uv run manage.py runserver
```

### Migration

```bash
uv run manage.py makemigrations
```

```bash
uv run manage.py migrate
```

### Superuser

```bash
uv run manage.py createsuperuser
```

### Django shell

```bash
uv run manage.py shell
```

### Check

```bash
uv run manage.py check
```

---

# 74. Migration commandini adashtirmaslik

Har doim:

```text
models.py o‘zgardi
        ↓
uv run manage.py makemigrations
        ↓
uv run manage.py migrate
```

`makemigrations`:

```text
Migration fayl yaratadi
```

`migrate`:

```text
Migrationni PostgreSQL'ga qo‘llaydi
```

---

# 75. Django'da xato chiqsa

Masalan:

```text
404
```

bo‘lsa:

```text
urls.py
```

tekshir.

```text
TemplateDoesNotExist
```

bo‘lsa:

```text
templates/
```

tekshir.

```text
ProgrammingError
```

bo‘lsa:

```text
models.py
migration
PostgreSQL
```

tekshir.

```text
NoReverseMatch
```

bo‘lsa:

```text
{% url %}
path(...)
name=
```

tekshir.

```text
ModuleNotFoundError
```

bo‘lsa:

```text
package
app
import
virtual environment
```

tekshir.

```text
Port already in use
```

bo‘lsa:

```text
8000 portni boshqa process ishlatyapti.
```

---

# 76. Django projectni tushunish uchun asosiy qoida

Har bir yangi feature uchun o‘zingga shu savollarni ber:

```text
1. URL kerakmi?
       ↓
2. View kerakmi?
       ↓
3. Database kerakmi?
       ↓
4. Model kerakmi?
       ↓
5. Form kerakmi?
       ↓
6. Template kerakmi?
       ↓
7. Static/media kerakmi?
       ↓
8. Authentication/permission kerakmi?
```

Shunda Django'da adashish ancha kamayadi.

---

# 77. Final mental model

Personal Blog'da user:

```text
Browser
   ↓
URL
   ↓
urls.py
   ↓
views.py
   ↓
ORM
   ↓
PostgreSQL
   ↓
views.py
   ↓
Template
   ↓
HTML
   ↓
Browser
```

Post yaratishda:

```text
Browser
   ↓
POST request
   ↓
View
   ↓
Form
   ↓
Validation
   ↓
Model
   ↓
PostgreSQL
```

Image bilan:

```text
Browser
   ↓
multipart/form-data
   ↓
request.FILES
   ↓
ImageField
   ↓
media/posts/
```

Productionda:

```text
Internet
   ↓
Domain
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django
   ↓
PostgreSQL
```

---

# 78. Bizning asosiy qoida

Bu projectni **birdaniga yozmaymiz**.

Har bir PHASE tugagandan keyin tekshiramiz.

```text
PHASE 1
   ↓
ishlayaptimi?
   ↓
PHASE 2
   ↓
ishlayaptimi?
   ↓
PHASE 3
   ↓
ishlayaptimi?
```

Shu tarzda oxirigacha boramiz.

**PostgreSQL esa projectning boshidan ishlaydi. SQLite'ga o'tish bosqichi yo‘q.**
