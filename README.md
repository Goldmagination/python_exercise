# Flask REST API

This is a REST API built with Flask for managing messages. Each message is associated with a user, and the API is secured with Basic HTTP Authentication.

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Goldmagination/python_exercise.git
cd python_exercise
```

### 2. Create a Virtual Environment

Set up a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Environment Variables

In `config.py`, you'll find the connection string to the database, which you should adjust as needed
```
DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
```

### 5. Initialize the Database

Run the following commands to set up the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

This will create the necessary tables in the database.

### 6. Run the Application

Start the Flask application:

```bash
flask run
```

The application will start on `http://127.0.0.1:5000/` by default.

## API Endpoints

### 1. Register a New User

Necessary to communicate with the app

- **Endpoint:** `POST /register`
- **Description:** Registers a new user.
- **Request:**
  - URL: `http://127.0.0.1:5000/register`
  - Method: `POST`
  - Body (JSON):
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    ```
- **Response:**
  - Status: `201 Created`
  - Body:
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    ```

### 2. Get All Messages

- **Endpoint:** `GET /messages`
- **Description:** Retrieves all messages for the authenticated user.
- **Request:**
  - URL: `http://127.0.0.1:5000/messages`
  - Method: `GET`
  - Headers:
    - `Authorization: Basic Auth`
- **Response:**
  - Status: `200 OK`
  - Body (example):
    ```json
    [
        {
            "id": "generated_uuid",
            "content": "This is a test message",
            "retrieval_count": 0,
            "user_id": "user_id"
        }
    ]
    ```

### 3. Get a Specific Message

- **Endpoint:** `GET /messages/<string:message_id>`
- **Description:** Retrieves a specific message by its uuID for the authenticated user.
- **Request:**
  - URL: `http://127.0.0.1:5000/messages/<message_id>`
  - Method: `GET`
  - Headers:
    - `Authorization: Basic Auth`
- **Response:**
  - Status: `200 OK`
  - Body (example):
    ```json
    {
        "id": "generated_uuid",
        "content": "This is a test message",
        "retrieval_count": 1,
        "user_id": "user_id"
    }
    ```

### 4. Create a New Message

- **Endpoint:** `POST /messages`
- **Description:** Creates a new message for the authenticated user.
- **Request:**
  - URL: `http://127.0.0.1:5000/messages`
  - Method: `POST`
  - Headers:
    - `Authorization: Basic Auth`
  - Body (JSON):
    ```json
    {
        "content": "This is a test message"
    }
    ```
- **Response:**
  - Status: `201 Created`
  - Body:
    ```json
    {
        "id": "generated_uuid",
        "content": "This is a test message",
        "retrieval_count": 0,
        "user_id": "user_id"
    }
    ```

### 5. Update a Message

- **Endpoint:** `PUT /messages/<int:message_id>`
- **Description:** Updates the content of a specific message for the authenticated user.
- **Request:**
  - URL: `http://127.0.0.1:5000/messages/<message_id>`
  - Method: `PUT`
  - Headers:
    - `Authorization: Basic Auth`
  - Body (JSON):
    ```json
    {
        "content": "Updated message content"
    }
    ```
- **Response:**
  - Status: `200 OK`
  - Body:
    ```json
    {
        "id": "generated_uuid",
        "content": "Updated message content",
        "retrieval_count": 1,
        "user_id": "user_id"
    }
    ```

### 6. Delete a Message

- **Endpoint:** `DELETE /messages/<int:message_id>`
- **Description:** Deletes a specific message by its ID for the authenticated user.
- **Request:**
  - URL: `http://127.0.0.1:5000/messages/<message_id>`
  - Method: `DELETE`
  - Headers:
    - `Authorization: Basic Auth`
- **Response:**
  - Status: `200 OK`
  - Body:
    ```json
    {
        "result": "success"
    }
    ```

