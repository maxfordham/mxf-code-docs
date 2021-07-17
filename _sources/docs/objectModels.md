# Object Models

To make code more: re-useable, clearly-defined, portable and well-documented, we can use object models to create definitions of the variables and datatypes that are required for a program to run.

Python is dynamically typed (i.e. you don't have to declare the type of vars before using them), this makes it quick to write, but it can also make it slow to run and be more difficult to maintain / bug-fix in a production environment.

Python [dataclasses](https://docs.python.org/3/library/dataclasses.html), [typing](https://docs.python.org/3/library/typing.html) and type-hinting have been added to the core python library which allow users to more clearly define function and variables. There is also a popular 3rd party library called "[__Pydantic__](https://pydantic-docs.helpmanual.io/)" which allows users to create clearly defined (types required) object models of program variables. This is designed primarily for data-validation, for example when creating a API, but can be used more generally for creating clearly defined data-structures upon which a program can be built.

The [pydantic documentation](https://pydantic-docs.helpmanual.io/) so take a look if you're interested; below i'll outline some suggested use-cases of Pydantic.

With a clearly defined pydantic model it should be possible to:

- generate a portable JSON schema definition of parameters and datatypes used
- generate user-facing markdown documentation with parameter definitions
- facilitate caching appdata to a file-server
- facilitate interface with a database

## JSON schemas

pydantic models can be converted to and from json schemas allowing for language agnostic sharing of object definitions.

- Pydantic model --> JSON schema
  - https://pydantic-docs.helpmanual.io/usage/schema/
- JSON schema --> Pydantic model
  - https://pydantic-docs.helpmanual.io/datamodel_code_generator/

### Example JSON schema --> Pydantic model

Matt Clapham at FCB generated a JSON schema from a C# object model for Energy Tracker. Using the pydantic code-gen tools we can generate a pydantic datamodel that can be easily imported, and used for type checking etc.
```J:\J4047\Incoming\20201008_001 Energy tracker - Energy Tracker data\Energy Tracker project data schema\Energy Tracker project data schema```

```bash
cd objectModels
pip install datamodel-code-generator
datamodel-codegen --input project.schema.json --input-file-type jsonschema --output model.py
```

### Data serialisation

Pydantic models can be easily exported to_dict, to_json, to_pickle etc. There is in-built serialisation of common types and users can define there own serialisation and validators as required. This is useful when reading and writing data-objects to and from file (or database).

https://pydantic-docs.helpmanual.io/usage/exporting_models/

## Clear documentation

### Generating markdown documentation

User facing markdown documentation can be generated from the JSON schema. There is a simple python tool for doing this:

```bash
pip install jsonschema2md
jsonschema2md project.schema.json projectschema.md
```

There is also a more comprehensive javascript version that is developed by adobe:
https://github.com/adobe/jsonschema2md

### Storing variable aliases and other info

in the example below, it demonstrates that using an object model, it is possible to store aliases, descriptions and equations alongside variables. This would:

- make it easier to create output-ready content (formatted graphs and tables) using the descriptive fields
- generate documenation from the calculation definititons
- use the meta data (e.g. eval below) to store relationships between variables

```python
from pydantic import BaseModel, Field

class Elec(BaseModel):
    """
    This is the description of the main model
    """

    v: float = Field(
        42,
        name='voltage',
        description='a wordy description of voltage',
        unit='V'
        eval='voltage = df.resistance * df.current'  # pass this to pandas eval for calc
        gt=0,  # min
        lt=50,  # max
    )
    i: float = Field(
        3,
        name='resistance',
        description='a wordy description of voltage',
        unit='V'
        eval='resistance = df.voltage / df.current'  # pass this to pandas eval for calc
        gt=0,  # min
        lt=50,  # max
    )
```

## Mapping to database ORMs (Object Relationship Mapping) 

there is an example of using Pydantic with SQLalchemy here: 
https://pydantic-docs.helpmanual.io/usage/models/

also an experimental repo for making SQLalchemy models directly from Pydantic models:
https://github.com/tiangolo/pydantic-sqlalchemy

## Better code

Making clearly defined object types can reduce repetition of variable definitions and make it easier to share commonly used data objects. Using type-hinting, see example below, one can make functions that have defined object definitions to run and output defined object definitions. This improves clarity. Type hints also make writing code much easier as intellisense kicks in.

```python
from dataclasses import dataclass, asdict
from dacite import from_dict

@dataclass
class myobj:
    var = None

@dataclass
class newobj:
    var = None
    var1 = None


def func(obj: myobj) -> newobj:
    newobj = from_dict(data=asdict(myobj),data_class=newobj)
    return newobj
```
