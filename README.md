# 🇷🇺 Goyda
**Rest assured that the hooks have passed, hearing loud af sound**
## Setup
### 1. Install and configure [pre-commit](https://pre-commit.com)
### 2. Add the following as the last hook in your `.pre-commit-config.yaml`
```yaml
  - repo: https://github.com/SteckCDev/goyda-pre-commit
    rev: v0.5
    hooks:
      - id: goyda
```
