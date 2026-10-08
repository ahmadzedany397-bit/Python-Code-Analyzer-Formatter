# 🐍 Python Code Analyzer & Formatter

A lightweight, interactive web application that acts as a real-time linter, formatter, and complexity analyzer for Python code. Built entirely in Python, this tool instantly restructures messy code to strict PEP-8 standards while mathematically grading the complexity of its underlying logic.

**[View the Live Web App Here](https://ahmadzedany397-bit-python-code-analyzer-formatter-main-hhpwb7.streamlit.app/)**

## Features

- **Instant PEP-8 Formatting:** Integrates the Uncompromising Code Formatter (`black`) to automatically clean up indentation, spacing, and line breaks.
- **Cyclomatic Complexity Grading:** Uses `radon` to evaluate the execution paths of user-defined functions and classes, outputting an objective complexity score.
- **Resilient Error Handling:** Gracefully catches invalid syntax, plain text inputs, and edge-case scripts without breaking the application state.
- **Responsive UI:** Built with Streamlit for a clean, intuitive two-column layout that updates instantly upon execution.

## Tech Stack

- **Language:** Python 3
- **Frontend & Routing:** Streamlit
- **Formatting Engine:** Black
- **Complexity Engine:** Radon

## How to Run Locally

1. **Clone the repository** and navigate into the project directory:

   ```bash
   git clone git clone https://github.com/ahmadzedany397-bit/Python-Code-Analyzer-Formatter.git
   cd python-code-analyzer
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv venv

   # Mac/Linux:
   source venv/bin/activate

   # Windows:
   venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**

   ```bash
   streamlit run main.py
   ```
