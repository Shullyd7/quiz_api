# Quiz API

## Description

This project provides an API for managing quizzes and questions. It allows users to create, retrieve, update, and delete questions and quizzes. Users can also submit quizzes and get their scores.

## Requirements

- Python 3.x
- Django 3.x
- Django Rest Framework 3.x

## API Endpoints

### Questions

#### List/Create Questions

- **Endpoint:** `/questions/`
- **Method:** GET, POST
- **Description:** Fetch a list of questions or create a new question.
- **Request Body (POST):**
  ```json
  {
    "text": "Question text",
    "options": ["Option 1", "Option 2", "Option 3"],
    "correct_option": 0
  }
  ```
- **Response Body:** List of questions or newly created question.

#### Retrieve/Update/Delete Question

- **Endpoint:** `/questions/<int:pk>/`
- **Method:** GET, PUT, PATCH, DELETE
- **Description:** Retrieve, update, or delete a specific question by its ID.
- **Request Body (PUT/PATCH):**
  ```json
  {
    "text": "Updated question text",
    "options": ["Updated option 1", "Updated option 2", "Updated option 3"],
    "correct_option": 1
  }
  ```
- **Response Body:** Retrieved, updated, or deleted question.

### Quizzes

#### List/Create Quizzes

- **Endpoint:** `/quizzes/`
- **Method:** GET, POST
- **Description:** Fetch a list of quizzes or create a new quiz.
- **Request Body (POST):**
  ```json
  {
    "name": "Quiz name",
    "questions": [1, 2, 3],
    "start_time": "2024-05-10T08:00:00Z",
    "end_time": "2024-05-10T09:00:00Z"
  }
  ```
- **Response Body:** List of quizzes or newly created quiz.

#### Retrieve/Update/Delete Quiz

- **Endpoint:** `/quizzes/<int:pk>/`
- **Method:** GET, PUT, PATCH, DELETE
- **Description:** Retrieve, update, or delete a specific quiz by its ID.
- **Request Body (PUT/PATCH):**
  ```json
  {
    "name": "Updated quiz name",
    "questions": [4, 5, 6],
    "start_time": "2024-05-11T08:00:00Z",
    "end_time": "2024-05-11T09:00:00Z"
  }
  ```
- **Response Body:** Retrieved, updated, or deleted quiz.

#### Submit Quiz

- **Endpoint:** `/quizzes/<int:quiz_id>/submit/`
- **Method:** POST
- **Description:** Submit a quiz response for scoring.
- **Request Body:**
  ```json
  {
    "user": "JohnDoe",
    "answers": {
      "1": 2,
      "2": 3,
      "3": 1
    }
  }
  ```
- **Response Body:** Quiz response with score and details.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/Shullyd7/quiz_api.git
   ```

2. Navigate to the project directory:

   ```
   cd quiz-api
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Run the Server

```
python manage.py runserver
```

## Admin Interface

- **URL:** `/admin/`
- **Username:** jvec
- **Password:** password

## Postman Collection

Import the Postman collection provided (`JVEC.postman_collection.json`) to run the APIs on localhost.