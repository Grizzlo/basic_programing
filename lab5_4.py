
def file_search(struct,file_name):
    path_to_file=''
    if struct.count(file_name) > 0:
        path_to_file = struct[0]+'/'+struct[struct.index(file_name)]
        return path_to_file
    else:
        for i in range(len(struct)):
            if type(struct[i]) == list:
                struct[i][0]= struct[0]+'/'+struct[i][0]
                path_to_file=file_search(struct[i],file_name)
        if path_to_file=='':
            return False
        else:
            return path_to_file
