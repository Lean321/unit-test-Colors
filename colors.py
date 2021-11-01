colors=['blue','yellow','red']

def fcolor(vtext):
    vflag = 0
    while vflag == 0:
        if vtext == 'quit':
            vflag = 1
            return('bye')
        elif vtext not in colors:
            return('Not a valid color')
        else:
            return(vtext)

def fcolor_print(vtext):
    vflag = 0
    while vflag == 0:
        if vtext == 'quit':
            vflag = 1
            print('bye')
        elif vtext not in colors:
            print('Not a valid color')
        else:
            print(vtext)

