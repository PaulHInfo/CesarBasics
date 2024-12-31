def caesar_cipher(message: str, key: str) -> str:
    """
    """

    shift = 0
    for letter in key.lower():
        if letter.isalpha():
            shift += ord(letter) - ord('a')
    shift %= 26

    resultat = []
    for char in message:
        if char.isalpha():
            # Distinction majuscule / minuscule
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            resultat.append(new_char)
        else:
            resultat.append(char)

    return "".join(resultat)


# ------------------------------------------------------------------


if __name__ == "__main__":
    texte = "Bonjour"
    cle = "ABC"  # addition (A=0, B=1, C=2) => 0+1+2 = 3
    texte_chiffre = caesar_cipher(texte, cle)
    print("Texte original :", texte)
    print("Clé :", cle)
    print("Texte chiffré :", texte_chiffre)
