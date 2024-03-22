def ingresar_datos_empleados():
    empleados = []
    for i in range(int(input("Ingrese el numero de empleados: "))):
        nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
        sueldo_base = float(input(f"Ingrese el sueldo base del empleado {i + 1}: "))
        dias_trabajados = int(input(f"Ingrese los dias trabajados por el empleado {i + 1}: "))
        horas_extras = int(input(f"Ingrese las horas extras trabajadas por el empleado {i + 1 }: "))
        ventas = float(input(f"Ingrese el monto total de ventas realizadas por el empleado {i + 1}: "))
        
        empleados.append({
            "nombre": nombre,
            "sueldo base": sueldo_base,
            "dias trabajados": dias_trabajados,
            "horas extras": horas_extras,
            "ventas": ventas
        })
    return empleados

def calcular_sueldos(empleados):
    for empleado in empleados:
        sueldo_normal = empleado["dias trabajados"] * 8 * 8
        sueldo_extra = empleado["horas extras"] * 15
        descuento_seguro = empleado["sueldo base"] * 0.05
        bono_ventas = 0
        if empleado["ventas"] > 5000:
            bono_ventas = empleado["ventas"] * 0.1
        sueldo_final = sueldo_normal + sueldo_extra - descuento_seguro + bono_ventas
        empleado["sueldo_final"] = sueldo_final
        print(f"Nombre: {empleado['nombre']}, Sueldo final: ${sueldo_final}")

def generar_reportes(empleados):
    valor_total = sum(empleado["sueldo_final"] for empleado in empleados)
    
    print("-" * 50)
    print("Informacion de los empleados:")
    print("-" * 50)
    for empleado in empleados:
      nombre = empleado["nombre"]
      for key, value in empleado.items():
        print(f"{key}: {value}")
        print("-" * 25)
       
      sueldo_final= empleado["sueldo_final"]
      print(f"Nombre: {nombre}")
      print(f"Sueldo final: ${sueldo_final}")
      print()

    print("-" * 40)
    print(f"Valor total a pagar de todos los empleaods: ${valor_total}")

    print("-" * 40)

    if valor_total > 10000:
      print("El valor total a pagar es mayor a $10000, por lo que se procedera a realizar un recorte de personal.")
      print("Los dos ultimos empleados seran despedidos.")
      print("-" * 40)
      empleados = empleados[:-2]
      print("Información de los empleados despues del recorte")
      print("-" * 40)
      for empleado in empleados:
        nombre = empleado["nombre"]
        sueldo_final = empleado["sueldo_final"]
        print(f"Nombre: {nombre}")
        print(f"Sueldo final: ${sueldo_final}")
        print()

def ordenar_empleados(empleados):
    if not empleados or "sueldo_final" not in empleados[0]:
        print("Primero debe calcular los sueldos de los empleados.")
        return

    empleados.sort(key=lambda empleado: empleado['sueldo_final'], reverse=True)
    print("Empleados ordenados por sueldo final de mayor a menor:")
    for empleado in empleados:
        print(f"Nombre: {empleado['nombre']}, Sueldo final: ${empleado['sueldo_final']}")

def buscar_empleados(empleados):
    nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre_buscar:
            print(f"Nombre: {empleado['nombre']}, Sueldo final: ${empleado['sueldo_final']}")
            break
    else:
        print("Empleado no encontrado.")

def main():
    empleados = []

    while True:
               
        print("\nmenu de opciones")
        print("1. Ingresar datos de empleados") 
        print("2. Calcular sueldos")
        print("3. Generar reportes")
        print("4. Ordenar empleados por sueldos")
        print("5. buscar empleados por nombre")
        print("0. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opcion no valida.")
            continue 

        if opcion == 1:
            empleados = ingresar_datos_empleados()
        elif opcion == 2:
            calcular_sueldos(empleados)
        elif opcion == 3:
            generar_reportes(empleados)
        elif opcion == 4:
            ordenar_empleados(empleados)
        elif opcion == 5:
            buscar_empleados(empleados)
        elif opcion == 0:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()