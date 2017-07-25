familyNames = []
while True:
        print('Enter the name of the family member ' + str(len(familyNames) + 1) +
              ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        familyNames = familyNames + [name] # list concentation
print('The family names are:')
for name in familyNames:
        print('   ' + name)
        
