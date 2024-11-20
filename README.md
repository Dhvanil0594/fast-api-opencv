# Employee Attendance System with Face Recognition 🎯

This is a modern **Employee Attendance System** powered by **FastAPI**, **PostgreSQL**, and the **DeepFace** framework for facial recognition. 🚀 The system streamlines attendance management by using facial recognition technology, offering a seamless and secure experience for employees and administrators.

---

## 🔥 Key Features

✅ **Employee Registration**: Register employees with their name, position, email, and password.  

✅ **Photo Upload**: Employees upload photos for facial recognition.  

✅ **Attendance Marking**: Attendance is automatically marked by recognizing the uploaded face.  

✅ **Advanced Face Recognition**: Powered by DeepFace to ensure accuracy and reliability.  

✅ **FastAPI Framework**: Provides a blazing-fast API for smooth integration.

---

## 🛠️ Prerequisites

Before you get started, ensure the following tools and frameworks are installed:

- Python 3.8+  

- PostgreSQL Database  

- FastAPI Framework  

- DeepFace Library  

- OpenCV for image processing  

- Uvicorn ASGI server

---

## 🚀 Quick Start Guide

### Step 1: Clone the Repository

```
git clone https://github.com/Dhvanil0594/fast-api-opencv.git

cd fast-api-opencv

```

### Step 2: Set Up Virtual Environment & Install Dependencies

```
python3 -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt

```

### Step 3: Configure PostgreSQL Database

- Install PostgreSQL and create a database for the project.  

- Update the database URL in the configuration file (`config.py` or environment variables).

### Step 4: Initialize the Database Schema

```
alembic upgrade head

```

**Optional Commands**:  

- **Reset Database**: `alembic downgrade base`  

- **Roll Back Migration**: `alembic downgrade head`  

- **Create New Revision**: `alembic revision --autogenerate -m "update database"`

### Step 5: Set Up DeepFace for Face Recognition

- DeepFace will download pre-trained models automatically.  

- Configure the directory (`db_path`) for saving facial data.

### Step 6: Launch the App 🚀

```
uvicorn main:app --reload

```

---

## 📡 API Endpoints

### 1️⃣ Register Employee

**Endpoint**: `/api/v1/employee-auth/register`  

**Method**: `POST`  

**Description**: Register a new employee with their details.

#### Example Request:

```
curl -X POST 'http://0.0.0.0:8001/api/v1/employee-auth/register'

-H 'Content-Type: application/json'

-d '{

  "name": "John Doe",

  "position": "Software Engineer",

  "email": "john.doe@example.com",

  "password": "securepassword"

}'

```

#### Example Response:

```
{

  "message": "Employee registered successfully"

}

```

---

### 2️⃣ Upload Employee Photo

**Endpoint**: `/api/v1/employee-auth/upload_image/{employee_id}`  

**Method**: `POST`  

**Description**: Upload a photo for face recognition.

#### Example Request:

```
curl --location 'http://0.0.0.0:8001/api/v1/employee-auth/upload_image/5'

--form 'file=@"/path/to/photo.jpg"'

```

#### Example Response:

```
{

  "message": "Image uploaded and face registered successfully"

}

```

---

### 3️⃣ Mark Attendance

**Endpoint**: `/api/v1/employee-detection/upload_image`  

**Method**: `POST`  

**Description**: Mark attendance by uploading a photo for recognition.

#### Example Request:

```bash

curl --location 'http://0.0.0.0:8001/api/v1/employee-detection/upload_image'

--form 'file=@"/path/to/image.jpg"'

```

#### Example Response:

```
{

  "message": "Attendance marked successfully",

  "employee_id": 5

}

```

---

## 💡 How Face Recognition Works

The system leverages **DeepFace** to compare the uploaded image with stored images in the database. The following code snippet illustrates the process:

```
from deepface import DeepFace

results = DeepFace.find(

    img_path="img1.jpg",  # Image to be matched

    db_path="path/to/database"  # Directory containing stored images

)

```

---

## 🗂️ Database Schema

### Employees Table

| Column      | Type        | Description                        |

|-------------|-------------|------------------------------------|

| `id`        | Integer     | Primary Key (Auto Increment)       |

| `name`      | String      | Employee Name                     |

| `position`  | String      | Job Title                         |

| `email`     | String      | Employee Email Address            |

| `password`  | String      | Hashed Password                   |

### Photos Table

| Column        | Type        | Description                        |

|---------------|-------------|------------------------------------|

| `id`          | Integer     | Primary Key (Auto Increment)       |

| `employee_id` | Integer     | Foreign Key to Employees Table     |

| `photo_path`  | String      | Path to the Uploaded Photo         |

---

## 💻 Dependencies

- **FastAPI**: Framework for building APIs.  

- **Uvicorn**: ASGI server for FastAPI.  

- **Psycopg2**: PostgreSQL adapter for Python.  

- **DeepFace**: Facial recognition library.  

- **OpenCV**: Image processing library.  

- **Pydantic**: Data validation and parsing.

---
