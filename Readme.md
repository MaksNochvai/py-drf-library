# Library API

-----------------------------------

### Project Description
The Library Management System is an online platform designed to revolutionize the way a library operates. It provides a web-based interface for managing books, book borrowings, customers, payments. The system aims to optimize the library administration process and enhance user experience.

----

## Project Structure

### Architecture
The system follows a microservices architecture with the following components:

- Books Service: Manages books' inventory and information.
- Users Service: Handles user registration and authentication.
- Borrowings Service: Manages book borrowings and return processes.
- Payments Service (Stripe): Handles payments for borrowings.

- Components

### Books Service
The Books Service is responsible for managing books' inventory and information.

API Endpoints:
```
POST /books/ - Add a new book.
GET /books/ - Get a list of books.
GET /books/<id>/ - Get detailed information about a book.
PUT/PATCH /books/<id>/ - Update book details (including inventory).
DELETE /books/<id>/ - Delete a book.
```

### Users Service
The Users Service handles user registration and authentication.

API Endpoints:
```
POST /users/ - Register a new user.
POST /users/token/ - Get JWT tokens for authentication.
POST /users/token/refresh/ - Refresh JWT tokens.
GET /users/me/ - Get the user's profile information.
PUT/PATCH /users/me/ - Update the user's profile.
```
### Borrowings Service
The Borrowings Service manages users' book borrowings.

API Endpoints:
```
POST /borrowings/ - Add a new borrowing (decreases inventory).
GET /borrowings/ - Get borrowings by user ID and active status.
GET /borrowings/<id>/ - Get details of a specific borrowing.
POST /borrowings/<id>/return/ - Mark borrowing as returned (increases inventory).
```

### Payments Service (Stripe)
The Payments Service handles payments for book borrowings using Stripe.

API Endpoints:
```
GET /success/ - Check successful Stripe payment.
GET /cancel/ - Return payment paused message.
```
# Install PostgreSQL and create a database

1. Clone the repository:
git clone https://github.com/MaksNochvai/py-drf-library
2. Change directory after cloning:
```
git checkout -b develop
```
3. Set up a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate # Activation of the virtual environment (Unix)
venv\Scripts\activate # Activation of the virtual environment (Windows)
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Create .env file using the schema you can see in the .env_sample file

6. Start the development server:
```
python manage.py migrate
python manage.py runserver
```
# Run with docker

-----------------------------------
docker should be installed
```
docker-compose build
docker-compose up
```
# Getting access

------------------------------------
- create user via /api/users/register/
- get access token via /api/users/token/

## Features
- Book Inventory Management: Add, update, and delete books from the library's inventory. Keep track of book availability.

- Book Borrowing: Allow users to borrow books. Track borrowing dates, expected return dates, and actual return dates.

- User Authentication: Users can register, log in, and update their profile information. Authentication is managed securely with JWT tokens.

- Payment Handling: Enable users to make payments for borrowings through the integrated Stripe payment gateway.

- Admin Dashboard: Provide administrators with an overview of library operations, including book inventory, active borrowings, and payments.


------
## Technologies Used
The Library API is built with the following technologies:

- Python: The primary programming language used for backend development.

- Django REST framework: An extension of Django that simplifies building RESTful APIs.

- PostgreSQL: A powerful open-source relational database used for storing data related to books, borrowings, and users.

- Stripe: A popular online payment processing platform used to handle payments securely.

- JWT (JSON Web Tokens): Used for user authentication and secure communication between the frontend and backend.

- Docker: Used for containerization and deployment of the application.

- Git: Version control system for tracking changes.

- GitHub: A platform for hosting and managing the project's source code.

--------------------------------------------------------------------------------------
