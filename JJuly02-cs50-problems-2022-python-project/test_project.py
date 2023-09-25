import pytest
from check import check
from generator import p_gen
from hasher import hashe

def main():
    test_checker()
    test_generator()
    test_hasher()

def test_checker(capsys):

    check("password", 1_000_000_000)
    captured = capsys.readouterr()
    assert "Your password is very common, change it immediately!" in captured.out

    check("PaSSword", 1_000_000_000)
    captured = capsys.readouterr()
    assert "Your password is very common, change it immediately!" in captured.out

    check("CSwe2@fWSwadsw", 1_000_000_000)
    captured = capsys.readouterr()
    assert "Your password has digits, lowercase, uppercase, and special characters!" and "This means your password is indeed very secure!" in captured.out


    check("CSwe2@fWSwadsw23f2u9wWsweifhjwWWWf9e2jwd92ol2WWEw<Wqwf11aX", 1_000_000_000)
    captured = capsys.readouterr()
    assert "Your password is inpenetrable!" in captured.out


def test_generator(capsys):

    p_gen(1, 8)
    captured = capsys.readouterr()
    assert "This means your password is low security :(" in captured.out

    p_gen(3, 8)
    captured = capsys.readouterr()
    assert "This means your password is low security :(" in captured.out

    p_gen(3, 20)
    captured = capsys.readouterr()
    assert "This means your password is indeed very secure!" in captured.out


    p_gen(3, 30)
    captured = capsys.readouterr()
    assert "Your password is inpenetrable!" in captured.out

def test_hasher(capsys):

    hashe("Misiek", "md5")
    captured = capsys.readouterr()
    assert "6cec5f8255209853c5f8340302590b1c" in captured.out

    hashe("Cs50", "sha1")
    captured = capsys.readouterr()
    assert "610781cf078bbefccb8f3122204d43e918d22918" in captured.out

    hashe("Harvard", "sha256")
    captured = capsys.readouterr()
    assert "fef9dcd64817f95c8f107588be201136ac8ef2d67f99ae83dae86941e8a5568a" in captured.out



if __name__ == "__main__":
    main()