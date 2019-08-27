animals_in_kennel = [
    {
        "id": 1,
        "breed": "German Shepherd",
        "age": 3,
        "name": "Jack"
    },
    {
        "id": 2,
        "breed": "Siamese",
        "age": 9,
        "name": "Shy"
    },
    {
        "id": 3,
        "breed": "Labradoodle",
        "age": 5,
        "name": "Avett"
    },
    {
        "id": 4,
        "breed": "Shnauzer",
        "age": 1,
        "name": "Gypsy"
    },
]

for x in animals_in_kennel:
  if len(x)==4:
    print(x)

# simplest way to produce output

for animal in animals_in_kennel:
  for k,v in animal.items():
      print(f'Key "{k}" = {v}')

# Output
# Key "id" = 1
# Key "breed" = German Shepherd
# Key "age" = 3
# Key "name" = Jack
# Key "id" = 2
# Key "breed" = Siamese
# Key "age" = 9
# Key "name" = Shy
# Key "id" = 3
# Key "breed" = Labradoodle
# Key "age" = 5
# Key "name" = Avett
# Key "id" = 4
# Key "breed" = Shnauzer
# Key "age" = 1
# Key "name" = Gypsy

