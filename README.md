# Fullstack Project Initializer

This is a Python-based CLI tool to instantly generate a clean and organized Fullstack project with:<br>
✅ Backend - Django<br>
✅ Frontend - React + TailwindCSS using Vite<br>
✅ Customizable folder structure and starter files<br>
✅ Git initialization<br>
✅ Optional VS Code launch<br>
<br>

## 🧠 What It Does

This script automates the tedious setup of a fullstack app by:<br>
- Taking a project name as an argument or input<br>
- Creating folders and initializing files<br>
- Bootstrapping a Django project with a base app<br>
- Setting up a basic API route and view<br>
- Creating a Vite + React frontend project<br>
- Installing and configuring TailwindCSS<br>
- Cleaning up unnecessary react files (bloatware)<br>
- Setting up Git and making an initial commit<br>
- Optionally launching backend and frontend in VS Code<br>
<br>

## 🚀 Usage

### Option 1: From Command Line
```bash
python -u script.py project_name
```

### Option 2: With Input Prompt
Enable `TAKE_INPUT = True` in `settings.py` to be prompted for:
- Django project name
- Django app name
- React project name
- Git commit name

### Option 3: Configuration in `settings.py`
Customize your project generation with:
```python
TAKE_INPUT = False
OVERRIDE_EXISTING_PROJECT_FILENAME = True
INITIALIZE_GIT = True
OPEN_VSCODES = True

DJANGO_PROJECT_NAME = "backend"
DJANGO_APP_NAME = "base"
REACT_PROJECT_NAME = "frontend"
GIT_COMMIT_NAME = "initial commit"
```
You can also customize:
- Django starter URLs & views
- Tailwind config
- Vite templates
- File contents

## 📁 Folder Structure

```powershell
project_name/
├── apps/
│   ├── backend/
│   │   ├── backend/
│   │   ├── base/
│   │   ├── .gitignore
│   │   └── packages.txt
│   └── frontend/
│       ├── public/
│       ├── src/
│       ├── index.html
│       └── vite.config.js
├── .git/
├── README.md
└── Implementation (Incomplete).png
```

