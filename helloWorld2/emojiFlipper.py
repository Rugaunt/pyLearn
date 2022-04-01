def emoji_flipper(words):
    find_emoji = words.split(" ")
    emojis = {
        ":)": ":(",
        ":(": ":)",
        "O.o": "-.-"
    }

    output = ''
    for i in find_emoji:
        output += emojis.get(i, i) + " "

    return output


playerWords = input('> ')
print(emoji_flipper(playerWords))
