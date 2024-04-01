
# Di8it Labs - Test API


## Installation

To get started with the project, follow these steps:

### Prerequisites

- Python 3.11 or higher
- Pip package manager

### Clone the repository
- Clone this repository
- Open terminal/cmd at the cloned repository


### Create and activate a virtual environment

- python -m venv venv
- source venv/bin/activate # For Linux/Mac
- venv\Scripts\activate # For Windows


### Install dependencies

- pip install -r requirements.txt

### Set Environment Variables (.env) file

- Create .env file in the root directory and set the following variables:
    
        PRODUCTION (Value can be True or False)
        ALLOWED_HOSTS (List of Strings e.g. ["localhost","127.0.0.1"])

        DB_HOST=localhost
        DB_PORT=5432
        DB_NAME=db_name
        DB_USER=user_name
        DB_USER_PASSWORD=user_pass

    

### Execute necessary sql for creating tables and procedures
- ***Locker***: Execute ***table_procedure_locker.sql*** in the root file
- ***Definition***: Execute ***table_procedure_locker.sql*** in the root file
    

### Start the development server

- python manage.py runserver

You should now be able to access the API at http://localhost:8000/ or the specified port.


## API Endpoints

Below is a list of available API endpoints.

Please ensure to specify the version number at the beginning of the endpoint URL.

For example, /v1/locker/


### Locker
- <span style='color:#FFD13E'>**URL**: /locker/</span>
- **Description**: Create locker
- **Method**: POST
---
- <span style='color:#FFD13E'>**URL**: /locker/<str:id>/</span>
- **Description**: Update an exisitng locker
- **Method**: PUT
- To update the data you need to send the payload with updated data fields
- **Note**: <span style='color:#FFD13E'>To update the data, you need to send the complete payload with updated field values that need to be updated and leave the rest as it is for that particular entry. </span>

#### Request Body
```json
{
    "name": "locker 1",
    "description": "Small locker for personal belongings",
    "lockerdata": {
        "username": "user",
        "password": "pass456",
        "port": "1234",
        "domain": "example.com",
        "database": "db1",
        "pam": {
            "pamcredbit": "abc123",
            "PAMConfigurationID": "config456",
            "PamUserID": "user"
        }
    }
}
```

### Definition
- <span style='color:#FFD13E'>**URL**: /definition/</span>
- **Description**: Create definition
- **Method**: POST
---
- <span style='color:#FFD13E'>**URL**: /definition/<str:id>/</span>
- **Description**: Update an exisitng definition
- **Method**: PUT
- **Note**: <span style='color:#FFD13E'>To update the data, you need to send the complete payload with updated field values that need to be updated and leave the rest as it is for that particular entry. </span>

#### Request Body
```json
{
    "name": "defination 1",
    "detail": "some details",
    "deftarget": {
            "All": {
                "All": {
                    "win": {
                        "192.168.1.1": ["All"],
                        "192.168.1.2": ["All"]
                    },
                    "linux": {
                        "192.168.1.3": ["All"],
                        "192.168.1.4": ["All"]
                    }
                }
            }
        }
}
```