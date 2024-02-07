# Library Management System

This is a Library Management System built using Django, a high-level Python web framework. The system allows librarians to manage books, patrons, borrowing, and returning.

## Features

- **Book Management**: Add, edit, and delete books in the library inventory.
- **Patron Management**: Manage library patrons, including their registration and details.
- **Borrowing and Returning**: Allow patrons to borrow books and return them within the due date.
- **Admin Dashboard**: Provide an admin dashboard to manage system settings, view reports, and monitor activities.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd LibraryManagementSystem
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://localhost:8000/`.

## Usage

- Visit the admin dashboard at `http://localhost:8000/admin/` and log in with the superuser credentials.
- Use the admin interface to manage books, patrons, and borrowing records.
- Patrons can access the public-facing interface to search for books, view their borrowing history, and check availability.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
