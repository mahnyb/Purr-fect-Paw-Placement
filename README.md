# Project Setup Instructions

Welcome to the PurrfectPawPlacement setup guide. Follow these steps to set up your development environment.

## Prerequisites

Ensure you have the following installed before you begin:

1. Python (version 3.10 or higher recommended)
2. pip (Python package manager)

## Install Dependencies

This project uses a virtual environment to manage dependencies.

## Setup the Project

a) For Linux or Windows Subsystem for Linux (WSL), use the provided shell script:
```
./start_project.sh
```
b) For Windows (PowerShell or CMD), use the provided batch script:
```
start_project.bat
```

## Running the Application

After running the setup script, the Django development server should start automatically. Access the application through your web browser at:
```
http://127.0.0.1:8000/registration/login
```

## Testing Users

- General User: EmirE, Password: root1234
- Shelter User: K1L2M3N4O5P, Password: root1234

## Additional Notes

The setup scripts will handle virtual environment creation, dependency installation, database migrations, and server startup.

## Troubleshooting

- **Permission Errors**: Ensure you have execution permissions for the scripts. For Linux/WSL, you might need to run:
  ```
  chmod +x start_project.sh
  ```
- **Dependency Issues**: Ensure all dependencies listed in `requirements.txt` are compatible with your Python version. Upgrade pip if necessary using:
  ```
  python -m pip install --upgrade pip
  ```
