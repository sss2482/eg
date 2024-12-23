# Engineering Design Course Website

This repository is part of the **Engineering Design** course in our first semester. It contains the source code for a website that acts as a connecting interface between guides and their respective guided individuals.

## How to Run This Project

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Create a virtual enviroment**
   ```bash
   python -m venv <venv_name>
   
   # Activate the virtual environment
   <venv_name>\Scripts\activate   # For Windows
   source <venv_name>/bin/activate  # For macOS/Linux

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set up the database**
   py manage.py makemigrations
   py manage.py migrate

5. **Run the server**
   py manage.py runserver
   
