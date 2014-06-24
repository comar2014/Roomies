class  Apartamento:

      
    def __init__(self): # Constructor para  la publicacion de apartamentos 
        self.Titulo=  ""
        self.Descripcion= ""
        self.Facilidades= ""
        self.Caracteristicas=""
        self.Ubicacion= ""
        self.Precio= ""
        self.Telefono= ""
        self.Correo= ""
        self.lista=[]
        self.lista=self.leer_Archivo()
        


    def crear_Archivo(self):
        archi=open('Apartamentos.txt','a')
        archi.close()
        

# Metodo que permite recibir las variables del html para escibirlas en un archivo, y si permitir la publicacion del apartamento
    def Publica_Apartamento(self,titulo, descripcion,facil,caract,ubi,pre,tel, email): 
            
          #  Facilidades= []
            print("Ingrese los datos del apartamento que desea publicar\n")
            self.Titulo= titulo
            self.Descripcion= descripcion
            self.Facilidades= facil
            self.Caracteristicas= caract
            self.Ubicacion= ubi
            self.Precio= pre
            self.Telefono= tel
            self.Correo= email
            Archivito=open('Apartamentos.txt','a')
            Archivito.write(str(self.Titulo).lower() + ";" + str(self.Descripcion).lower()+ ";"+  str(self.Facilidades).lower() + ";" +  str( self.Caracteristicas)  + ";" + str(self.Ubicacion).lower() + ";" + str(self.Precio).lower() + ";" + str(self.Telefono).lower() + ";" + str(self.Correo).lower())
            Archivito.write("\n")
            print("\n")
            print("Los datos del apartamento se han ingresado exitosamente\n")
            Archivito.close()
                
 #***********************************************************************************************
    # Se encarga de leer el archivo en donde se encuentran los datos del 

    def leer_Archivo(self):

        archi=open('Apartamentos.txt','r') 
        self.listaFacilidades=[]
        self.listaCaracteristicas=[]
        linea=archi.readlines() # Lista que contiene todas las lineas del archivo.    

        for li in linea:
     
           elimina=li.strip("\n") # elimina el salto de linea 
           y=elimina
           self.lista= self.lista + [self.lista.append([str(y)])]
         
        archi.close()
        self.lista= list(filter(None,self.lista))
        return self.lista
     
# Realiza la busqueda ya sea por cacteristica o facilidad
    def busqueda_Facilidades(self, facilidad):
        resultados=[]
        for  apartamento in  self.lista: # Recorre la lista estan todos los apartamentos
            for elem in apartamento: # recorre las sublistas de la lista 
                if facilidad in elem: # compara  elementos
                    resultados.append(apartamento)
                    
        if resultados==[]:
            print("No hay resultados")
         
        return resultados


    def busqueda_Precio(self, precio, mayor_menor):
        resultados=[]
        for  apartamento in  self.lista:# Recorre la lista estan todos los apartamentos
           ls_apartamento=apartamento[0].split(";") # Separa el string y lo convierte en lista
           if mayor_menor== "<":
                if float(precio) >= float(ls_apartamento[5]):
                    resultados.append(apartamento)#lista que contiene los apartamentos con los precios 
           else:
                if float(precio) < float(ls_apartamento[5]):
                    resultados.append(apartamento)

        if resultados==[]:
            print("No hay resultados")
        else:
            ls_resultados=[]
            lista_temp=[]
            for aparta in resultados: # recorre la lista de apartamentos ya buscados por el precio 
                lista_temp= aparta[0].split(";") # Convierte las facilidades en una lista
                ls_resultados.append(lista_temp)
                lista_temp=[]
            resultados=sorted(ls_resultados, key=lambda aparta: int(aparta[5]))  
        return resultados

    

    def lista_favoritos(self, nom_usa,apartamento):
        archi=open(nom_usa + "_favoritos.txt",'a')
        archi.write(str(apartamento))
        archi.write("\n")
        archi.close()
        # Crear archivo con el nombre del usuario_favoritos
        #escribe el apartamento selecionada en el app como favorito



  
