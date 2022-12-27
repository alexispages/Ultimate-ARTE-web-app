FROM python:3.10.9-slim-buster

# Setup workdir and venv
WORKDIR /python-docker
ENV VIRTUAL_ENV=/python-docker/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Run the app
COPY app.py .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]