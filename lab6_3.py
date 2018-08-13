
def saddle_point(matrix):
    row_min = []
    answ = ()
    reversed_matrix = []
    for i in range(len(matrix)):
        if matrix[i].count(min(matrix[i])) == 1:
           row_min.append([min(matrix[i]),i,matrix[i].index(min(matrix[i]))])
           reversed_matrix.append([matrix[j][matrix[i].index(min(matrix[i]))] for j in range(len(matrix))])
    #print (reversed_matrix)
    #print (row_min)
    for i in range(len(reversed_matrix)):
        if reversed_matrix[i].count(max(reversed_matrix[i])) == 1:
            if max(reversed_matrix[i])==row_min[i][0]:
                #print (max(reversed_matrix[i]))
                answ = (row_min[i][1],row_min[i][2])
                return answ
    return False
