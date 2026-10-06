PYTHON TO-DO LIST - WEBSITE VERSION
======================================

Requirements:
- Python 3.10+ recommended
- VS Code recommended

INSTALLATION
------------

1. Open this folder in VS Code.

2. Open Terminal.

3. Create a virtual environment:

   python -m venv venv

4. Activate it on Windows PowerShell:

   .\venv\Scripts\Activate.ps1

5. Install Flask:

   pip install -r requirements.txt

6. Start the website:

   python app.py

7. Open Chrome/Edge and visit:

   http://127.0.0.1:5000

FEATURES
--------
- Add tasks
- View tasks
- Complete/undo tasks
- Delete tasks
- Responsive website design

NOTE
----
Tasks are stored in memory while the Flask program is running.
They will reset when the application is stopped.
