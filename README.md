# Engineering Design Course Website

This repository is part of the **Engineering Design** course in our first semester. It contains the source code for a website that acts as a connecting interface between guides and their respective guided individuals.

## How to Run This Project

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone [<repository-url>](https://github.com/sss2482/eg.git)
   cd eg
   ```
2. **Create a virtual enviroment**
   ```bash
   python -m venv <venv_name>
   ```
3. **Activate the virtual environment**
   ```bash
   <venv_name>\Scripts\activate   # For Windows
   source <venv_name>/bin/activate  # For macOS/Linux
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up the database**
   ```bash  
   py manage.py makemigrations
   py manage.py migrate
   ```

7. **Run the server**
   ```bash
   py manage.py runserver
   ```
