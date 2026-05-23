def dodawanie(a, b):
    return a + b


def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(10, 5) == 15
    assert dodawanie(-1, 1) == 0

if __name__ == "__main__":
    test_dodawanie()
    print("Wszystkie testy przeszły poprawnie!")