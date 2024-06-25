import os

class Pelicula:
    def __init__(self,nombre,anio,director):
     self._nombre = nombre
     self._anio = anio
     self._director = director


class catalogoPeliculas:
  def __init__(self,nombre,ruta):
    self.nombre = nombre
    self.ruta = ruta


  def agregar_pelicula(self,pelicula):
    
    try:
      f = open(self.ruta,"a")
    except FileNotFoundError:
            print("¡La pelicula " + self.nombre + " no existe!\n")
            return
    else:
      f.write(pelicula._nombre + " ," + pelicula._anio + "," + pelicula._director + '\n')
      f.close()
      print("La pelicula se ha guardado.\n")
      return

  def listar_pelicula(self):
    
    f = open(self.ruta, 'r')
    print(f.read())
    f.close()

  def eliminar_catalogo(self):

    try:
      os.remove(self.ruta)
      print("El catálogo se ha borrado \n") 
      return
    except FileNotFoundError:
      print("¡El catálogo no existe!\n")
      return
        

def mostrar_menu():
  
 print("\n Menú de Opciones: ")
 print("1. Agregar Película")
 print("2. Listar Películas")
 print("3. Eliminar catálogo películas")
 print("4. Salir")


def main(): 
  
  nombre_catalogo = input("Ingrese el nombre del catálogo: ")
  ruta_catalogo = nombre_catalogo + ".txt" 
  catalogo = catalogoPeliculas(nombre_catalogo, ruta_catalogo)

  while True:
   mostrar_menu()
   opcion= input("Seleccione una opción: ")

   if opcion == "1":
    titulo = input("Ingrese el título de la película: ")
    director = input("Ingrese el director de la película: ")
    anio = input("Ingrese el año de la película: ")

    pelicula = Pelicula(titulo,director,anio)
    catalogo.agregar_pelicula(pelicula)

   elif opcion == "2":
    catalogo.listar_pelicula()
    
   elif opcion == "3":
    print(catalogo.eliminar_catalogo())
    
   elif opcion == "4":
       print("Saliendo del programa")
       break
  else:
    print("Opción no válida. Por favor, intente de nuevo")

if __name__ == "__main__":
  main()