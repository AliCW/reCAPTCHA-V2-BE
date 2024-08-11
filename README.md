# reCAPTCHA-V2-BE

The backend is built using a very simple django setup to facilitate reCAPTCHA V2 checks with google. This program serves the very basic frontend (https://github.com/AliCW/reCAPTCHAv2-test-example).

## Setup...

Install python:

    sudo apt install python3

Create a virtual environment for your python backend to run in:

    python3 -m venv <path-to-backend-directory>

Clone the repo into virtual environment directory you just made:

    git clone https://github.com/AliCW/reCAPTCHA-V2-BE.git

Create a .env file in the api root directory & add your DJANGO SECRET_KEY

To run the server, navigate to the api/recaptchV2Test directory and type the below command to listen for post requests

    python3 manage.py runserver
