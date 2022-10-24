
names = {
    'parents': ['clair', 'jason'],
    'kids': ['thomas', 'zachary'], 
    'pets': ['ella', 'lucy']
}

for key in names:
    type = key.capitalize()
    for name in names[key]:
        print(f'{type} name is {name}')
