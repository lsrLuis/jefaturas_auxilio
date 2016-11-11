import csv
#NO,NOMBRE,LATITUD,LONGITUD,DESCRIPCION,DIRECCION
class Analisis:

    data_temp = []

    def __init__(self):
        pass

    def data_read(self, filename):
        with open(filename, "r") as file:
            data = csv.reader(file, dialect='excel')
            for row in data:
                self.data_temp.append(row)

    def data_print(self):
        for row in self.data_temp:
            print row

    def data_get(self):
        return self.data_temp
