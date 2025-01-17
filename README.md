# Todo API Server (Python Study)

This is a minimal implementation of a Todo API server built using Python without any frameworks.
The project demonstrate basic CRUD operation for a Todo list.

## 📂 Project Structure

```bash
.
├── server.py       # The main server implementation
├── todos.json      # Local JSON file for storing todos
├── venv/           # Virtual environment (optional)
└── README.md       # Project documentation
```

## 📋 Features

- **GET `/todos`**: Retrieve all todos.
- **POST `/todos`**: Add a new todo.
- **PUT `/todos/{id}`**: Update an existing todo by its ID.
- **DELETE `/todos/{id}`**: Delete a todo by its ID.

## 🛠️ Requirements

- Python 3.12.2 or higher

## 🚀 Getting Started

サーバーの起動

```bash
python server.py
```

ブラウザで <http://localhost:8080>にアクセス

## 🔧 API Usage

### 1. Get All Todos

- **Endpoint**: `GET /todos`
- **Description**: Fetches all the todos.
- **Example**:

  ```bash
  curl http://localhost:8080/todos
  ```

- **Response**:

  ```json
  []
  ```

### 2. Add a New Todo

- **Endpoint**: `POST /todos`
- **Description**: Adds a new todo item.
- **Example**:

  ```bash
  curl -X POST http://localhost:8080/todos \
      -H "Content-Type: application/json" \
      -d '{"title": "Learn Python", "completed": false}'
  ```

- **Response**:

  ```json
  {
    "title": "Learn Python",
    "completed": false,
    "id": 0
  }
  ```

## 🗂️ Notes

...

## 🌟 Future Improvements

...
