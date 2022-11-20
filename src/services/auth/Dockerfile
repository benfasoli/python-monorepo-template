FROM python:latest

WORKDIR /src

# Download ssh public key for github.com
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

COPY . .
RUN --mount=type=ssh pip install .
