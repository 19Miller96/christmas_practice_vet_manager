DROP Table animals
DROP Table vets

CREATE Table vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age VARCHAR(255)
);

CREATE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type VARCHAR(255),
    owner_info VARCHAR(255),
    treatment_notes VARCHAR(255)
);