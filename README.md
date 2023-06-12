# mPharma demo app

A sample project to utilize internationally recognized set of diagnosis codes.

The app exposes a couple of  APIs for interacting with icd codes.

### Dependencies
1. Django, Python
2. Postgres
3. Redis
4. Docker
5. Docker hub

### Set application locallly for development
1. Navigate to a directory where you want to clone the repository.
2. Clone the repository using https
3. Change directory into the project.
4. Create a virtual environment
```shell
python3.10 -m venv venv
```
6. Activate the Python virtual environment
```shell
source venv/bin/activate
```
7. Install the project's development requirements
```shell
pip install -r requirements/dev.txt
```

### Run tests
```shell
pytest
```

### API Requirement
- GET /api/v1/diagnosis
- GET /api/v1/diagnosis/123
- POST /api/v1/diagnosis
- DELETE /api/v1/diagnosis/123
- GET /api/v1/upload-csv

### Architectural considerations
1. Since the applications has More READs than WRITEs:
    1. A caching layer (Redis) is introduced in between the application layer and the database layer.
    2. Frequently accessed data is cached to enhance low latency responses.

### To start the applications
1. To run the applications make sure you have docker and docker-compose installed on your local machine
2. Run the following command:
```shell
docker-compose up
```