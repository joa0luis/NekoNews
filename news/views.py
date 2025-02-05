from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm
from .models import Noticia
from django.contrib.auth import login
from .forms import RegistroForm


def home(request):
    noticias = Noticia.objects.all().order_by('-data_publi')
    return render(request, 'home.html',{'noticias':noticias})

def sobre(request):
    return render(request,'sobre.html')

def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia,id=id)
    return render(request,'detalhe_noticia.html',{'noticia':noticia})

def perfil(request):
    return render(request, 'perfil.html')

#função para postagens 
@login_required
def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('home')  # Redireciona para a homepage após a postagem
    else:
        form = NoticiaForm()
    return render(request, 'criar_noticia.html', {'form': form})

@login_required
def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if noticia.autor != request.user:  # Garante que só o autor pode editar
        return redirect('home')
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})

@login_required
def excluir_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if noticia.autor == request.user:  # Garante que só o autor pode excluir
        noticia.delete()
    return redirect('home')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/register.html',{'form':form})

def logout_view(request):
    return render(request,'registration/logout.html')

def logout_confirm(request):
    return render(request,'registration/logout.html')


