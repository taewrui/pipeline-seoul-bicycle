# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pandas google-cloud-storage
COPY . /app
# 인증 파일 복사
COPY delta-discovery-405105-1010a9d46e53.json /app

# 환경 변수 설정
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json


CMD tail -f /dev/null
