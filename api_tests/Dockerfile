# Picks the pytho image
FROM python:latest

# Setup the working directory path
WORKDIR /Tests

#Copy all files including subfolder in /
COPY . /

#Install any python librarties in the python container
RUN pip install pytest
RUN pip install requests

#Execute the python tests with pytest
CMD ls
CMD [ "pytest" ]