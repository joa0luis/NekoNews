from django.db import models
from django.contrib.auth.models import User
 # AQUE FICARA OS MODELOS DE NOTICIAS E INFORMACOES BASICAS.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    data_publi = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='noticias/',null=True,blank=True)

    def __str__(self):
        return self.titulo

 
