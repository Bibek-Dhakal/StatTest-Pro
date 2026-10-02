# Contributing to StatTest-Pro

First off, thank you for considering contributing to StatTest-Pro!

## 1. Commit Message Standard (Strictly Enforced)

This project strictly enforces **Conventional Commits** (`type(scope): message`). All automated versioning and `CHANGELOG.md` generation is driven by commit history using Google's `release-please`.

### Valid Commit Types
* `feat:` A new feature (correlates to a **minor** semantic version bump).
* `fix:` A bug fix (correlates to a **patch** semantic version bump).
* `feat!:` or `fix!:` A breaking change (correlates to a **major** semantic version bump).
* `docs:`, `chore:`, `style:`, `refactor:`, `test:`, `ci:` Non-release related changes.

Example:
```bash
git commit -m "feat(power): add capability to compute power for continuous metrics"
```

## 2. Release & Versioning Workflow

We use `release-please` via GitHub Actions:
1. When you push to `main`, `release-please` aggregates the commits and creates/updates a **Release PR**.
2. **DO NOT modify version tags or the CHANGELOG.md manually.**
3. When the Release PR is merged by a maintainer, `release-please` automatically tags the release, finalizes the CHANGELOG, and bumps the version.

## 3. Development Setup

1. Fork and clone the repository.
2. Install dependencies: `pip install -e .[dev]`
3. Install pre-commit hooks: `pre-commit install && pre-commit install --hook-type commit-msg`
4. Run tests before submitting a PR: `pytest`

## 4. Code Quality

All Python code is formatted and linted using `Ruff`. Ensure your code passes all checks by running `pre-commit run --all-files` before submitting.
