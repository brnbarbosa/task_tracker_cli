# TaskTrackerCli

A simple Command Line Interface (CLI) application for tracking tasks, built with Python, Typer, and Rich.

## Features

*   Add new tasks.
*   List existing tasks in a formatted table.
*   (Future) Mark tasks as complete.
*   (Future) Remove tasks.
*   Clean and colorful CLI output using Rich.

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd TaskTrackerCli
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Make sure you have a `requirements.txt` file with the following content:
    ```txt
    typer[all]>=0.9.0,<1.0.0
    rich>=13.0.0,<14.0.0
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` yet, you can install directly: `pip install "typer[all]" rich`)*

## Usage

The application is run from the command line using `python task_tracker.py`.

*(Note: The following examples assume future development based on the project goal. The current code might differ.)*

**Add a new task:**

```bash
python task_tracker.py add "Write the README file" --priority high
