import subprocess, os, shutil, sys
from settings import *

STEPS = """
- get input
- create folder (project name)
- create the following empty files
- create backend project folder (django-admin startproject backend)
- create empty files in backend folder (.gitignore, packages.txt)
- create app "base"
- update backend's .gitignore
- setup basic urls
- create frontend project folder (npx create-vite@latest frontend --template react)
- install tailwind
- setup tailwind
- remove bloatware from frontend like CSS files
- git init
- open vscodes
- delete __pycache__ created from this script
"""

def replace_file_contents(filepath, lines):
    try:
        with open(filepath, "w") as file:
            for line in lines:
                file.write(line + "\n")
        return True
    except Exception as e:
        print(e)
        return False

def run_cmd(cwd, cmd, shell):
    result = subprocess.run(
        cmd, cwd=cwd,
        shell=shell,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(result.stderr)
        return False
    return True

def run_cmds(cwd, cmds, shell):
    for cmd in cmds:
        if not run_cmd(cwd, cmd, shell):
            return False
    return True

def create_fullstack_project(PROJECT_NAME):
    global TAKE_INPUT, OVERRIDE_EXISTING_PROJECT_FILENAME, DJANGO_PROJECT_NAME, DJANGO_APP_NAME, GIT_COMMIT_NAME, REACT_PROJECT_NAME, PROJECT_URLS_PY_LINES, APP_URLS_PY_LINES, APP_VIEWS_PY_LINES, DJANGO_PACKAGES_LINES, VITE_CONFIG_JS_LINES, INDEX_HTML_LINES, APP_JSX_LINES, MAIN_JSX_LINES

    # get input
    if TAKE_INPUT:
        DJANGO_PROJECT_NAME = input("django project name: ")
        DJANGO_APP_NAME = input("django app name: ")
        REACT_PROJECT_NAME = input("react project name: ")
        GIT_COMMIT_NAME = input("git commit name: ")

    # create folder (project name)
    try:
        os.mkdir(PROJECT_NAME)
    except FileExistsError:
        if TAKE_INPUT:
            print(f"A folder with the name {PROJECT_NAME} already exists.")
            OVERRIDE_EXISTING_PROJECT_FILENAME = input("Do you want to override? (y/n)")[0].lower() == "y"
        if OVERRIDE_EXISTING_PROJECT_FILENAME:
            shutil.rmtree(PROJECT_NAME)
            os.mkdir(PROJECT_NAME)
        else: return print(f"A folder with the name {PROJECT_NAME} already exists")

    # create the following empty files
    empty_files = ["Implementation (Incomplete).png", "README.md"]
    for filename in empty_files:
        filepath = os.path.join(PROJECT_NAME, filename)
        with open(filepath, "w"): pass

    # create backend project folder (django-admin startproject backend)
    apps_dir = os.path.join(PROJECT_NAME, "apps")
    os.makedirs(apps_dir)
    if not run_cmd(
        cwd=apps_dir, shell=False,
        cmd=["django-admin", "startproject", DJANGO_PROJECT_NAME],
    ): return
    print(f"backend project \"{DJANGO_PROJECT_NAME}\" initialized")

    # create empty files in backend folder (.gitignore, packages.txt)
    empty_files = [".gitignore", "packages.txt"]
    for filename in empty_files:
        filepath = os.path.join(PROJECT_NAME, "apps", "backend", filename)
        with open(filepath, "w"): pass

    # create app "base"
    if not run_cmd(
        cwd=os.path.join(PROJECT_NAME, "apps", "backend"),
        cmd=["python", "manage.py", "startapp", DJANGO_APP_NAME],
        shell=False,
    ): return
    print(f"backend app \"{DJANGO_APP_NAME}\" initialized")

    # update backend's .gitignore
    if not replace_file_contents(
        filepath=os.path.join(PROJECT_NAME, "apps", "backend", ".gitignore"),
        lines=[
            f"db.sqlite3",
            f"backend/__pycache__",
            f"{DJANGO_APP_NAME}/migrations",
            f"{DJANGO_APP_NAME}/__pycache__",
        ]
    ): return
    print(f"backend gitignore initialized")

    # setup basic urls
    settings_path = os.path.join(PROJECT_NAME, "apps", "backend", "backend", "settings.py")
    with open(settings_path, "r") as file:
        lines = file.readlines()
    new_lines = []
    inside_installed_apps = False
    app_name_in_installed_apps = False
    for line in lines:

        if app_name_in_installed_apps:
            new_lines.append(line)
            continue
        
        stripped = line.strip()
        if stripped.startswith("INSTALLED_APPS"):
            inside_installed_apps = True
        
        if inside_installed_apps and stripped == "]" and not app_name_in_installed_apps:
            new_lines.append(f"\n    \"{DJANGO_APP_NAME}\",\n")
            app_name_in_installed_apps = True
        new_lines.append(line)
        
    with open(settings_path, "w") as file:
        file.writelines(new_lines)
    
    backend_dir = os.path.join(PROJECT_NAME, "apps", DJANGO_PROJECT_NAME)
    for file in [
        [os.path.join(backend_dir, DJANGO_PROJECT_NAME, "urls.py"), PROJECT_URLS_PY_LINES],
        [os.path.join(backend_dir, DJANGO_APP_NAME, "urls.py"), APP_URLS_PY_LINES],
        [os.path.join(backend_dir, DJANGO_APP_NAME, "views.py"), APP_VIEWS_PY_LINES],
        [os.path.join(backend_dir, "packages.txt"), DJANGO_PACKAGES_LINES],
    ]:
        if not replace_file_contents(filepath=file[0], lines=file[1]):
            return
    print(f"backend basic url setup completed")

    # create frontend project folder (npx create-vite@latest frontend --template react)
    if not run_cmd(
        cwd=os.path.join(PROJECT_NAME, "apps"),
        cmd=["npx", "create-vite@latest", REACT_PROJECT_NAME, "--template", "react"],
        shell=True,
    ) or not run_cmd(
        cwd=os.path.join(PROJECT_NAME, "apps", REACT_PROJECT_NAME),
        cmd=["npm", "install"],
        shell=True,
    ): return
    print(f"frontend project \"{REACT_PROJECT_NAME}\" initialized")

    # install tailwind
    if not run_cmd(
        cwd=os.path.join(PROJECT_NAME, "apps", REACT_PROJECT_NAME),
        cmd=["npm", "install", "tailwindcss", "@tailwindcss/vite"],
        shell=True,
    ): return

    # setup tailwind
    frontend_dir = os.path.join(PROJECT_NAME, "apps", REACT_PROJECT_NAME)
    for file in [
        [os.path.join(frontend_dir, "vite.config.js"), VITE_CONFIG_JS_LINES],
        [os.path.join(frontend_dir, "index.html"), INDEX_HTML_LINES],
        [os.path.join(frontend_dir, "src", "app.jsx"), APP_JSX_LINES],
        [os.path.join(frontend_dir, "src", "main.jsx"), MAIN_JSX_LINES],
    ]:
        if not replace_file_contents(filepath=file[0], lines=file[1]):
            return
    print(f"frontend tailwind installation and setup completed")

    # remove bloatware from frontend like CSS files
    frontend_dir = os.path.join(PROJECT_NAME, "apps", REACT_PROJECT_NAME)
    for path in [
        os.path.join(frontend_dir, "public"),
        os.path.join(frontend_dir, "src", "assets"),
        os.path.join(frontend_dir, "src", "App.css"),
        os.path.join(frontend_dir, "src", "index.css"),
    ]:
        try:
            if os.path.isfile(path): os.remove(path)
            if os.path.isdir(path): shutil.rmtree(path)
        except:
            print(f"could not delete bloatware file: {path}")
            return
    print(f"frontend bloatware removed")

    # git init
    if INITIALIZE_GIT:
        GIT_COMMIT_NAME = "\"" + GIT_COMMIT_NAME + "\""
        if not run_cmds(
            cwd=PROJECT_NAME, shell=False,
            cmds=[
                ["git", "init"],
                ["git", "add", "."],
                ["git", "commit", "-m", GIT_COMMIT_NAME],
            ]
        ): return
        print(f"git initialized")

    # open vscodes
    backend_dir = os.path.join(PROJECT_NAME, "apps", DJANGO_PROJECT_NAME)
    frontend_dir = os.path.join(PROJECT_NAME, "apps", REACT_PROJECT_NAME)
    if OPEN_VSCODES:
        try:
            if not run_cmd(
                cwd=backend_dir, shell=False,
                cmd=["code", "."],
            ) or not run_cmd(
                cwd=frontend_dir, shell=False,
                cmd=["code", "."],
            ): return
        except Exception as e:
            print(f"couldnt open vscode: {e}")

    # delete __pycache__ created from this script
    if os.path.isdir("__pycache__"): shutil.rmtree("__pycache__")

    # print next steps for user
    print(f"""
\033[92m========================================\033[0m
\033[92mFullstack project \"{PROJECT_NAME}\" initialized successfully!\033[0m
\033[93m👉 NEXT STEPS:\033[0m

\033[94mbackend (django):\033[0m
cd {PROJECT_NAME}/apps/backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

\033[94mfrontend (react):\033[0m
cd {PROJECT_NAME}/apps/frontend
npm run dev

\033[94mgit (optional if pushing to github):\033[0m
cd {PROJECT_NAME}
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push origin main

\033[92mHappy coding!\033[0m
    """)

if __name__ == "__main__":
    PROJECT_NAME = sys.argv[1] if len(sys.argv) > 1 else input("project name: ")
    create_fullstack_project(PROJECT_NAME)

