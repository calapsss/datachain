# Datachain 

## Description

Datachain is a comprehensive project that includes a Python package for backend operations and a Django application for the frontend. The backend provides classes and helper functions for interacting with a PostgreSQL database. The frontend is a boilerplate UI for the chatbot, 

## Backend
![Python package](https://github.com/username/repository/workflows/Python%20package/badge.svg)

The backend provides the following key features:

- Establishing a connection to a PostgreSQL database.
- Creating tables based on provided table names and CSV data.
- Executing SQL queries.
- Inserting data from CSV files into specified tables.
- Fetching data from tables.
- Deleting tables from the database.

## Frontend

The frontend is a Django application with the following views:

- `index`: Renders the main page.
- `database_tables`: Fetches and displays the list of tables in the database.
- `view_table`: Fetches and displays the data from a selected table.
- `query_page`: Allows users to execute SQL queries and view the results.

## Installation

`datachain_backend` already comes preinstalled as dependency on the frontend. If you want to install and use the package in your project:
1. Clone the repository: `git clone https://github.com/calapsss/datachain.git`
2. Navigate to `dist` directory: `cd datachain/datachain-backend/dist/datachain_backend-0.1.0-py3-none-any.whl`
3. You can install the package `pip install datachain_backend-0.1.0-py3-none-any.whl`

To check the how it works with `datachain_frontend`:
1. Clone the repository: `git clone https://github.com/calapsss/datachain.git`
2. Navigate to the project directory: `cd datachain\datachain-frontend`
3. Install the Python package dependencies using Poetry: `poetry install`
4. Run with Poetry: `poetry run python manage.py runserver 8080`
5. [Additional installation steps, if any]

## Usage

To use the project, follow these steps:

1. Start the Django Server: `poetry run python manage.py runserver 8080`
2. Visit `localhost:8000` in your web browser to view the application.

## Contributing

We welcome contributions from the community. To contribute to the project, please follow these guidelines:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your changes'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

This project is licensed under the MIT. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or questions, please contact the project maintainer at [charles@calapini.com](mailto:charles@calapini.com).

## TODO

### Features
- Chat handler function
- Internal code interpreter

### Maintainability
- Add unit tests for backend operations.
- Improve error handling in the frontend views.
- Implement user authentication and authorization.
- Refactor code for better modularity.
