 ## perform the file ask
#### create the file and write the file

# with open('file.txt','x') as file:
#     write=file.write("Hello Word \n It is My Python Task....")
#     print("FIle is created and conect is wrie...")
    
### muliple line can be wrie
with open('file.txt', mode='w', encoding='utf-8') as my_file:
    my_file.writelines(['First line', '\n', 'Second Line'])
    print("wrie....")
#### read the file ####
with open('file.txt','r') as file:
    print(file.read())
    

#### seek() ####
with open('file.txt', mode='r', encoding='utf-8') as my_file:
    my_file.seek(0) # brings cursor to beginning of file
    print(my_file.tell()) # prints location of cursor
    content = my_file.read()
    print(content)
    
    
#### a translator program that can read a file with English content and create a new translated version of the file in a different language.
from translate import Translator

spanish_translate=Translator(to_lang='es')
french_translate=Translator(to_lang='fr')

try:
    with open('translate.txt','r') as file:
        quote=file.read()
        quote_spanish =spanish_translate.translate(quote)
        quote_french=french_translate.translate(quote)
        print(quote_french,quote_spanish)
        
        try:
            with open('quote-es.txt', mode='w') as quote_de:
                quote_de.write(quote_spanish)
            with open('quote-fr.txt', mode='w') as quote_fr:
                quote_fr.write(quote_french)
        except IOError as error:
            print('An error ocurred')
            raise (error)
except FileNotFoundError as error:
    print('File not found')
    raise (error)