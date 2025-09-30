# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask web application with SQLite database integration. The application uses a simple MVC-like structure with routes in `app.py`, database operations in `database.py`, and Jinja2 templates in the `templates/` directory.

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
flask --app app run

# Run with debug mode
flask --app app run --debug
```

## Architecture

### Database Layer (`database.py`)
- **Data class**: Handles SQLite database operations using raw SQL queries
- Database file: `database.db` (SQLite)
- SQLAlchemy engine is initialized but not actively used for queries (uses raw sqlite3 instead)
- Current implementation uses `check_same_thread=False` for sqlite3 connection

### Application Layer (`app.py`)
- Main Flask application entry point
- Routes handle both HTML rendering and JSON API responses
- User input is escaped using `markupsafe.escape()` in form handlers
- Database instance (`data`) is created at module level and shared across requests

### Template Structure
- `base.html`: Base template for inheritance
- Form templates: `age.html`, `users.html`
- Content templates: `articles.html`, `blog.html`, `search.html`
- Error pages: `404.html`

## Key Routes

- `/` - Home page
- `/users` - Display all users (GET), add user form
- `/users/add` - Add new user (POST)
- `/articles` - Display articles list with hardcoded data
- `/age` - GET/POST form example
- `/api/ping` - JSON API endpoint
- `/search?q=` - Search endpoint (query parameter)

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT
)
```

## Important Notes

- The application uses a shared database connection across all requests (`check_same_thread=False`), which is not ideal for production
- SQLAlchemy is installed but only used for connection testing; main queries use raw sqlite3
- User input in forms is escaped but database queries use string formatting (potential SQL injection risk in `database.py:18`)