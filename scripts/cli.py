#!/usr/bin/env python3
"""aws-iam-checker — CLI for aws iam checker."""

import sys, json, argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Aws Iam Checker")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    
    result = {
        "tool": "aws-iam-checker",
        "description": "Aws Iam Checker",
        "version": "1.0.0",
        "author": "Jose Zuma",
        "timestamp": datetime.utcnow().isoformat(),
    }
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['tool']} v{result['version']}")
        print(f"{result['description']}")
        print(f"Run with --help for options")


if __name__ == "__main__":
    main()
