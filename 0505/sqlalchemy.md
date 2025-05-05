# SQL Santykiai – One‐to‐Many ir Many‐to‐Many



##  Įvadas

Duomenų bazėse dažnai tenka susieti informaciją per kelių lentelių ryšius.  
**SQLAlchemy** – tai galingas ORM įrankis, leidžiantis Python programose patogiai dirbti su šiais ryšiais.  
Šioje pamokoje nagrinėjami du pagrindiniai ryšių tipai:

- **One-to-Many** (vienas-daugeliui)
- **Many-to-Many** (daug-daugeliui)

---

##  One-to-Many ryšys

**Apibrėžimas:** Viena lentelės eilutė gali turėti daug susijusių eilučių kitoje lentelėje.  
**Pavyzdys:** Viena komanda (`Team`) turi daug programuotojų (`Coder`).

###  Lentelių kūrimas

```python
from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///one_to_many.db")
Base = declarative_base()

class Coder(Base):
    __tablename__ = "coder"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    xp_years = Column(Integer)
    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="coders")

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    coders = relationship("Coder", back_populates="team")

Base.metadata.create_all(engine)
````

###  Ryšio naudojimas su SQLAlchemy

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

team_row = Team(name="DevOps")
coder_row = Coder(first_name="Romas", last_name="Adomaitis", age=35, team=team_row)
coder_row2 = Coder(first_name="Adomas", last_name="Adomaitis", age=25, team=team_row)

session.add(team_row)
session.commit()

print(coder_row.first_name, coder_row.last_name, coder_row.team.name)
print(team_row.coders)
print(*[f"{row.first_name} {row.last_name}\n" for row in team_row.coders])
```

---

## Many-to-Many ryšys

**Apibrėžimas:** Viena lentelės eilutė gali būti susieta su daugeliu kitos lentelės eilučių, ir atvirkščiai.
**Pavyzdys:** Vienas programuotojas (`Coder`) turi kelis įgūdžius (`Skill`), o vienas įgūdis gali priklausyti keliems programuotojams.

### Lentelių kūrimas

```python
from sqlalchemy import Table, Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///many_to_many.db")
Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('coder_id', Integer, ForeignKey('koderiai.id')),
    Column('skill_id', Integer, ForeignKey('skillsai.id'))
)

class Coder(Base):
    __tablename__ = "koderiai"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    xp_years = Column(Integer)
    skills = relationship("Skill", secondary=association_table, back_populates="coders")

class Skill(Base):
    __tablename__ = "skillsai"
    id = Column(Integer, primary_key=True)
    technology = Column(String)
    coders = relationship("Coder", secondary=association_table, back_populates="skills")

Base.metadata.create_all(engine)
```

###  Ryšio naudojimas su SQLAlchemy

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

skill_row1 = Skill(technology="Python")
skill_row2 = Skill(technology="Java")
skill_row3 = Skill(technology="Django")
skill_row4 = Skill(technology="PostgreSQL")
skill_row5 = Skill(technology="Google Cloud")

coder_row1 = Coder(first_name="Romas", last_name="Adomaitis", age=35,
                   skills=[skill_row1, skill_row3, skill_row4])

coder_row2 = Coder(first_name="Adomas", last_name="Adomaitis", age=25,
                   skills=[skill_row1, skill_row2, skill_row5, skill_row4])

coder_row3 = Coder(first_name="Tomas", last_name="Tomaitis", age=25,
                   skills=[skill_row1, skill_row5])

session.add(coder_row1)
session.add(coder_row2)
session.commit()

# Atvaizduoti visus programuotojus ir jų įgūdžius
all_coders = session.query(Coder).all()
for row in all_coders:
    print(row.first_name, row.last_name, row.age, [skill.technology for skill in row.skills])

# Atvaizduoti visus įgūdžius ir susijusius programuotojus
all_skills = session.query(Skill).all()
for row in all_skills:
    print(row.technology, [f"{c.first_name} {c.last_name} {c.age}" for c in row.coders])
```

---

## 📌 Išvados

* **One-to-Many**: naudojamas, kai viena eilutė (pvz., komanda) turi daug susijusių eilučių (pvz., programuotojus).
* **Many-to-Many**: naudojamas, kai abi lentelės turi tarpusavio ryšį (pvz., programuotojai ir jų įgūdžiai).
* `relationship()` ir `ForeignKey()` leidžia lengvai apibrėžti ir valdyti ryšius tarp lentelių.
* SQLAlchemy suteikia efektyvias priemones sudėtingų duomenų modelių valdymui Python aplinkoje.

-
