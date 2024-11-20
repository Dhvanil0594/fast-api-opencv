<!-- # fast-api-opencv


# Pretrained Model Download :
[Fruits Pretrained Model](https://drive.google.com/file/d/1H4JVP9GX1v4z3_EcJ5CZFijloJ6noHXV/view?usp=drive_link)

## Download the model and put it in this place 
```
fast-api-opencv/src/api/v1/constants
``` -->
# Employee Attendance System with Face Recognition

This project is an Employee Attendance System built using **FastAPI** and **PostgreSQL**, which leverages **DeepFace** for face recognition. The system allows employees to register, upload their photos, and mark their attendance based on facial recognition.

## Project Features

- **Employee Registration**: Employees can register with their name, position, email, and password.

- **Employee Photo Upload**: After registration, employees can upload their photos, which will be used for facial recognition.

- **Attendance Marking**: The system uses facial recognition to mark attendance based on uploaded images.

- **Face Recognition using DeepFace**: Utilizes the DeepFace framework to match uploaded images with stored photos.

## Prerequisites

- Python 3.8 or higher

- PostgreSQL Database

- FastAPI

- DeepFace library

- OpenCV

- Uvicorn (for FastAPI server)

## Installation

1\. Clone the repository:

    ```bash

    git clone https://github.com/Dhvanil0594/fast-api-opencv.git

    cd fast-api-opencv

    ```

2\. Set up a virtual environment and install dependencies:

    ```bash

    python3 -m venv venv

    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    pip install -r requirements.txt

    ```

3\. Install PostgreSQL and set up your database:

    - Ensure you have PostgreSQL installed and a database created for the project.

    - Update the database URL in the environment configuration or `config.py`.

4\. Set Up the Database

    - You may need to set up the database (MySQL or SQLite, depending on your configuration). You can use Alembic to handle database migrations.

    - To initialize the database schema, run the following command (make sure you’ve configured `alembic.ini` to match your database settings):

    ```bash
    alembic upgrade head
    ```

    - optional:
    * If you need to recreate the database, you can run the following command:

    ```bash
    alembic downgrade base
    ```

    * You can also use `alembic downgrade head` to roll back to the latest version.

    * If you want to update the database, you can use following command:
    ```bash
    alembic revision --autogenerate -m "update database"
    ```

4\. Set up the DeepFace model:

    - DeepFace will automatically download the pre-trained models needed for facial recognition.

    - You need to provide a directory path for saving facial data in `db_path`.

5\. Run the FastAPI app:

    ```bash

    uvicorn main:app --reload

    ```

## API Endpoints

### 1. Register Employee

Register a new employee by providing their details: `name`, `position`, `email`, and `password`.

#### Request:

```bash

curl -X 'POST'

  'http://0.0.0.0:8001/api/v1/employee-auth/register'

  -H 'accept: application/json'

  -H 'Content-Type: application/json'

  -d '{

  "name": "employee_name",

  "position": "job_title",

  "email": "user@example.com",

  "password": "password"

}'

```

#### Response:

```json

{

  "message": "Employee registered successfully"

}

```

---

### 2. Upload Employee Photo

After registration, employees need to upload a photo for facial recognition. This photo will be used for matching when they mark attendance.

#### Request:

```bash

curl --location 'http://0.0.0.0:8001/api/v1/employee-auth/upload_image/5'

--form 'file=@"/path/to/photo.jpg"'

```

#### Response:

```json

{

  "message": "Image uploaded and face registered successfully"

}

```

---

### 3. Mark Attendance Using Face Recognition

Employees can mark their attendance by uploading a photo for face recognition. The system will match the uploaded image with the registered employees.

#### Request:

```bash

curl --location 'http://0.0.0.0:8001/api/v1/employee-detection/upload_image'

--form 'file=@"/path/to/image.jpg"'

```

#### Response:

```json

{

  "message": "Attendance marked successfully",

  "employee_id": 5

}

```

---

## DeepFace Face Recognition Integration

DeepFace is used to match the uploaded photo against the stored images. The following code snippet shows how DeepFace is used to perform the face recognition:

```python

from deepface import DeepFace

dfs = DeepFace.find(

    img_path = "img1.jpg",  # The image to match

    db_path = "path/to/database",  # The directory where the images are stored

)

```

The system uses this `find` function to search for the closest match in the database and returns the corresponding employee's ID for attendance marking.

## Database Setup

The project uses PostgreSQL to store employee data and uploaded images. The database should have the following structure:

### Employees Table

- `id`: Primary Key, Auto Increment

- `name`: Employee's name

- `position`: Job title of the employee

- `email`: Email address

- `password`: Hashed password

### Photos Table

- `id`: Primary Key, Auto Increment

- `employee_id`: Foreign key to Employees table

- `photo_path`: Path to the uploaded photo

## Running the Application

1\. **Start PostgreSQL database** (if not already running).

2\. **Run the FastAPI app**:

    ```bash

    uvicorn main:app --reload

    ```

3\. **Access the app** at `http://0.0.0.0:8001` or your configured server URL.


## Dependencies

- `fastapi`: The web framework used to build the APIs.

- `uvicorn`: ASGI server for running the FastAPI app.

- `psycopg2`: PostgreSQL adapter for Python.

- `deepface`: Facial recognition library used for the matching.

- `opencv-python`: Library for image processing.

- `pydantic`: Data validation and settings management.