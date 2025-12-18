#Logistic company needs a dictionary for theirs operations 

#1-Diccionario base
operation = {
    "operation_id" : "IMP-001",
    "status" : "PRODUCTION",
    "provider" : "MAERSK",
    "origin" : "CN",
    "destination" : "CO"
    }

#print(operation) - 
# output {'operation_id': 'IMP-001', 'status': 'PRODUCTION', 'provider': 'MAERSK', 'origin': 'CN', 'destination': 'CO'}

#2-Accedemos al campo
print("Operation ID", operation["operation_id"])
print("Status", operation["status"])

#operation["status"] es cómo se accede a los datos en backend

#3- Condicional para actualizar estado
if (operation["status"] == "PRODUCTION"):
    operation["status"] = "COMPLETED"

print("Updated operation", operation)

#4- Lista de operaciones (usa la misma + otra) 

operations = [
    operation,
    {
        "operation_id": "EXP-002",
        "status": "DRAFT",
        "provider": "MSC",
        "origin": "CO",
        "destination": "US"
    }
]


#5-recorre la lista
for op in operations:
    print(op["operation_id"], "->", op["status"])
#🧠 Esto es exactamente lo que hace una API cuando devuelve “muchas operaciones”.
