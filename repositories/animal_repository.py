from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet

from repositories import vet_repository

def save(animal):
    sql = "INSERT INTO animals(name) VALUES (%s) RETURNING id"
    values = [animal.name]
    results = run_sql( sql, values )
    animal.id = results[0]['id']
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['date_of_birth'], row['type'], row['owner_info'], row['treatment_notes'])
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['name'], result['date_of_birth'], result['type'], result['owner_info'], result['treatment_notes'])
    return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animal WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def vets(animal_id):
    vets = []
    sql = "SELECT vets.* FROM vets WHERE animal_id = %s"
    values = [animal_id]

    results = run_sql(sql, values)

    for row in results:
        vet = Vet(row['name'], row['age'])
        vets.append(vet)

    return vets

def update(animal):
    sql = "UPDATE animals SET (name) = (%s) WHERE id = %s"
    values = [animal.name, animal.id]
    run_sql(sql, values)