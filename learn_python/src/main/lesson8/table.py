# table.py

def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attriutes from a list of objects
    :param objects:
    :param colnames:
    :return:
    '''
    # Emit table headers
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    for obj in objects:
        # Emit for of table data
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj,colname))), end = ' ')
        print()


def print_table_v2(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attriutes from a list of objects
    Then instead of hard coding the printing I will let it drive the formatter object
    '''
    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames ]
        formatter.row(rowdata)



# NOTE: In the print( , end = ' ') the end with empty spaces tells it not to go to new line.

'''
class TableFormatter(object):
    def headings(self, headers):
        raise NotImplementedError
    
    def row(self,rowdata):
        raise NotImplementedError
'''


class TableFormatter(object):
    # Serves as a design spec for making tables and inheritance to customize
    def headings(self, headers):
        raise NotImplementedError

    def row(self,rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for header in headers:
            print('{:10s}'.format(header), end = ' ')
        print()

    def row(self,rowdata):
        for item in rowdata:
            print('{:10s}'.format(item), end = ' ')
        print()


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>', end='')

    def row(self, rowdata):
        print('<tr>', end='')
        for h in rowdata:
            print('<td>{}</td>'.format(h), end='')
        print('</tr>', end='')

