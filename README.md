# Banking Application API
This project implements a RESTful API for a banking application using Flask, MySQL, and SQLAlchemy. It provides endpoints for user management, account management, transaction management, and basic financial functionalities.

## Features Implemented
1. RESTful API Endpoints:
- User Management
- Account Management
- Transaction Management
- Budget Management
- Bill Management

2. Database Models:
- User: Represents user accounts.
- Account: Represents user accounts with account type, balance, etc.
- Transaction: Represents financial transactions with details like amount, type, etc.
- Budget: Represents budget categories for expense tracking.
Bill: Represents scheduled bill payments.

3. Authentication:
Session-based authentication using Flask-Login.

## Setup and Installation
1. Clone the Repository:
    - git clone https://github.com/your/repository.git
    - cd repository
2. Install Dependencies:
    - pip install -r requirements.txt
3. Set Up Environment Variables:
    - Create a .env file in the root directory with the following configuration:
dotenv
DATABASE_URI=mysql+pymysql://username:password@localhost/dbname
SECRET_KEY=your_secret_key
Replace username, password, localhost, and dbname with your actual database credentials.
    - Initialize Database:
        flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
    - Run the Application:
        flask run

## API Endpoints
1. User Management
    POST /auth/register: Create a new user account.
    ![alt text](image.png)
    POST /auth/login: Authenticate user and generate session token.
    ![alt text](image-1.png)
    POST /auth/logout: Logout the currently authenticated user.
    ![alt text](image-2.png)

2. Account Management
    GET /accounts: Retrieve all accounts.
    ![alt text](image-3.png)
    GET /accounts/:id: Retrieve details of a specific account.
    POST /accounts: Create a new account.
    ![alt text](image-4.png)
    PUT /accounts/:id: Update details of an existing account.
    DELETE /accounts/:id: Delete an account.
3. Transaction Management
    GET /transactions: Retrieve all transactions.
    ![alt text](image-5.png)
    GET /transactions/:id: Retrieve details of a specific transaction.
    POST /transactions: Create a new transaction (deposit, withdrawal, transfer).
    ![alt text](image-6.png)

4. Database Management
    Stored Users
    ![alt text](image-7.png)
    Stored Accounts
    ![alt text](image-8.png)
    Stored Transaction
    ![alt text](image-9.png)

## Error Handling
Proper error handling and validation are implemented for each endpoint to handle potential errors and provide meaningful error messages.

## POSTMAN Documentation
https://documenter.getpostman.com/view/34484533/2sA3e1AUpx