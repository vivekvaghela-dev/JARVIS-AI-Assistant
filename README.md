# JARVIS AI Assistant 🤖

A Python-based AI assistant project designed to automate tasks and provide useful desktop utilities through different Python modules.

## ✨ Features

- 🧠 Memory management
- 🔎 Google search functionality
- 📂 File opening utilities
- 🖥️ Windows control and automation
- ⌨️ Keyboard and mouse control
- 📸 Screenshot functionality
- 🎵 Music tools
- 🌦️ Weather information
- 🛠️ AI-assisted code automation

## 🧰 Technologies Used

- Python
- JSON for local memory storage
- Python libraries listed in `requirements.txt`

## 📁 Project Structure

```text
JARVIS-AI-Assistant/
├── memory/
│   ├── __init__.py
│   └── jarvis_memory.py
├── agent.py
├── border.py
├── jarvis_auto_code.py
├── jarvis_file_open.py
├── jarvis_get_whether.py
├── jarvis_google_search.py
├── jarvis_music_tools.py
├── jarvis_prompts.py
├── jarvis_screenshot.py
├── jarvis_window_CTRL.py
├── keyboard_mouse_CTRL.py
├── memory_interceptor.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd JARVIS-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a local `.env` file using `.env.example` as a reference. Add the API keys required by your project.

**Never upload your `.env` file or private API keys to GitHub.**

### 6. Run the application

```bash
python agent.py
```

Check the project's actual entry point before running this command.

## 🔐 Security & Privacy

- Keep API keys and passwords private.
- Do not upload `.env` to GitHub.
- Keep `memory/memory_data.json` local if it contains personal or private data.
- Review permissions before enabling keyboard, mouse, or Windows automation features.

## ⚠️ Notes

- This project may be designed primarily for Windows.
- Some features may require additional configuration or API credentials.
- Make sure you understand the actions performed by automation modules before running them.

## 👨‍💻 Author

**Vivek Vaghela**

---

*Built with Python and a passion for AI-powered automation.*
