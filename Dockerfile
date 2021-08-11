FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

# Create app directory
WORKDIR /app

# copy directory
COPY . /app/


#installing dependencies from file
# RUN pip install -r requirements.txt


EXPOSE 8008

# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     /py/bin/pip install -r requirements.txt && \
#     adduser --disabled-password --no-create-home app && \
#     chmod -R +x scripts

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x scripts

ENV PATH="scripts:/py/bin:$PATH"

USER app

# CMD [ "python", "server.py" ]

CMD ["run.sh"]