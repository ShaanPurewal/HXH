# Load env variables
import json
import os
import sys

from dotenv import load_dotenv

from profile import Profile
from bots.indeed import Indeed


# Setup loaded .env and creds
def setup():
    load_dotenv("./environments/creds.env")
    load_dotenv("./environments/bots.env")

    return [x.lower() for x in sys.argv][1:], [x.lower() for x in json.loads(os.getenv("BOTS"))]


# Command Line Interface
def cli():
    print("CLI ENABLED")

    while 1:
        cmd = input("~ ").lower()

        if cmd == "exit":
            return

        run_bot([cmd])


# Take job profile as user input
def capture_input():
    return Profile(
        title=input("Please enter a title: "),
        location=input("Please enter a location: "),
        salary=int(input("Please enter a salary: ")),
        description=input("Please enter a description: ")
    )


# Job bot controller
def run_bot(arguments: list[str]):
    for arg in arguments:
        if arg not in bots:
            print("\nERROR:")
            print(f"\tInvalid bot argument, skipped {arg}\n")
        else:
            profile = capture_input()
            match arg:
                case "indeed":
                    Indeed(profile)
                case _:
                    print(f"job not found for bot: {arg}")


# Main File
if __name__ == '__main__':
    args, bots = setup()

    if len(args) > 0 and 'cli' in args:
        cli()
    else:
        run_bot(args)

    print("~~ Program Complete ~~")
