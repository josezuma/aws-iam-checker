# FAQ

## Do I need AWS credentials?
Yes. The tool wraps the AWS CLI, which must be configured with `aws configure`.

## What permissions does it need?
Minimum: `iam:ListRoles`. Add `iam:ListRolePolicies` for advanced checks.

## Can I use it in CI/CD?
Yes. Use `--json` for machine-readable output. Exit code 0 on success.

## Does it cost money?
No. AWS IAM ListRoles API is free.

## Why not just use AWS CLI directly?
This tool formats output, detects unused roles, and provides structured JSON for monitoring.
