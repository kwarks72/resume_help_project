from resume_helper import chat_loop
from resume_agents import check_env


def main():
    check_env()
    chat_loop()


if __name__ == "__main__":
    main()
