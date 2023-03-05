from CookieCutter.main import hello_world


def test_main(benchmark, capsys):
    benchmark(hello_world)
    captured = capsys.readouterr()
    assert True
