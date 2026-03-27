import argparse


def greet(name, loud=False):
    message = f"Привет, {name}!"
    if loud:
        message = message.upper()
    print(message)


parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("name", help="Имя пользователя")
parser.add_argument("--loud", action="store_true", help="Громкий режим")

args = parser.parse_args()
greet(args.name, args.loud)
