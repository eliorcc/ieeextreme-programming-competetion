#NOTE:
#CARBON DIOXIDE CONTAINS 2 OXYGEN ATOMS AND 1 CARBON ATOM PER MOLECULE
#WATER CONTAINS 2 HYDROGEN ATOMS AND 1 OXYGEN ATOM PER MOLECULE
#GLUCUSE CONTAINS 6 CARBON ATOMS 12 HYDROGEN ATOMS AND 6 OXYGEN ATOMS PER MOLECULE

#WE CAN CALCUALTE IT BY SOLVING AN 3 VARIABLES EQUATION
atoms = input()
spitted_list_Atoms = (atoms.split(" "))
carbon_atoms = int(spitted_list_Atoms[0])
hydrogen_atoms = int(spitted_list_Atoms[1])
oxygen_atoms = int(spitted_list_Atoms[2])
# print(carbon_atoms,hydrogen_atoms,oxygen_atoms)
# carbon_dioxide + 6*glocuse = number of carbon atoms
# water + 6glocuse = number of hydrogen/2 atoms
# water + 2carbon-dioxide +6glocuse = oxygen atoms
CARBON_DIOXIDE_MOLECULES = (2 * oxygen_atoms - hydrogen_atoms)/4
WATER_MOLECULES = (hydrogen_atoms - 2 * carbon_atoms + 2 * CARBON_DIOXIDE_MOLECULES)/2
GLUCOSE_MOLECULES = (carbon_atoms - CARBON_DIOXIDE_MOLECULES) / 6

#NOW WE NEED TO CHECK IF THEY ALL CONTAINS ONLY FROM NATURL NUMBERS

if(WATER_MOLECULES < 0 or (int(WATER_MOLECULES) != WATER_MOLECULES)):
    print("ERROR")
if(CARBON_DIOXIDE_MOLECULES < 0 or (int(CARBON_DIOXIDE_MOLECULES) != CARBON_DIOXIDE_MOLECULES)):
    print("ERROR")
if(GLUCOSE_MOLECULES < 0 or (int(GLUCOSE_MOLECULES) != GLUCOSE_MOLECULES)):
    print("ERROR")
else:
    print(int(WATER_MOLECULES),int(CARBON_DIOXIDE_MOLECULES),int(GLUCOSE_MOLECULES))
