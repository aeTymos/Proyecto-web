from django.forms import ValidationError
from datetime import date

class MaxSizeFileValidator:

    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size*1048576

        if size > max_size:
            raise ValidationError('El tamaño máximo del archivo debe ser de {}Mb'.format(self.max_file_size))
        
        return value

def noFechaFuturo(value):
    hoy = date.today()
    if value > hoy:
        raise ValidationError('La fecha de agregado no puede ser un día en el futuro') 