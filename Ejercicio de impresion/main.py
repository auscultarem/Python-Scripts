print("Hello wolrd!!\t") #uso del tabulor
print("\nThose are my first lines of code") #Se imprime un enter antes de ejecutar la linea


######
print ("Mary had a little lamb.")
print ("its fleece was white as %s." % 'snow')
print ("And everywhre that mary went.")
print ("." * 10) # que hara?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


print (end1 + end2 + end3 + end4 + end5 + end6),
print (end7 + end8 +end9 + end10 + end11 +end12)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Aqui estan los dias: ", days)
print("Aqui estan los meses: ", months)

#############
print("Let's practice everithing.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.\n")

poem ="""
\tThe lovely world
with logic so firmly planted
cannot dicern \n the needs of love
nor comprehend passion from intuition
and requieres an explanation
\n\t\twhere there is none.
"""

print("---------------")
print (poem)
print ("---------------")

five = 10 - 2 + 3 - 6
print("This should be five: {0}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {0}".format(start_point))
print("We'd have {0} beans, {1} jars, ans {2} crates".format(beans, jars, crates))

start_point = start_point / 10

print("\nWe can also do that this way: ")
print("we'd have {0} beans, jars, and  crates.\n".format(secret_formula(start_point)))