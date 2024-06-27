phonebook = {
    "Vanya": 100, 
    "Petya": 200,
    "Alisa": 300
    }


other_phonebook = {
    "Igor": 1000, 
    "Petya": 800,
      "Alyena": 2000
      }


phonebook.update(other_phonebook)

phonebook['Gosha']=phonebook.pop('Igor')


print(phonebook)

print(phonebook.keys(),phonebook["Vanya"])

print(phonebook.get('Stepasn'))

