
# UniSync

This project aims to automate the process of generating and managing class/semester schedules or timetables for students and teachers developed as part of my university coursework. It provides a convenient way to create schedules based on various constraints such as course availability, room availability, and teacher availability. The system also allows for easy modification and adjustment of schedules as needed.

## Prerequisites

- Python (version 3.10 or newer)
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/neon16bit/UniSync.git
    ```

2. Navigate to the project directory:

    ```bash
    cd UniSync
    ```

3. Create a virtual environment (recommended):

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        env\Scripts\activate
        ```

    - On Unix or macOS:

        ```bash
        source env/bin/activate
        ```

5. Install the project dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the project root directory and add your environment variables. For example:

    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

Replace `your_secret_key` with a new secret key generated using the Django `get_random_secret_key` function.

7. Run database migrations:

    ```bash
    python manage.py migrate
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be running at `http://127.0.0.1:8000/`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request
