a=int(input("Ingrese el total de preguntas que se le realizó: "))
res=int(input("Ingrese la cantidad de preguntas que respondió correctamente: "))
porcentaje_correctas= (res/a) * 100
if porcentaje_correctas < 40:
    nivel = "Fuera de Nivel"
else:
    if porcentaje_correctas >= 40 and porcentaje_correctas < 70:
        nivel = "Nivel Regular"
    else:
        if porcentaje_correctas >= 70 and porcentaje_correctas < 95:
            nivel = "Nivel Medio"
        else:
            if porcentaje_correctas >= 95:
                nivel = "Nivel Máximo"        

print(f"Porcentaje de respuestas correctas:   {porcentaje_correctas}%")
print(f"Nivel: {nivel}")
