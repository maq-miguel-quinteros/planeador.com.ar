# Backend

## Setup

### Virtual environment

```shellscript
python -m venv env
env/Scripts/activate # source env/bin/activate in GitHub Codespaces
```

### Dependencies

Create `requirements.txt` with content:

```plaintext
asgiref
Django
django-cors-headers
djangorestframework
djangorestframework-simplejwt
PyJWT
pytz
sqlparse
psycopg2-binary
python-dotenv
```

Install libraries

```shellscript
pip install -r requirements.txt
o
pip install -r backend/requirements.txt # if pull project
```

### Git ignore

Create `.gitignore` file white content

```plaintext
env/
```

### Create project

```shellscript
django-admin startproject backend
```

## Settings

`setting.py` in `backend`

### Imports

```py3
# for token lifetime
from datetime import timedelta
# for environment variables
from dotenv import load_dotenv
import os

load_dotenv()
```

### Permissions

```py3
# any request
ALLOWED_HOSTS = ["*"]

# for JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# token lifetime
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

### Apps

```py3
INSTALLED_APPS = [
	#...    
    # django app
    'rest_framework',
    # para evitar errores de cors
    'corsheaders',
]
```

### Middleware

```py3
MIDDLEWARE = [
	#...
    # corsheaders middleware
    "corsheaders.middleware.CorsMiddleware",
]
```

### End of the file

```py3
# corsheaders config
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
```

### Git ignore

At `backend` create `.gitignore` file white content

```plaintext
.env
db.sqlite3
```

## Users app

### Create & config

```shellscript
cd backend
python manage.py startapp users # or api or same. Register & login users app
```

`settings.py` in `backend`

```py3
INSTALLED_APPS = [
    #...
    # register y login users app
    'users',
]
```

### Model

Use the `User` model from `django.contrib.auth.models`

### Serializer

At `users` create `serializers.py`

```py3
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    # redefine create function from ModelSerializer
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
```

### Views

At `users` create `views.py`

```py3

```
