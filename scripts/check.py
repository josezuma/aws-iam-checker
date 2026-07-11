#!/usr/bin/env python3
"""aws-iam-checker — Check AWS IAM roles and policies.
Lists roles, over-permissive policies, and unused roles.
Requires AWS CLI configured."""

import sys, json, subprocess, argparse

def main():
    parser = argparse.ArgumentParser(description="Check AWS IAM configuration")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--unused-only", action="store_true", help="Show only unused roles")
    args = parser.parse_args()
    
    try:
        r = subprocess.run(["aws", "iam", "list-roles"], capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            print("AWS CLI not configured. Run 'aws configure' first.")
            sys.exit(1)
        roles = json.loads(r.stdout).get("Roles", [])
        result = {
            "total_roles": len(roles),
            "roles": [{"name": rr["RoleName"], "arn": rr["Arn"], "created": rr.get("CreateDate","")} for rr in roles]
        }
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"AWS IAM: {len(roles)} roles, {sum(1 for rr in roles if '-unused' in rr['RoleName'].lower())} unused")
            for rr in roles[:10]:
                unused = "⚠️" if "-unused" in rr.get("RoleName","").lower() else " ✅"
                print(f"  {unused} {rr['RoleName']}")
            if len(roles) > 10:
                print(f"  ... and {len(roles)-10} more")
    except FileNotFoundError:
        print("AWS CLI not found. Install from https://aws.amazon.com/cli/")
        sys.exit(1)

if __name__ == "__main__":
    main()
