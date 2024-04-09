# Development Environment

Clone this repo and install the development dependencies:

```bash
make install
```

This will create a virtual environment in the `.venv` directory at the repository root. You may need to configure your IDE to point to the newly created virtual environment after it has been created.

Run `make help` for list of available tasks.

Start local containerized instances of infrastructure dependencies (requires `docker`) with:

```bash
make infra
```

Run static analysis tools to check formatting, linting, and types with:

```bash
make check
```

Run tests against local infrastructure with:

```bash
make test
```

Start a local development server with:

```bash
make start-dev
```

You can then access the OpenAPI reference page at: [127.0.0.1:8000/schema](http://127.0.0.1:8000/schema)

Stop any running containers and remove development artifacts with:

```bash
make clean
```
