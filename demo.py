import barcode
from barcode.writer import ImageWriter

def testEan():
    EAN = barcode.get_barcode_class('Code-39')
    ean = EAN(u'65', writer=ImageWriter())
    fullname = ean.save('my_ean13_barcode')

if __name__ == '__main__':
    testEan()
