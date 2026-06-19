import argparse

parser = argparse.ArgumentParser(description="Demo CLI parser with verbosity")
parser.add_argument("input", help="Path to the input file")
parser.add_argument("--verbose", action="store_true", help="Print more details")
parser.add_argument("--format", default="csv", help="Output format")

args = parser.parse_args()

print("Reading file:", args.input)
if args.verbose:
	print("Verbose mode is ON - now printing extra info...")

if args.format == "json":
	print("Formatting output as JSON...")
elif args.format == "csv":
	print("Formatting output as CSV...")
else:
	print(f"Unknown format '{args.format}', defaulting to plain text.")
