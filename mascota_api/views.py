from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Mascota
from .forms import MascotaForm
import json

# 1. LISTAR (GET)
def api_lista_mascotas(request):
    mascotas = Mascota.objects.all().values()  # Convierte el QuerySet a diccionarios
    return JsonResponse(list(mascotas), safe=False)

# 2. CREAR (POST)
@csrf_exempt
def api_crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'mensaje': 'Mascota creada'
            }, status=201)
        else:
            return JsonResponse({
                'mensaje': 'Error de registro',
                'errores': form.errors
            }, status=422)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# 3. ACTUALIZAR (PUT/POST)
@csrf_exempt
def api_editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {'error': 'JSON inválido'},
                status=400
            )

        form = MascotaForm(data, instance=mascota)

        if form.is_valid():
            form.save()
            return JsonResponse(
                {'mensaje': 'Mascota actualizada correctamente'},
                status=200
            )
        else:
            return JsonResponse(
                {'errores': form.errors},
                status=422
            )

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# 4. ELIMINAR (DELETE)
@csrf_exempt
def api_eliminar_mascota(request, pk):
    if request.method == 'DELETE':
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        return JsonResponse({'mensaje': 'Mascota eliminada'}, status=204)
    return JsonResponse({'error': 'Método no permitido'}, status=405)