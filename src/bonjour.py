"""Premier module du projet : une fonction que l'on peut tester."""


def dire_bonjour(nom: str) -> str:
    return f"Bonjour {nom}, bienvenue en MLOps !"


if __name__ == "__main__":
    print(dire_bonjour("monde"))
