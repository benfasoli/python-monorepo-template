from lib.core import hello_world
from lib.dtos import Message


def main() -> bytes:
    message = hello_world()
    dto = Message(1, message)
    return dto.to_json()


if __name__ == "__main__":
    main()
