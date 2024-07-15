import argparse
import os
import sys
import time

global_delay = 0.05

punctuation_marks = [
    ".",
    ",",
    "?",
    "!",
    ": ",
    ";",
]


def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def TypeWriter(text: str, delay: float = global_delay):
    # Loop over each char in string and print to terminal
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * 10 if char in punctuation_marks else delay)


def TypeWriter_vertical(text: str, delay: float = global_delay):
    # Split text into serperate lines
    lines = text.splitlines()

    # Find the longest line
    longest_line = max(lines, key=len)

    # Create blank lines to output to for each line of text
    out_lines = ['' for _ in lines]

    # Loop for the length of the longest line
    for char_count, _char in enumerate(longest_line):
        # Itterate over each line
        for line_count, line in enumerate(lines):
            # Append the next char to the out_line
            try:
                out_lines[line_count] += line[char_count]
            # If end of string, append blank space
            except IndexError:
                out_lines[line_count] += ""
        
        # Move the cursor up to the start of the output if not first column
        if char_count > 0:
            sys.stdout.write(f"\033[{len(lines)}A") # \033 indicates ASCII escape character, [A move cursor up by a specificed number of lines

        # Print outlines
        for line in out_lines:
            sys.stdout.write(f"{line}\n")
        sys.stdout.flush()
        time.sleep(delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outputs the contents of a file like a typewriter.")

    parser.add_argument("data", type=str, nargs="?", help="The filepath to read or string to type")
    parser.add_argument("-d", "--delay", type=float, dest="delay", metavar="seconds", default=global_delay, help="The delay between printing characters")
    parser.add_argument("-v", "--vertical", dest="vertical", action="store_true", help="Whether to print vertically")
    parser.add_argument("-c", "--clear", dest="clear", action="store_true", help="If screen should be cleared before printing")
    args = parser.parse_args()

    # Should clear screen before outputting?
    if args.clear:
        ClearScreen()

    # If no data was specifed run the intro
    if not args.data:
        intro_text = r"""
          ______                    _       __     _ __           
         /_  __/_  ______  ___     | |     / /____(_) /____  _____
          / / / / / / __ \/ _ \    | | /| / / ___/ / __/ _ \/ ___/
         / / / /_/ / /_/ /  __/    | |/ |/ / /  / / /_/  __/ /    
        /_/  \__  /  ___/\___/     |__/|__/_/  /_/\__/\___/_/     
            /____/_/            

        A script by: Anno!           
        https://github.com/Sir-Anno                      
        """

        TypeWriter_vertical(intro_text)

    else:
        data = "" # File path or string to use

        # See if positional argument is a file path
        if os.path.isfile(args.data):
            # Parse file into string
            with open(args.data) as file:
                data = f"{file.read()}"
        else:
            data = args.data

        # Print vertical?
        if not args.vertical:
            TypeWriter(data, args.delay)
        else:
            TypeWriter_vertical(data, args.delay)
