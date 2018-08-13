morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : " "
}
sig_morze = {'.':'^_','-':'^^^_',' ':'____'}

def encode_morze(string):
    upstring = string.upper()
    morze_sig = ''
    for i in range(len(upstring)):
        if (ord(upstring[i]) == 32) or ((ord(upstring[i])>64)and(ord(upstring[i])<91)):
            if (ord(upstring[i]) == 32):
                morze_sig = morze_sig + sig_morze[' ']
            else:
                dig_sig  = ''
                for j in range(len(morse_code[upstring[i]])):
                    dig_sig = dig_sig + sig_morze[morse_code[upstring[i]][j]]
                morze_sig = morze_sig + dig_sig + '__'

    return morze_sig[:(len(morze_sig)-3)]
