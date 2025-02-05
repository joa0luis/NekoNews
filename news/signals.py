from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def enviar_email_bem_vindo(sender, instance, created, **kwargs):
    if created:  # Verifica se é um novo usuário
        assunto = "Bem-vindo ao NEKO NEWS!"
        mensagem = f"Olá {instance.username}, pelo visto você é um otaku fidido, não se preocupe esse site é apenas um projeto pra meu portifolio back-end!"
        destinatario = [instance.email]  # E-mail cadastrado pelo usuário
        send_mail(
            assunto,
            mensagem,
            'seuemail@gmail.com',  # Substitua pelo seu e-mail
            destinatario,
            fail_silently=False,)
        
        
