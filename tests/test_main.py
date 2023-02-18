from CookieCutter.main import hello_world


def test_main(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
