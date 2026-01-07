#  string ##
#Strings are immutable in nature. It means the value of a string cannot be tampered or changed.

##### Formatted String #######
first_name="Khushi"
last_name="Gohel"

print(f"welcome {first_name} {last_name}")

####### string indexing ###########
txt = "python"
print(txt[0])
print(txt[0:2])
print(txt[0::2])
print(txt[::-1])
print(txt[1:])
print(txt[-1])
print(txt[::-1])

##### Built-in string functions and methods #########
quote = 'java is awesome'
print(len(quote))   #len function

new_quote=quote.replace('java','python')  #replace()
print(new_quote)

print(new_quote.capitalize())    #capitalize()

print(new_quote.upper())

