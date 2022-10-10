from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Professor, Aulas

# Resonsável por converter a table Professor do banco em um JSON
class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Professor
    fields = '__all__'

# Como o cadastro das aulas não tem no corpo da requisição todos os campos necessários, a criação do serializer é um pouco diferente
class CadastrarAulaSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  nome = serializers.CharField(max_length=100)

  # Criando validações adicionais de dados
  def validate_nome(self, value):
    if len(value) < 3:
      raise ValidationError("Nome deve ter ao menos três caracteres")
    return value

# Serializer da Aula após ser cadastrada
class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aulas
    fields = '__all__'