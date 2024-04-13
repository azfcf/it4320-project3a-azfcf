#Use an official python runtime
FROM python:3.11

#Set the working directory
WORKDIR /app

#Copy the code base in the current directory to the container /app
COPY . /app

#Upgrade pip
RUN pip install --upgrade pip

#install needed packages
RUN pip install -r requirements.txt

#Set the default command to run when starting the container
CMD ["python", "Stock_Visualizer.py"]

