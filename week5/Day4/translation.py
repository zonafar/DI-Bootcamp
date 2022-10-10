from translate import Translator

input = "C:/Users/ZONA/3D Objects/Orange DI/DI-Bootcamp/week5/Day4/english_text.txt"
output = "C:/Users/ZONA/3D Objects/Orange DI/DI-Bootcamp/week5/Day4/french_text.txt"
translator= Translator(to_lang="fr")
text ="Text minimal size is over passed"
try:
    with open(input) as f:
        text = f.read(500)
except:
    print("Look again your input file path")

translation = translator.translate(text)
print(translation)

try:
    with open(output,"w") as f:
        f.write(translation)
except:
    print("Look again your output file path")


