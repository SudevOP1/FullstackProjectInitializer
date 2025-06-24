TAKE_INPUT = False
OVERRIDE_EXISTING_PROJECT_FILENAME = True

INITIALIZE_GIT = True
GIT_COMMIT_NAME = "initial"
DJANGO_PROJECT_NAME = "backend"
DJANGO_APP_NAME = "base"
REACT_PROJECT_NAME = "frontend"
OPEN_VSCODES = False

PROJECT_URLS_PY_LINES = [
    "from django.contrib import admin",
    "from django.urls import path, include",
    "",
    "urlpatterns = [",
    "    path('admin/', admin.site.urls),",
    "    path('base/', include(\"base.urls\")),",
    "]",
    "",
]
APP_URLS_PY_LINES = [
    "from django.urls import path",
    "from . import views",
    "",
    "urlpatterns = [",
    "    path('hello/', views.hello, name=\"hello\"),",
    "]",
    "",
]
APP_VIEWS_PY_LINES = [
    "from django.http import JsonResponse",
    "",
    "def hello(request):",
    "    return JsonResponse({\"success\": True, \"message\": \"Hello\",})",
    "",
]
DJANGO_PACKAGES_LINES = [
    "django",
    "",
]
VITE_CONFIG_JS_LINES = [
    "import { defineConfig } from 'vite'",
    "import react from '@vitejs/plugin-react'",
    "import tailwindcss from '@tailwindcss/vite'",

    "// https://vite.dev/config/",
    "export default defineConfig({",
    "plugins: [",
    "  react(),",
    "  tailwindcss(),",
    "],",
    "})",
    "",
]
INDEX_HTML_LINES = [
    "<!doctype html>",
    "<html lang=\"en\">",
    "<head>",
    "  <meta charset=\"UTF-8\" />",
    "  <!-- <link rel=\"icon\" type=\"image/svg+xml\" href=\"/vite.svg\" /> -->",
    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />",
    "  <title>Vite + React</title>",
    "  <style>",
    "    @import \"tailwindcss\";",
    "  </style>",
    "</head>",
    "<body>",
    "  <div id=\"root\"></div>",
    "  <script type=\"module\" src=\"/src/main.jsx\"></script>",
    "</body>",
    "</html>",
    "",
]
APP_JSX_LINES = [
    "",
    "function App() {",
    "  return (",
    "    <h1 className=\"bg-yellow-500\">Hello</h1>",
    "  )",
    "}",
    "",
    "export default App",
    "",
]
MAIN_JSX_LINES = [
    "import { StrictMode } from 'react'",
    "import { createRoot } from 'react-dom/client'",
    "import App from './App.jsx'",
    "",
    "createRoot(document.getElementById('root')).render(",
    "  <StrictMode>",
    "    <App />",
    "  </StrictMode>,",
    ")",
    "",
]


