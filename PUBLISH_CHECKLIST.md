# Publish Checklist

## Done

- Rebranded the project to `Pulse`.
- Renamed the Django package to `pulse_project`.
- Removed cached Python artifacts from the working tree.
- Kept repository ignore rules for local environment files and databases.

## Still recommended before first public commit

- Review `README.md` and remove any business details you do not want public.
- Decide whether to keep the current contact address and Instagram references.
- Add screenshots if you want the repository to work as a portfolio piece.

## Still required before production

- Move `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` to environment-based settings.
- Replace SQLite with PostgreSQL for production deployments.
- Add real automated tests beyond the placeholder `home/tests.py`.
- Add CI for Django checks and Python compilation.
