
morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                   '-..': 'D', '.': 'E', '..-.': 'F',
                   '--.': 'G', '....': 'H', '..': 'I',
                   '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                   '...': 'S', '-': 'T', '..-': 'U',
                   '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '.----': '1',
                   '..---': '2', '...--': '3', '....-': '4',
                   '.....': '5', '-....': '6', '--...': '7',
                   '---..': '8', '----.': '9', '-----': '0',
                   '--..--': ', ', '.-.-.-': '.', '..--..': '?',
                   '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')',
                   '-.-.--': "!", '...---...': "SOS"}


def decodeMorse(morse_code):
    words = morse_code.strip().split("   ")
    decoded_word = []
    for word in words:
        decoded_word.append(" ")
        chars = word.split()
        decoded_char = [morse_code_dict[char.upper()] for char in chars]
        decoded_word.append("".join(decoded_char))
    return "".join(decoded_word).strip()


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
