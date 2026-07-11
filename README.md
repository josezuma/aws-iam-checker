<div align=center>
  <h1>☁️ AWS IAM Checker</h1>
  <p><em>Check AWS IAM roles and policies from CLI. Lists roles, detects unused roles, over-permissive policies, and credential expiry. Requires AWS CLI configured.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a></p>
  <p><strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
git clone https://github.com/josezuma/aws-iam-checker.git
cd aws-iam-checker
python3 scripts/check.py
```

## Prerequisites

- AWS CLI installed and configured (`aws configure`)
- IAM read-only permissions

## Features

| Feature | Description |
|---------|-------------|
| **Role listing** | Lists all IAM roles with ARN and creation date |
| **Unused detection** | Flags roles with "-unused" in name or no recent activity |
| **JSON output** | Machine-readable for pipeline integration |
| **Zero deps** | Requires only AWS CLI + Python stdlib |

## Demo

```bash
$ python3 scripts/check.py

AWS IAM: 12 roles, 3 unused
  ✅ admin-role
  ✅ ec2-service-role
  ⚠️  legacy-unused-role
  ✅ lambda-execution-role
  ⚠️  old-test-role-unused
  ✅ read-only-role
  ...
```

## License

MIT © 2026 Jose Zuma
