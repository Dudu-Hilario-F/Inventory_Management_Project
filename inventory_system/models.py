from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import re
from django.core.exceptions import ValidationError
from .utils import check_email


class Sector(models.Model):
        # Opções pré-definidas de setores existentes
    # Opções para o campo 'operation_status'
    class SectorOperation(models.TextChoices):
        OFFAL = "Laticinios", "Laticinios"
        COLDS = "Resfriados", "Resfriados"
        FROZEN = "Congelados", "Congelados"
        CATTLE = "Bovinos", "Bovinos"
        PIGS = "Suinos","Suinos"
        CLIMATE = "Climatizado", "Climatizado"
        COD = "Bacalhau", "Bacalhau"



    code = models.IntegerField(
        unique=True, 
        primary_key=True, 
        verbose_name="Codigo",
        db_index=True
        
    )
    
    sector = models.CharField(
        unique=True, 
        max_length=100,
        choices=SectorOperation.choices,
        default=SectorOperation.COLDS,
        verbose_name="Setor",
        help_text="Nome do setor"
    
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Criado em"
    )
    update_at = models.DateTimeField(
        auto_now=True, 
        verbose_name= "Atualizado em"
    )


    def __str__(self):
        return self.sector
    
class Camaras(models.Model):

    # Opções para o campo 'operation_status'
    class OperationStatus(models.TextChoices):
        ACTIVE = "Ativa", "Ativa"
        DISABLED = "Desativada", "Desativada"
        IN_MAINTENANCE = "Em manutenção", "Em manutenção"
    

    # class fields
    code = models.IntegerField(
        unique=True, 
        primary_key=True, 
        verbose_name="Codigo",
        db_index=True
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome",
        help_text="Nome da camara fria"
    )

    location = models.CharField(
        max_length=100, 
        verbose_name="Localização",
        help_text="Localização da camara"
    )

    operation_status = models.CharField(
        max_length=20,
        choices=OperationStatus.choices,
        default=OperationStatus.ACTIVE,
        verbose_name="Status de Operação"
    )

    min_temperature = models.FloatField(
        validators=[MinValueValidator(-99.99), MaxValueValidator(99.99)],
        help_text="Informe a temperatura minima",
        verbose_name="Temperatura minima"

        

    )
    max_temperature = models.FloatField(
        validators=[MinValueValidator(-99.99), MaxValueValidator(99.99)],
        help_text="Informe a temperatura maxima",
        verbose_name="Temperatura maxima"
    )

    min_humidity = models.FloatField(
        validators=[MinValueValidator(-99.99), MaxValueValidator(99.99)],
        help_text="Informe a umidade minima",
        verbose_name="Umidade minima"
    )

    max_humidity = models.FloatField(

        validators=[MinValueValidator(-99.99), MaxValueValidator(99.99)],
        help_text="Informe a umidade maxima",
        verbose_name="Umidade maxima"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Criado em"
    )

    update_at = models.DateTimeField(
        auto_now=True, 
        verbose_name= "Atualizado em"
    )

    description = models.TextField(
        help_text="Insira uma descrição detalhada do produto.",
        verbose_name="Descrição"
    )

    # Foreign keyForeign key
    ID_Sector = models.ForeignKey(
        Sector,
        on_delete=models.CASCADE,
    )

    # Class Method
    def __str__(self):
        return self.name
    
class Category(models.Model):
    class CategoryOperation(models.TextChoices):
        DAIRY_PRODUCTS = "Laticinios", "Laticinios"
        COLD = "Resfriados", "Resfriados"
        FROZEN = "Congelados", "Congelados"
        IN_NATURA_MEAT = "Carne in Natura", "Carne in Natura"
        FISH_AND_SEAFOOD = "Pescados e Frutos do Mar ","Pescados e Frutos do Mar"
        AIR_CONDITIONER = "Climatizado", "Climatizado"

    code = models.IntegerField(
        unique=True, 
        primary_key=True, 
        verbose_name="Codigo",
        db_index=True
    )

    name = models.CharField(
        max_length=100, 
        unique=True,
        choices=CategoryOperation.choices,
        default=CategoryOperation.IN_NATURA_MEAT
    
    )

    description = models.TextField(

        help_text="Descrição da Categoria",
        verbose_name="Descrição"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Criado em"
    )
    update_at = models.DateTimeField(
        auto_now=True, 
        verbose_name= "Atualizado em"
    )


    def __str__(self):
        return self.name

class Fornecedores(models.Model):
    class StatusFornecedor(models.TextChoices):
        ACTIVE = "Ativo", "Ativo"
        DISABLED = "Inativo", "Inativo"
    
    code = models.IntegerField(
        primary_key=True, 
        unique=True,
        help_text="Codigo do fornecedores",
        db_index=True,
        verbose_name="Codigo"
    
    )

    name = models.CharField(
        unique=True, 
        max_length=100,
        help_text="Nome",
        verbose_name="Nome Fornecedor",
    )

    email = models.EmailField(
        max_length=254, 
        unique=True, 
        verbose_name="E-mail"
    )

    cnpj = models.CharField(
        max_length=18,
        help_text="CNPJ",
        verbose_name="CNPJ",
        unique=True,
        validators= [check_email()]
    )

    status = models.CharField(
        max_length=20,
        choices=StatusFornecedor.choices,
        editable=True, 
        default=StatusFornecedor.DISABLED
           
    )


    # Foreign keyForeign key
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )



class Filial(models.Model):
    pass

class EnderecoFornecedor(models.Model):
    pass

class EnderecoFilial(models.Model):
    pass

class RecebimentoCarne(models.Model):
    pass


class AnaliseCarne(models.Model):
    pass

class Produtos(models.Model):
    pass