FROM tiangolo/uvicorn-gunicorn-fastapi

COPY requirements.txt .
<<<<<<< HEAD

=======
>>>>>>> 69e5547c90f067ece325601f878c99b64debd886
RUN pip install -r requirements.txt

RUN mkdir -p app
COPY ./app app
<<<<<<< HEAD
EXPOSE 8080
=======

EXPOSE 8080

>>>>>>> 69e5547c90f067ece325601f878c99b64debd886
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
