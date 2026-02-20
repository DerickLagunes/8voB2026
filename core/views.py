from django.shortcuts import render
from core.alumno import alumno
from core.forms import ContactoForm

# Create your views here.
def index(request):
    print("El usuario entro al sistema")
    return render(request, 'core/index.html')

def nuevo(request):
    variable = alumno("Pablo","Perez",20)
    return render(request, 'core/nuevo.html',{"alumno": variable})


from django.http import JsonResponse

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            #Registrar en la BD
            form.save()
            return JsonResponse({
                'status':'ok',
                'mensaje':'registro exitoso!'
            })
        else:
            return JsonResponse({
                'status':'error',
                'errors':form.errors
            })
            #return render(request, 'core/formulario.html', {'form': form, 'success': True})
    else:
        form = ContactoForm()
    
    return render(request, 'core/formulario.html', {'form': form})