FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

# Create app directory
WORKDIR /app

# copy directory
COPY . /app/


#installing dependencies from file
RUN pip install -r requirements.txt


# EXPOSE 8080
# CMD [ "python", "server.py" ]