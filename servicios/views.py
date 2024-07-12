from django.shortcuts import render
import requests
from django.shortcuts import redirect
import requests



def index(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        ncontacto = request.POST.get('ncontacto')
        placamoto = request.POST.get('placamoto')
        serviciossolicitados = request.POST.get('serviciossolicitados')
        repuestosolicitados = request.POST.get('repuestosolicitados')
        fechaactual = request.POST.get('fechaactual')
        fechasolicitada = request.POST.get('fechasolicitada')
        asesor = request.POST.get('asesor')
        mecanico = request.POST.get('mecanico')

        url_api_fastapi = 'https://tesis-back-motoware.onrender.com/solicitudes/solicitudes/'

        data = {
            "id": id,
            "nombres": nombres,
            "apellidos": apellidos,
            "ncontacto": ncontacto,
            "placamoto": placamoto,
            "serviciossolicitados": serviciossolicitados,
            "repuestosolicitados": repuestosolicitados,
            "fechaactual": fechaactual,
            "fechasolicitada": fechasolicitada,
            "asesor": asesor,
            "mecanico": mecanico,
        }

        try:
            response = requests.post(url_api_fastapi, json=data)
            response.raise_for_status()  

            if response.status_code == 200:
                return render(request, 'index.html', {'message': 'Solicitud registrada correctamente.'})
            else:
                return render(request, 'servicios/index.html', {'error_message': 'Su solicitud se ha enviado correctamente.'})

        except requests.exceptions.RequestException as e:
            return render(request, 'servicios/index.html', {'error_message': f'Error en la conexión: {e}'})

   
    return render(request, 'servicios/index.html')

