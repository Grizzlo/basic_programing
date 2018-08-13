num_holes_dict={'0':1,'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1}
def count_holes(n):
    if isinstance(n,(float,dict,tuple,bool)):
        return 'ERROR'
    else:
        char_list = list(str(n))
        if char_list[0] == '-':
            char_list.pop(0)
        while char_list[0]== '0':
            char_list.pop(0)
        #print (char_list)
        count_of_holes = 0
        for i in range(len(char_list)):
            if (ord(char_list[i])<48)or(ord(char_list[i])>57):
                return 'ERROR'
            else:
                count_of_holes = count_of_holes + num_holes_dict[char_list[i]]
        return count_of_holes
