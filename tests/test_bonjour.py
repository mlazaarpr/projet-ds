from bonjour import dire_bonjour


def test_dire_bonjour():
    assert dire_bonjour("Ada") == "Bonjour Ada, bienvenue en MLOps !"
