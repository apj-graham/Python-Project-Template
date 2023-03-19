import nox


@nox.session
def tests(session):
    session.install("-r", "requirements_dev.txt")
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("pytest", "-v", "--benchmark-skip", "tests")


@nox.session
def coverage(session):
    session.install("-r", "requirements_dev.txt")
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("pytest", "-cov={{cookiecutter.project_slug}}", "tests/")


@nox.session
def mypy(session):
    session.install("-r", "requirements_dev.txt")
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("mypy", "CookieCutter")


@nox.session
def benchmark(session):
    session.install("-r", "requirements_dev.txt")
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("pytest", "--benchmark-only", "tests")


@nox.session
def auto_format(session):
    session.install("black")
    session.install("isort")
    session.install("ruff")

    session.run("black", ".")

    session.run("isort", "--atomic", ".")

    session.run("ruff", "check", "--fix", ".")
