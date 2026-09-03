# AI-Assisted Box Selection System

## Overview

This project is a Django-based web application that recommends a
suitable shipping box for a product.

The application checks the product's dimensions and weight against
available box dimensions and maximum weight capacity. Among suitable
boxes, it recommends the box with the least unused space.

## Features

- Product management through Django Admin
- Shipping box management through Django Admin
- Product dimension validation
- Product weight validation
- Automatic box recommendation
- Handles cases where no suitable box is available
- Automated unit tests
- Simple web interface

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
box_selection_system/
│
├── box_selector/
│   ├── migrations/
│   ├── templates/
│   │   └── box_selector/
│   │       └── recommend.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
└── TEST_OUTPUT.md