# Blog API

This is a template for a Blog API project structure.

## Project Structure

```plaintext
blog-api/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── authors.py
│   │   ├── blogs.py
│   │   ├── categories.py
│   │   ├── tags.py
│   │   ├── users.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   ├── auth.py
│   │   └── security.py
│   ├── main.py
│   └── tests/
│       └── ... (test files)
├── Dockerfile
├── requirements.txt
└── README.md
```

## Usage

1. Clone this repository.
2. Navigate to the `blog-api` directory.
3. Set up your Python environment and install the required packages using `pip install -r requirements.txt`.
4. Run the application using `uvicorn app.main:app --reload`.
5. Access the API at `http://localhost:8000`.

## Docker

To run the application using Docker:

1. Build the Docker image: `docker build -t blog-api .`
2. Run the Docker container: `docker run -d --name blog-api -p 8000:8000 blog-api`

## API Endpoints

- `/api/authors`: CRUD operations for authors.
- `/api/blogs`: CRUD operations for blogs.
- `/api/categories`: CRUD operations for categories.
- `/api/tags`: CRUD operations for tags.
- `/api/users`: CRUD operations for users.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
