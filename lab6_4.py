sp_char = (',', '.', ':', ';', '!', '?', '-')
def find_most_frequent(string):
    word_list = []
    lstring = list(string)
    for i in range(1,len(lstring)):
        if sp_char.count(lstring[i-1]) == 1:
            if sp_char.count(lstring[i]) ==1:
                lstring[i-1] = ''
            else:
                lstring[i-1] = ' '
    if sp_char.count(lstring[len(lstring)-1]) ==1:
        lstring.pop()
    new_string = ''.join(lstring).lower()
    #print("str:",new_string)
    lstring.clear()
    lstring = new_string.split(" ")
    #print("words:",lstring)
    for i in range(len(lstring)):
        if (lstring.count(lstring[i]) > 1) and (lstring[i] != ''):
            word_list.append(lstring[i])
            lstring[i] = ''
    return sorted(word_list)
