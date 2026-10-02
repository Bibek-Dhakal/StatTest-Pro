# Code Quality & Formatting

This project enforces code quality automatically via Git Hooks to ensure consistency and prevent broken builds.

**Important Note:** Code formatting, linting, and commit message validations run automatically on `git commit`. Manual fallback commands are provided below.

## Environment Setup

We use `pre-commit` to manage our git hooks and `ruff` for all Python linting/formatting.

```bash
# 1. Install dependencies
pip install -e .[dev]

# 2. Install Git hooks into your local repository
pre-commit install

# 3. Install commit-message hook (for Conventional Commits)
pre-commit install --hook-type commit-msg
```

## Manual Execution Commands

Run quality checks repository-wide on all files:
```bash
pre-commit run --all-files
```

Run checks ONLY on staged/modified files:
```bash
pre-commit run
```

Run only Ruff (Linting & Formatting) manually without pre-commit:
```bash
# Check formatting and linting
ruff check .
ruff format --check .

# Auto-fix linting and formatting
ruff check --fix .
ruff format .
```

## Maintenance & Cache

To update tools to their latest versions:
```bash
pre-commit autoupdate
```

To clear local tool caches if hooks are acting unreliably:
```bash
pre-commit clean
```

## Emergency Bypassing

If you absolutely must bypass hooks in an emergency (e.g., hotfix commit), use the `--no-verify` flag. **Use this responsibly.**
```bash
git commit -m "fix(core): hotfix critical issue" --no-verify
```
