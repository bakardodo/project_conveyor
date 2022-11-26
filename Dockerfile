#dockerise the application with python
FROM python:3.9
COPY . .
RUN pip install -r requirements.txt

# RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver"]
EXPOSE 8000
