# Contributing

Thanks for contributing to `pulse-site`.

## Development flow

- Create a branch from `main`.
- Keep changes small and reviewable.
- Update documentation when user-facing behavior changes.
- Do not commit `.env`, local databases, or generated caches.

## Local validation

Run a basic syntax check before opening a pull request:

```bash
python -m compileall pulse_project home
```

If you change dependencies or settings, verify the Django app still starts:

```bash
pip install -r requirements.txt
python manage.py check
```

## Pull requests

- Explain the functional change clearly.
- Mention any deployment or environment variable impact.
- Keep secrets, local paths, and machine-specific files out of the diff.
