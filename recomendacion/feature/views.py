from django.shortcuts import render
from .models import caracteristicas
from django.core.files.storage import FileSystemStorage
from .VBPR import Recomendacion, listar
from .forms import UploadFileForm

def home(request):
    return render(request,'inicio.html')

def extraction(request):
    return render(request, 'extraction.html')

def cargar_datos(request):

    if request.method =='POST':

        form = UploadFileForm(request.POST, request.FILES)

        uploaded_file= request.FILES['document']
        uploaded_csv= request.FILES['CSV']
        uploaded_IDs= request.FILES['IDs']

        
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        fs.save(uploaded_csv.name,uploaded_csv)
        fs.save(uploaded_IDs.name,uploaded_IDs)
        

        ajustes = request.POST
        datos = request.FILES
        datos.update(ajustes)

        #print(datos)


        estatico = False
        Recomendacion(datos,estatico)

        resultados, Metricas = listar()

        #print(resultados)

        """
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_csv.name)
        print(uploaded_csv.size)
        print(uploaded_IDs.name)
        print(uploaded_IDs.size)
        """

        return render(request, 'formulario_recomendacion.html', {'resultados':resultados, 'Metricas':Metricas})
    else:
        form = UploadFileForm()

    return render(request, 'Cargar_datos.html',{'form': form})

def recomendacion(request):
    
    datos = request.POST
    estatico = True
    Recomendacion(datos,estatico)
    resultados, Metricas = listar()
    
    print(resultados)

    return render(request, 'formulario_recomendacion.html', {'resultados':resultados, 'Metricas':Metricas})

def VBPR(request):
    carac = caracteristicas.objects.all()

    return render(request,'formulario_recomendacion.html', {'carac': carac})