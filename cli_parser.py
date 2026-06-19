import argparse

parser = argparse.ArgumentParser(description="Demo CLI parser with verbosity")
parser.add_argument("input", help="Path to the input file")
parser.add_argument("--verbose", action="store_true", help="Print more details")
parser.add_argument("--format", default="csv", help="Output format")

args = parser.parse_args()

print("Reading file:", args.input)
if args.verbose:
	print("Verbose mode is ON - now printing extra info...")
print(f"Output format: {args.format}")
