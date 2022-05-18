

import cornac
from cornac.data import ImageModality , Reader
from cornac.eval_methods import RatioSplit
from pathlib import Path
import numpy as np
import pandas as pd
import os 

def Recomendacion(datos):

    for key in datos:
        print (key,":",datos[key])
        if key == "array":
            #{ static "features_VGG19_Conv5_block1_features_fine_tunning.npy" }
            Array_url = datos[key]

            indice_i = Array_url.find('"')
            indice_f = Array_url.find('.npy')

            Array_url = Array_url[(indice_i+1):indice_f]
            Array_url = 'feature/static/'+ Array_url + '.npy'
            print(Array_url)
        if key == "IDs":
            #{ static "ids/ids_5189.txt" }
            Ids_url = datos[key]

            indice_i = Ids_url.find('"')
            indice_f = Ids_url.find('.txt')

            Ids_url = Ids_url[(indice_i+1):indice_f]
            Ids_url = 'feature/static/'+ Ids_url + '.txt'
            print(Ids_url)

        if key == "CSV":
            CSV_url = datos[key]

            indice_i = CSV_url.find('"')
            indice_f = CSV_url.find('csv')

            CSV_url = CSV_url[(indice_i+1):indice_f]
            CSV_url = 'feature/static/'+ CSV_url + 'csv'
            print(CSV_url)
            

        if key == "test_size":
            test_size_ = datos[key]
        if key == "validation_size":
            validation_size_ = datos[key]
        if key == "Numero_epocas":
            Numero_epocas = datos[key]
        if key == "tamaño_lote":
            tamaño_lote = datos[key]
    #print(Array_url,"----", Ids_url,"-----",test_size,"-----",validation_size,"-------",Numero_epocas,"----",tamaño_lote)


    reader = Reader()
    feedback = reader.read(CSV_url,fmt= "UI", sep=',')

    item_ids = cornac.data.reader.read_text(Ids_url)

    features = np.load(Array_url)

    # Instantiate a ImageModality, it makes it convenient to work with visual auxiliary information
    # For more details, please refer to the tutorial on how to work with auxiliary data
    item_image_modality = ImageModality(features=features,ids =item_ids , normalized=True)

    # Define an evaluation method to split feedback into train and test sets
    ratio_split = RatioSplit(
        data=feedback,
        test_size=float(test_size_),
        rating_threshold=0.5,
        exclude_unknowns=True,
        verbose=True,
        item_image=item_image_modality,
    )
    # Instantiate CVAE

    vbpr = cornac.models.VBPR(
        k=10,
        k2=20,
        n_epochs=int(Numero_epocas),
        batch_size=int(tamaño_lote),
        learning_rate=0.005,
        lambda_w=1,
        lambda_b=0.01,
        lambda_e=0.0,
        use_gpu=True,
    )

    # Instantiate evaluation measures
    auc = cornac.metrics.AUC()
    rec_50 = cornac.metrics.Recall(k=5)
    precision_50 = cornac.metrics.Precision(k=5)



    ruta_guardado ='C:/Users/erica/Desktop/Aplicacion proyecto de titulo/recomendacion/feature/static/resultados/'
    # Put everything together into an experiment and run it
    cornac.Experiment(eval_method=ratio_split,
     models=[vbpr],
     show_validation = True,
     metrics=[auc, rec_50,precision_50],
     save_dir=ruta_guardado).run()

def listar():

    url = 'C:/Users/erica/Desktop/Aplicacion proyecto de titulo/recomendacion/feature/static/resultados'

    contenido = os.listdir('C:/Users/erica/Desktop/Aplicacion proyecto de titulo/recomendacion/feature/static/resultados')

    imagenes = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(url, fichero)) and fichero.endswith('.log'):
            imagenes.append(fichero)
    #print(imagenes)

    archivo = 'C:/Users/erica/Desktop/Aplicacion proyecto de titulo/recomendacion/feature/static/resultados/' + imagenes[0]

    lineas = []
    with open(archivo,"r") as f:
        for i,linea in enumerate(f.readlines()):
            lineas.append(linea)
    
    Titulos = lineas[3]
    valores = lineas[5]

    print(Titulos+"\n")
    AUC = Titulos.find('AUC')
    Precision = Titulos.find('Precision')
    Recall = Titulos.find('Recall')

    AUC = Titulos[AUC:(AUC+3)]
    Precision = Titulos[Precision:(Precision+12)]
    Recall = Titulos[Recall:(Recall+9)]


    Metricas = []
    resultados = []

    Metricas.append(AUC)
    Metricas.append(Precision)
    Metricas.append(Recall)

    for i in range(4):
        fin = valores.find('|')
        valor = valores[0:fin]
        valores = valores[(fin+1):]
        if valor == 'VBPR ':
            print("es VBPR")
        else:
            inicio = valor.find('0')
            valor = valor[inicio:]
            resultados.append(valor)

    return (resultados, Metricas)






