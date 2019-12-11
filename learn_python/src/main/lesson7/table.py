# table.py

def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attriutes from a list of objects
    :param objects:
    :param colnames:
    :return:
    '''
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    for obj in objects:
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj,colname))), end = ' ')
        print()



# NOTE: In the print( , end = ' ') the end with empty spaces tells it not to go to new line.

