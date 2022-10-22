import requests
import os

museo=requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects=True)
os.makedirs('museos/2022-octubre')
f=open('museos/2022-octubre/museos-22-10-2022.csv', 'wb')
f.write(museo.content)

bibliotecas=requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects=True)
os.makedirs('bibliotecas/2022-octubre')
f=open('bibliotecas/2022-octubre/bibliotecas-22-10-2022.csv', 'wb')
f.write(bibliotecas.content)

cines=requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/f7a8edb8-9208-41b0-8f19-d72811dcea97/download/salas_cine.csv", allow_redirects=True)
os.makedirs('cines/2022-octubre')
f=open('cines/2022-octubre/cines-22-10-2022.csv', 'wb')
f.write(cines.content)
