import nox


@nox.session
def tests(session):
    session.install("-r", "requirements_dev.txt")
    session.install(".")
    session.run("pytest")
