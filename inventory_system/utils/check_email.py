import re
from django.core.exceptions import ValidationError


def check_cnpj(x):
        cnpj = x
        regex_cnpj = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
        if re.match(regex_cnpj, cnpj):
            pass
        else:
            raise ValidationError("Campo não está em formado de cnpj")
