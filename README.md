# INDONESIAN LANGUAGE PARSER CKY ALGORITHM

FILE DIRECTORY GUIDE:
- cfg.txt -> contains the CFG form of grammar
- init.py -> contains function to move CFG from text file into a dictionary
- converter.py -> converts the CFG into CNF form and stores it in cnf.txt
- cnf.txt -> stores the CNF form of grammar to be accessed for CYK algorithm
- cyk.py -> uses CNF to implement CYK Algorithm and determine whether a string is accepted in that language or not
- demo.py -> main python file to containing all modules to run the whole program in the click of a button
- openfile -> for opening cnf file in app.py
- app.py -> frontend of the application
- main.py -> main python file to run the whole program
