#Base
FROM python:3.13

#workdir
WORKDIR /app

#copy
COPY . /app

#run
RUN pip install -r requirements.txt

#port 
EXPOSE 5000

#command
CMD ["python", "./app.py"]