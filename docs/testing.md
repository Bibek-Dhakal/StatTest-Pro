# 🧪 Testing Strategy

StatTest-Pro utilizes `pytest` to guarantee the engine's mathematical properties and structural invariants.

[← Back to Documentation Index](README.md)

## Testing Tiers
1. **Unit Tests**: Ensure individual calculation logic (`power.py`, `evaluator.py`) matches deterministic statistical expectations.
2. **Invariant Tests**: Ensure anomaly states (like Sample Ratio Mismatch) trigger `SRMError` exceptions appropriately and halt execution.

## Running Tests
```bash
# Run all tests
pytest

# Run tests with coverage output
pytest --cov=stattest_pro
```

## CI Integration
Tests are automatically executed on PR creation via GitHub Actions (configured in `.github/workflows/`) or pre-push hooks if enabled by the user locally.
