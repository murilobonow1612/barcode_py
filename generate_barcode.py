import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    ean13 = barcode.get_barcode_class('ean13')
    barcode_instance = ean13(data, writer=ImageWriter())
    barcode_instance.save(filename)

data = "4006381333931"
filename = "barcode_gerado"
generate_barcode(data, filename)