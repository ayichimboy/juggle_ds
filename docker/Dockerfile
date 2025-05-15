# step 1 for creating dockerfile
# docker is based on base image
FROM python:3.11-slim

# crate a directory in the docker file if doesn't exist, create one
WORKDIR /app  # similar to cd in python terminal

# copy files from the local host

COPY linear_reg.pkl .  
COPY requirements.txt .          
COPY linear_penguins.ipynb .
COPY app.py .

# COPY ["app.py", "linear_penguins.ipynb", "linear_reg.pkl", "requirements.txt", "./"]

# copy the files from the local folder to the docker containter
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt 

# copy all the files from the host machine into the docker image
# first dot. from your local machine dot dot is to the docker image ( in the WORKDIR)
COPY . . 

EXPOSE 5000

# execute the container 
CMD ["python","app.py"]


# what's next 
# build docker image using 
# docker build -t name_file .
# docker run -p 5000:5000 name_file