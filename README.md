This **python monorepo template** is for large codebases comprised of multiple python libraries (core domain logic, infrastructure facades, data (de)serialization, observability, etc.) and applications (HTTP APIs, asynchronous event workers).

## Highlights

- Dependency management with [`uv` workspaces](https://docs.astral.sh/uv/concepts/workspaces/)
- Linting and formatting analysis with [`ruff`](https://docs.astral.sh/ruff/)
- Strong typing with [`pyright`](https://microsoft.github.io/pyright/#/)
- Path-based package resolution for editable installs, composability, and drift safety. Selectively opt-in to artifact-based package distribution.

## Layout

```
├── sql  # sql migration scripts
├── src  # python packages containing application logic and supporting libraries
│   ├── api
│   │   ├── src  # src layout for tool discovery and import compatibility
│   │   │   └── api
│   │   ├── tests
│   │   ├── Dockerfile
│   │   └── pyproject.toml  # service metadata and dependencies
│   └── worker
├── compose.yaml  # build specs for services and local infra dependencies
├── Makefile  # development environment task runner, see dedicated section
├── pyproject.toml  # workspace metadata and global tool configs
└── uv.lock  # cross-platform dependency lock file
```

## Development environment

Create a new repo from this template and clone the repo.

- `make install` will create a virtual environment at `.venv`, resolve runtime + development dependencies defined in `packages/*/pyproject.toml` and `services/*/pyproject.toml` updating `uv.lock` if necessary, and install the runtime + development dependencies.

  ```console
  $ make install

  Using CPython 3.13.2
  Creating virtual environment at: .venv
  Resolved 32 packages in 6ms
  Installed 31 packages in 119ms
  + annotated-types==0.7.0
  + anyio==4.8.0
  + api==0.0.0 (from file:///Users/benfasoli/repos/monorepo/src/api)
  + certifi==2025.1.31
  + click==8.1.8
  ...
  ```

- `make lint` will check the code for compatibility with formatting, linting, and type checking requirement. `make format` will fix most formatting issues.

  ```console
  $ make lint

  14 files already formatted
  All checks passed!
  0 errors, 0 warnings, 0 informations
  ```

- `make dev-infra` will start local infra in docker containers.

  ```console
  $ make dev-infra

  [+] Running 2/2
  ✔ Network monorepo_default  Created
  ✔ Container monorepo-db-1   Started
  ```

- `make test` will discover and run tests across all packages. Implicitly runs `make dev-infra`.

  ```console
  $ make test

  ---------- coverage: platform darwin, python 3.13.2-final-0 ----------
  Name                                Stmts   Miss  Cover   Missing
  -----------------------------------------------------------------
  src/api/src/api/__init__.py             0      0   100%
  src/api/src/api/main.py                12      0   100%
  src/api/tests/test_main.py             12      0   100%
  src/core/src/core/__init__.py           3      0   100%
  src/core/tests/test_core.py             9      0   100%
  src/dtos/src/dtos/__init__.py           2      0   100%
  src/dtos/src/dtos/message.py            4      0   100%
  src/dtos/tests/test_dtos.py             7      0   100%
  src/worker/src/worker/__init__.py       0      0   100%
  src/worker/src/worker/main.py           5      0   100%
  src/worker/src/worker/queue.py          7      0   100%
  src/worker/tests/test_main.py           8      0   100%
  -----------------------------------------------------------------
  TOTAL                                  69      0   100%

  ========================= 6 passed in 1.19s ==========================
  ```

- `make build` will build deployable docker images for all services.

  ```console
  $ make build

  ...
  ✔ api     Built
  ✔ worker  Built
  ```

- `make dev` will build and start local infra and local service docker containers, forwarding ports to the host system.

  ```console
  $ make dev

  ✔ Container monorepo-db-1 Created 0.0s
  ✔ Container monorepo-worker-1 Created 0.0s
  ✔ Container monorepo-api-1 Created 0.0s
  ...
  ```

- `make clean` will remove all temporary development files (`.venv`, caches, coverage reports, etc.) from the source tree.

- `make help` will print all available options

  ```console
  $ make help

  Usage: make <COMMAND>

  Commands:

    help         Show available options.
    build        Build docker image for each service
    dev          Build and run each service in a local docker container
    clean        Remove development artifacts
    install      Install dependencies in .venv and refresh lockfile
    infra        Start local development infra in docker containers
    format       Format code overwriting if necessary
    lint         Run static analysis checks for all libs and apps
    test         Run tests for all libs and apps
  ```
