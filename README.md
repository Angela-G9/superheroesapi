# Superheroes API

The Superheroes API is a Flask-based application that allows users to manage superheroes, their powers, and the relationships between them. It provides endpoints to create, read, update, and delete heroes, powers, and hero-power relationships.

## Features

- **Heroes Management**: Create, retrieve, update, and delete heroes.
- **Powers Management**: Create, retrieve, update, and delete powers.
- **Hero-Power Relationships**: Link heroes to powers with a strength attribute.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Superheroes
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Seed the database:
   ```bash
   python seed.py
   ```

## Usage

1. Run the application:
   ```bash
   flask run
   ```

2. Access the API at `http://127.0.0.1:5000`.

## API Endpoints

### Heroes

- **GET** `/api/heroes`: Retrieve all heroes.
- **GET** `/api/heroes/<id>`: Retrieve a specific hero by ID.
- **POST** `/api/heroes`: Create a new hero.
- **PATCH** `/heroes/<id>`: Update an existing hero.
- **DELETE** `/heroes/<id>`: Delete a hero.

### Powers

- **GET** `/api/powers`: Retrieve all powers.
- **GET** `/api/powers/<id>`: Retrieve a specific power by ID.
- **POST** `/api/powers`: Create a new power.
- **PATCH** `/api/powers/<id>`: Update an existing power.
- **DELETE** `/powers/<id>`: Delete a power.

### Hero-Powers

- **POST** `/api/hero_powers`: Link a hero to a power with a strength attribute.

## Models

### Hero

- `id`: Integer, primary key.
- `name`: String, required.
- `super_name`: String, required.

### Power

- `id`: Integer, primary key.
- `name`: String, required.
- `description`: String, required (minimum 20 characters).

### HeroPower

- `id`: Integer, primary key.
- `strength`: String, required (values: "Strong", "Weak", "Average").
- `hero_id`: Foreign key to `Hero`.
- `power_id`: Foreign key to `Power`.

## Validation

- **Power Description**: Must be at least 20 characters long. Returns an error if invalid.
- **HeroPower Strength**: Must be one of "Strong", "Weak", or "Average". Returns an error if invalid.

## Development

- **Run the app**: `python run.py`
- **Database migrations**: Use Flask-Migrate commands (`flask db migrate`, `flask db upgrade`).

## License

This project is licensed under the MIT License.