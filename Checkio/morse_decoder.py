# morse_decoder
# Created by JKChang
# 2019-08-22, 11:26
# Tag:
# Description: The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

# Input: The secret message.
#
# Output: The decrypted text.
# Precondition:
# 0 < len(message) < 100
# The message will consists of numbers and English letters only.

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    return ' '.join(
        ''.join(MORSE[char] for char in word.split())
        for word in code.strip().split('   ')
    ).capitalize()


if __name__ == '__main__':
    # print("Example:")
    # print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")