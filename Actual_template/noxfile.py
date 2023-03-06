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
    session.run("pytest", "-cov=CookieCutter", "tests/")


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
def bandit(session):
    session.install("-r", "requirements_dev.txt")
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("bandit", "CookieCutter/*")


@nox.session
def auto_format(session):
    session.install("black")
    session.install("isort")
    session.install("pylint")

    session.run("black", "CookieCutter")
    session.run("black", "tests")

    session.run("isort", "--atomic", "CookieCutter/.")
    session.run("isort", "--atomic", "tests/.")

    session.run("pylint", "CookieCutter")
    session.run("pylint", "tests")

