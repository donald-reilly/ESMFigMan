```markdown
# Security Policy

## Reporting a Vulnerability

We take the security of ESMManager seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to Donald.Reilly.Jr@outlook.com. 

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information in your report:
- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

## Security Update Process

When a security vulnerability is reported:
1. We will confirm receipt of your vulnerability report
2. We will investigate and validate the security issue
3. We will develop and test a fix
4. We will prepare a security advisory with details about the vulnerability
5. Once the fix is ready, we will:
   - Release a security patch
   - Notify users through GitHub Security Advisories
   - Credit the reporter (unless they wish to remain anonymous)

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Communication

- Security advisories will be published through GitHub Security Advisories
- Additional notifications may be posted in the repository's Discussions or Issues
- For critical vulnerabilities, we may reach out to maintainers of known dependent projects

## Bug Bounty Program

At this time, we do not operate a bug bounty program.

## Security Best Practices

We encourage all contributors to follow these security best practices:
- Keep all dependencies up to date
- Review code changes carefully
- Follow secure coding guidelines
- Enable 2FA on your GitHub account
- Sign your commits
