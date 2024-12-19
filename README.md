# Math Service Project

This project provides two main API services:

1. **Difference Service**: Calculates the difference between the sum of the squares and the square of the sum for the first `n` natural numbers.
2. **Triplet Service**: Determines if a set of three numbers `(a, b, c)` form a Pythagorean triplet and calculates their product if true.

## Features

- API endpoints to handle difference calculations and Pythagorean triplet validation.
- Swagger UI for API documentation.
- Persistent logging of requests in the database.
---

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

Ensure the following tools are installed on your system:

- Python 3.10 or later
- Pip (Python package manager)
---

## Setup Instructions (for MacOs)

```bash
# create virtual env
python3 -m venv venv
# activate environment
source venv/bin/activate
# install dependencies
pip install -r requirements.txt
# start redis
brew services start redis
```


## Commands Summary

| Task                         | Command                                       |
|------------------------------|-----------------------------------------------|
| Create migrations            | `python manage.py makemigrations`            |
| Apply migrations             | `python manage.py migrate`                   |
| Create superuser             | `python manage.py createsuperuser`           |
| Run server                   | `python manage.py runserver`                 |
| Start Celery worker          | `celery -A math_service_project worker --loglevel=info` |
| Start Flower                 | `celery -A math_service_project flower`       |
| Run integration tests        | `python manage.py test`                      |
| Purge Celery queue           | `celery -A math_service_project purge`       |
| Check Celery worker status   | `celery -A math_service_project status`      |


## URLS
- Django app running on: [http://localhost:8000/](http://localhost:8000/)
- Django admin running on: [http://localhost:8000/admin](http://localhost:8000/admin)
- Swagger docs running on: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Flower UI for Celery running on: [http://localhost:5555/](http://localhost:5555/)


## Example Requests
```bash
GET http://localhost:8000/api/difference/?number=10
GET http://localhost:8000/api/triplet/?a=3&b=4&c=5
```