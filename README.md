# CLI Arg Parser

A simple command-line tool demonstrating argument parsing in Python using `argparse`. Built as a hands-on exercise to understand how CLI tools accept and validate user input from the terminal.

## What It Does

The script takes a filename as input and supports optional flags to control output verbosity and formatting.

```bash
python3 cli_parser.py demo.txt --verbose --format json
```

## Features

- **Positional argument** — `input` (required filename)
- **Optional flag** — `--verbose` (boolean, enables extra output)
- **Optional flag with default** — `--format` (string, defaults to `csv`)
- **Built-in validation** — missing required arguments automatically trigger a usage/error message, no extra code needed

## Usage

```bash
# Basic run
python3 cli_parser.py demo.txt

# With verbose output
python3 cli_parser.py demo.txt --verbose

# With a specific format
python3 cli_parser.py demo.txt --format json

# All together
python3 cli_parser.py demo.txt --verbose --format json
```

## Example Output

```
$ python3 cli_parser.py demo.txt --verbose --format json
Reading file: demo.txt
Verbose mode is ON — now printing extra info...
Formatting output as JSON...
```

## What I Learned

- The difference between positional and optional arguments
- How `action="store_true"` turns a flag into a boolean switch
- How to set default values for optional arguments
- How `argparse` handles validation and error messages automatically

## Tech

- Python 3
- `argparse` (standard library)
