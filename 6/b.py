# Write a program to use split and join methods in the string and trace a birthday of a person with a dictionary data
# structure.


birthdays = {'samyak_jain': '14-09-2000', 'python': '20-02-1991'}

name = '_'.join(input('\nName: ').lower().split())

print('Birthday:', birthdays.get(name, 'not found'))
