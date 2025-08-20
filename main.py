import os, random
from datetime import datetime

ruta = "test"

class herramientas_test:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ruta_entrada = os.path.join(ruta, "entrada")

    """ RUTA CREACION DE ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS"""
    def creacion_deEstructura(self, historial=[]):

        for a in ["entrada", "procesados", "logs"]:
            ruta_completa = os.path.join(self.ruta, a)

            if not os.path.isdir(ruta_completa):
                os.mkdir(ruta_completa)
                historial.append(os.path.basename(ruta_completa))

        return historial
                   
    def creacion_deArchivos(self, historial=[]):

        for a in ["reporte_final.pdf", "datos_clientes.csv", "notas_importantes.txt", "foto_perfil.img", "ventas_trimestre.csv", "manual_usuario.pdf", "registro_errores.txt", "inventario_2023.csv", "backup_configuracion.img", "estadisticas_finales.csv"]:
            ruta_completa = os.path.join(self.ruta,"entrada", a)

            if not os.path.exists(ruta_completa):
                open(ruta_completa, "w")
                historial.append(os.path.basename(ruta_completa))

        return historial
    
    def agregar_informacion_archivos(self, historial=[]):

        def probabilidad_archivo_vacio(probabilidad=0.3):
            return random.random() < probabilidad

        for a in os.listdir(self.ruta_entrada):
            ruta_completa = os.path.join(self.ruta_entrada, a)

            with open(ruta_completa, "w") as f:
                if probabilidad_archivo_vacio:
                    f.write("orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged")
                    historial.append(os.path.basename(ruta_completa))
                else:
                    f.truncate(0)

        return historial

class logs:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ruta_log = os.path.join(ruta, "logs")
        self.nombre = "procesamiento.txt"
        self.ruta_completa = os.path.join(self.ruta_log, self.nombre)
        self.lista_logs = []

    def creacion_archivo(self):
        if not os.path.isfile(self.ruta_completa):
            open(self.ruta_completa, "w")
            return os.path.basename(self.ruta_completa)

        return os.path.basename(self.ruta_completa)

    def registro_cambios(self, *registros):
        lista_combinada = []

        for registro in registros:
            if isinstance(registro, list):
                lista_combinada.extend(registro)
            else:
                lista_combinada.append(registro)

        for n, item in enumerate(lista_combinada, 1):
            print(f"{n}. {item}")

test = herramientas_test(ruta)
log = logs(ruta)

if __name__ == "__main__":
    funciones = [
        test.creacion_deEstructura(),
        test.creacion_deArchivos(),
        test.agregar_informacion_archivos(),
        log.creacion_archivo(),
    ]

    log.registro_cambios(*funciones)

