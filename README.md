# Team Jurubetsu - Group 9 - IP Tracker

### Team Members:
- Aras, Juanito
- Baltazar, Zeus James
- Crebello, Cynna Mae
- Moreno, Wenzel

### Major Requirements:
- Git (Local Version Control)
- GitHub (Remote Version Control)
- Python (Programming Language)
- Pipenv (Packaging Tool with Virtual Environment)
- Django (Python Web Framework)
- HTML/CSS/JS (Web Page Fundamentals)
- Bootstrap (CSS Framework)

### Create a virtual environment
We are using pipenv packaging tool to manage dependencies and virtual environemnt. To activate the virtual environment, run the following command in the base directory of the repository project. Also, you can just run the **'shell'** script on the scripts folder depending on your operating system.
```python
pipenv shell
```

### Install package dependencies
No need to worry about manual installation of package dependencies because there is a provided pipfile. All you need to do is to run the following command in the base directory of the repository project. Also, you can just run the **'install'** script on the scripts folder depending on your operating system.
```python
pipenv install
```

### Run the main entry point of the program
You will always use this particular command in the development because it is the main entry point. Also, there are provided script files to run the web application, these are **'run_linux.sh'** and **'run_windows.bat'** depending on your operating system.
```python
python manage.py runserver
```