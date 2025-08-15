import os, random

ruta = "test"

class herramientas_test:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ruta_entrada = os.path.join(ruta, "entrada")

    """ RUTA CREACION DE ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS"""
    # creacion_deEstructura = lambda self : [os.mkdir(os.path.join(self.ruta, a)) for a in ["entrada", "procesados", "logs"] if not os.path.exists(os.path.join(self.ruta,a))]
    def creacion_deEstructura(self):
        for a in ["entrada", "procesados", "logs"]:
            ruta_completa = os.path.join(self.ruta, a)
            if not os.path.isfile(ruta_completa):
                os.mkdir(ruta_completa)
            
    # creacion_deArchivos = lambda self : [open(os.path.join(self.ruta_entrada, a), "w") for a in ["reporte_final.pdf", "datos_clientes.csv", "notas_importantes.txt", "foto_perfil.img", "ventas_trimestre.csv", "manual_usuario.pdf", "registro_errores.txt", "inventario_2023.csv", "backup_configuracion.img", "estadisticas_finales.csv"] if not os.path.exists(os.path.join(self.ruta_entrada,a))]
    def creacion_deArchivos(self):
        for a in ["reporte_final.pdf", "datos_clientes.csv", "notas_importantes.txt", "foto_perfil.img", "ventas_trimestre.csv", "manual_usuario.pdf", "registro_errores.txt", "inventario_2023.csv", "backup_configuracion.img", "estadisticas_finales.csv"]:
            ruta_completa = os.path.join(self.ruta, a)


    def agregar_informacion_archivos(self):
        def probabilidad_archivo_vacio(probabilidad=0.3):
            return random.random() < probabilidad

        for a in os.listdir(self.ruta_entrada):
            with open(os.path.join(self.ruta_entrada, a), "w") as f:
                if probabilidad_archivo_vacio:
                    f.write("orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged")
                    return f"Se agrego informacion de prueba en el archivo{f}"
                else:
                    f.truncate(0)
class logs:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ruta_log = os.path.join(ruta, "logs")
    
    def creacion_archivo(self):
        nombre = "procesamiento.txt"
        if not os.path.isfile(os.path.join(self.ruta_log, nombre)):
            with open(os.path.join(self.ruta_log, nombre), "w") as archivo:
                pass
        else:
            print(f"Ya a sido el archivo {os.path.join(self.ruta_log, nombre)}")

    def registro_cambios(self, registro):
        print(registro)
            

test = herramientas_test(ruta)
log = logs(ruta)

if __name__ == "__main__":
    log.creacion_archivo()
    log.registro_cambios(test.agregar_informacion_archivos())
    
