from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet

from repositories import animal_repository

def save(vet):
    sql = "INSERT INTO vets(name, age) VALUES ( %s, %s ) RETURNING id"
    values = [vet.name, vet.age]
    results = run_sql( sql, values )
    vet.id = results[0]['id']
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    
    for row in results:
        vet = Vet(row['name'], row['age'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['age'])
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def animals(vet):
    animals = []
    sql = "SELECT animals.* FROM animals"
    values = [vet.id]

    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['name'], row['date_of_birth'], row['type'], row['owner_info'], row['treatment_notes'])
        animals.append(animal)

    return animals

def update(vet):
    sql = "UPDATE vets SET (name, age) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.age, vet.id]
    run_sql(sql, values)
