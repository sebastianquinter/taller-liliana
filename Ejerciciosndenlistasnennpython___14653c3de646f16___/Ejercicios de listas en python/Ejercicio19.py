personas={
    "sebas":18,
    "isa": 20,
    "jose": 17,
    "camila":15
}

mayores = [nombre for nombre,edad in personas.items() if edad >=18]
print("los mayores de edad son:",mayores)