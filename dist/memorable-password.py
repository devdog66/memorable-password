from classes import RandomMethods, UserInput

rm = RandomMethods()
ui = UserInput()
 
maxLength = ui.getMaxLength()
numberOfPasswords = ui.getNumberOfPasswords()
rm.randomPasswords(numberOfPasswords, maxLength)

