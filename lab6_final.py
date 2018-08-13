num_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',
22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}

inv_dict = {v: k for k, v in num_dict.items()}
def convert_n_to_m(x, n, m):
    if (isinstance(x,(str,int))):
        x_dem = 0
        x_str = str(x)
        xm_list = []
        if (x_str[0] != '-'):
            for i in range(len(x_str)):
                if (ord(x_str[i])>64) and (ord(x_str[i])<91):
                    x_dem = x_dem + int(inv_dict[x_str[i]])*(n**(len(x_str)-1-i))
                else:
                    x_dem = x_dem + int(x_str[i])*(n**(len(x_str)-1-i))
            if m != 1:
                while x_dem//m > 0:
                    if x_dem%m < 9:
                        xm_list.extend(str(x_dem%m))
                    else:
                        xm_list.extend(num_dict[x_dem%m])
                    x_dem = x_dem//m
                    if x_dem//m == 0:
                        if x_dem%m < 9:
                            xm_list.extend(str(x_dem%m))
                        else:
                            xm_list.extend(num_dict[x_dem%m])
                xm_list.reverse()
            else:
                xm_list = list('0' for i in range(x_dem))
            return ''.join(xm_list)
        else:
            return False
    else:
        return False
