from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=150)
    dt_nacimento = models.DateField()
    vivo = models.BooleanField(default=True)
    pais_origem = models.CharField(max_length=50)

    def-str-(self):
        return self.nome

class Livro(models.Model):
  
    genero_opcoes =[
      ('tr','terror'),
      ('rm','romance'),  
      ('aj','autoajuda'),
      ('av','aventura'),
      ('mg','mangá'),
      ('hq','historia em quadrinhos'),
      ('bg','biogtrafia')
    ]
  
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=50)
    dt_lancamento = models.DateField()
    preco = models.DecimalField(decimal_places=2,
    max_digits=10,  default=30)
    paginas = models.IntegerField()
    idioma= models.CharField(max_length=30)
    resumo = models.TextField(default='')
    genero = models.CharField(max_length=2,
    choices=genero_opcoes)
    nome = models.ForeignKey(Autor, 
    on_delete=models.SET_DEFAULT, default='')  
    
def-str-(self):
    return self.titulo