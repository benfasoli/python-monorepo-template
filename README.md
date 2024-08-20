This **python monorepo template** is for large codebases comprised of multiple python packages (application layer logic, infrastructure facades, data (de)serialization, observability, etc.) and services (HTTP APIs, data platform workers).

## Highlights

- Bleeding edge python tools for dependency management with [`uv` workspaces](https://docs.astral.sh/uv/concepts/workspaces/) and static analysis with [`ruff`](https://docs.astral.sh/ruff/)
- Strong typing with [`pyright`](https://microsoft.github.io/pyright/#/)
- Single virtual environment with editable package installs during development
- Minimized service dependencies at runtime
- Path-based package resolution for editable installs, discoverability, and drift safety. Opt-in for multi-version artifact-based package distributions.

## Layout

```
├──  db  # sql migration scripts
├──  packages  # core functionality grouped in python packages
│   ├──  lib-core  # lib.core namespace package
│   │   ├──  lib
│   │   │   └──  core
│   │   ├── 󰙨 tests
│   │   └──  pyproject.toml  # package metadata and dependencies
│   └──  lib-dtos
├──  services  # application entrypoints and orchestration logic grouped by context
│   ├── 󰒍 api
│   │   ├── 󱧼 src  # src layout for tool discovery and import compatibility
│   │   │   └── 󰒍 api
│   │   ├── 󰙨 tests
│   │   ├──  Dockerfile
│   │   └──  pyproject.toml  # service metadata and dependencies
│   └──  worker
├──  compose.yaml  # build specs for services and infra dependencies
├──  Makefile  # development environment task runner, see dedicated section
├──  pyproject.toml  # workspace metadata and global tool configs
└──  uv.lock  # cross-platform dependency lock file
```

## Development environment

Create a new repo from this template and clone the repo.

- `make install` will create a virtual environment at `.venv`, resolve runtime + development dependencies defined in `packages/*/pyproject.toml` and `services/*/pyproject.toml` updating `uv.lock` if necessary, and install the runtime + development dependencies.

  ```
  > make install

  Resolved 32 packages in 6ms
  Prepared 27 packages in 3ms
  Installed 31 packages in 22ms
  + annotated-types==0.7.0
  + anyio==4.4.0
  + api==0.0.0 (from file:///Users/benfasoli/repos/monorepo/services/api)
  + certifi==2024.7.4
  ...
  ```

- `make lint` will check the code for compatibility with formatting, linting, and type checking requirement. `make format` will fix most formatting issues.

  ```
  > make lint

  14 files already formatted
  All checks passed!
  0 errors, 0 warnings, 0 informations
  ```

- `make infra` will start local infra in docker containers.

  ```
  > make infra

  ✔ Container monorepo-db-1  Created                                                                                                              0.0s
  Attaching to db-1
  db-1  | The files belonging to this database system will be owned by user "postgres".
  db-1  | This user must also own the server process.
  ```

- `make test` will run pytest across all packages and services. Requires running `make infra` in a separate shell to monitor infra logs.

  ```
  > make test

  ---------- coverage: platform darwin, python 3.12.5-final-0 ----------
  Name                                     Stmts   Miss  Cover   Missing
  ----------------------------------------------------------------------
  packages/lib-core/lib/core/__init__.py       2      0   100%
  packages/lib-core/lib/core/hello.py          2      0   100%
  packages/lib-core/tests/test_core.py         9      0   100%
  packages/lib-dtos/lib/dtos/__init__.py       2      0   100%
  packages/lib-dtos/lib/dtos/message.py        4      0   100%
  packages/lib-dtos/tests/test_dtos.py         7      0   100%
  services/api/src/api/__init__.py             0      0   100%
  services/api/src/api/main.py                10      0   100%
  services/api/tests/test_main.py             12      0   100%
  services/worker/src/worker/__init__.py       0      0   100%
  services/worker/src/worker/main.py           5      0   100%
  services/worker/src/worker/queue.py          7      0   100%
  services/worker/tests/test_main.py           8      0   100%
  ----------------------------------------------------------------------
  TOTAL                                       68      0   100%


  ========================= 6 passed in 1.19s ==========================
  ```

- `make build` will build deployable docker images for all services.

  ```
  > make build

  [+] Building 2.8s (18/18) FINISHED                                                                         docker:desktop-linux
  => [api internal] load build definition from Dockerfile                                                                   0.0s
  => => transferring dockerfile: 623B                                                                                       0.0s
  => [worker internal] load metadata for ghcr.io/astral-sh/uv:0.2.37                                                        0.8s
  => [worker internal] load metadata for docker.io/library/python:3.12-slim-bookworm                                        0.8s
  => [worker internal] load build definition from Dockerfile                                                                0.0s
  => => transferring dockerfile: 717B                                                                                       0.0s
  => [worker internal] load .dockerignore                                                                                   0.0s
  => => transferring context: 265B                                                                                          0.0s
  => [api internal] load .dockerignore                                                                                      0.0s
  => => transferring context: 265B                                                                                          0.0s
  ...
  ```

- `make dev` will `make build` then start both local infra and local service docker containers, forwarding ports to the host system.

  ```
  > make dev

  ✔ Container monorepo-db-1      Created                                                                                    0.0s
  ✔ Container monorepo-worker-1  Created                                                                                    0.0s
  ✔ Container monorepo-api-1     Created                                                                                    0.0s
  ...
  ```

- `make clean` will remove all temporary development files (`.venv`, caches, coverage reports, etc.) from the source tree.

- `make help` will print all available options

  ```
  > make help

  Usage: make <COMMAND>

  Commands:

    help         Show available options.
    build        Build docker image for each service
    dev          Build and run each service in a local docker container
    clean        Remove development artifacts
    install      Install dependencies in .venv and refresh lockfile
    infra        Start local development infra in docker containers
    format       Format code overwriting if necessary
    lint         Run static analysis checks for all packages and services
    test         Run tests for all packages and services
  ```
