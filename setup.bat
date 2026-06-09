@echo off
REM POS System Setup Script for Windows
REM This script helps you set up the POS System application on Windows

echo.
echo ================================
echo POS System - Setup Script
echo ================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version > nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python %PYTHON_VERSION% found
echo.

REM Create virtual environment
echo [2/5] Setting up virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel > nul 2>&1
pip install -r requirements.txt > nul 2>&1
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully
echo.

REM Run migrations
echo [4/5] Setting up database...
python manage.py makemigrations > nul 2>&1
python manage.py migrate > nul 2>&1
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)
echo Database migrations completed
echo.

REM Create superuser
echo [5/5] Creating admin user...
echo To create a superuser account, run:
echo   python manage.py createsuperuser
echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Then access the application at:
echo   http://localhost:8000
echo.
echo Admin panel:
echo   http://localhost:8000/admin
echo.
pause
