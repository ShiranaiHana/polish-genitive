!DOCTYPE html
html lang=en
head
    meta charset=UTF-8
    titlePolish Genitive Quiztitle
    link rel=stylesheet href=httpspyscript.netlatestpyscript.css
    script defer src=httpspyscript.netlatestpyscript.jsscript
head
body
    h1🇵🇱 Polish Genitive Quizh1
    py-script
import random

# ---------- QUIZ DATA ----------
singular = [
    {word książki, meaning of the book, explanation Feminine nouns often end in -a-ka → -i in genitive singular.},
    {word matki, meaning of the mother, explanation Feminine noun ending -a → -i},
    {word szkoły, meaning of the school, explanation Feminine noun ending -a → -y-i},
    {word rzeki, meaning of the river, explanation Feminine noun ending -a → -i},
    {word torby, meaning of the bag, explanation Feminine noun ending -a → -y-i},
    {word kobiety, meaning of the woman, explanation Feminine noun ending -a → -y-i},
    {word herbaty, meaning of the tea, explanation Feminine noun ending -a → -y-i},
    {word kolegi, meaning of the colleaguefriend, explanation Masculine personal nouns ending in -a → -i},
    {word przyjaciela, meaning of the friend, explanation Masculine personal nouns add -a},
    {word wujka, meaning of the uncle, explanation Masculine nouns add -a},
    {word chłopca, meaning of the boy, explanation Masculine personal nouns ending -iec → -ca},
    {word przyrodnika, meaning of the naturalistscientist, explanation Masculine nouns add -a},
    {word mężczyzny, meaning of the man, explanation Masculine personal nouns ending -a → -y},
    {word króla, meaning of the king, explanation Masculine nouns add -a},
    {word dyrektora, meaning of the director, explanation Masculine nouns add -a},
    {word biskupa, meaning of the bishop, explanation Masculine nouns add -a},
    {word senatora, meaning of the senator, explanation Masculine nouns add -a},
    {word lekarza, meaning of the doctor, explanation Masculine nouns add -a},
    {word dziecka, meaning of the child, explanation Neuter nouns add -a in genitive singular},
    {word jabłka, meaning of the apple, explanation Neuter nouns add -a in genitive singular},
    {word mleka, meaning of the milk, explanation Neuter nouns add -a in genitive singular},
    {word zwierzęcia, meaning of the animal, explanation Neuter nouns add -a},
    {word zwierzątka, meaning of the little animal, explanation Neuter diminutive nouns add -a},
    {word okna, meaning of the window, explanation Neuter nouns add -a},
    {word muzeum, meaning of the museum, explanation Neuter nouns unchanged or add -u},
    {word lata, meaning of the year, explanation Neuter nouns add -a},
    {word źródła, meaning of the source, explanation Neuter nouns add -a},
    {word królestwa, meaning of the kingdom, explanation Neuter nouns add -a},
    {word imienia, meaning of the name, explanation Neuter nouns add -a},
    {word pomieszczenia, meaning of the room, explanation Neuter nouns add -a},
    {word owocu, meaning of the fruit, explanation Neuter nouns add -u}
]

# Plural forms (simplified examples, adjust as needed)
plural = [
    {word książek, meaning of the books, explanation Feminine plural nouns end in -ek in genitive plural},
    {word matek, meaning of the mothers, explanation Feminine plural nouns end in -ek},
    {word szkół, meaning of the schools, explanation Feminine plural nouns -a → -ów},
    {word rzek, meaning of the rivers, explanation Feminine plural nouns -a → -ów},
    {word torb, meaning of the bags, explanation Feminine plural nouns -a → -},
    {word kobiet, meaning of the women, explanation Feminine plural nouns -a → -},
    {word herbat, meaning of the teas, explanation Feminine plural nouns -a → -},
    {word kolegów, meaning of the colleagues, explanation Masculine personal plural nouns -i → -ów},
    {word przyjaciół, meaning of the friends, explanation Masculine personal plural -e → -ów},
    {word wujków, meaning of the uncles, explanation Masculine plural -ek → -ów},
    {word chłopców, meaning of the boys, explanation Masculine personal plural -iec → -ców},
    {word przyrodników, meaning of the naturalists, explanation Masculine plural add -ów},
    {word mężczyzn, meaning of the men, explanation Masculine personal plural irregular},
    {word królów, meaning of the kings, explanation Masculine plural add -ów},
    {word dyrektorów, meaning of the directors, explanation Masculine plural add -ów},
    {word biskupów, meaning of the bishops, explanation Masculine plural add -ów},
    {word senatorów, meaning of the senators, explanation Masculine plural add -ów},
    {word lekarzy, meaning of the doctors, explanation Masculine plural add -y-i},
    {word dzieci, meaning of the children, explanation Neuter plural irregular},
    {word jabłek, meaning of the apples, explanation Neuter plural add -ek},
    {word mlek, meaning of the milks, explanation Neuter plural add -ek},
    {word zwierząt, meaning of the animals, explanation Neuter plural add -},
    {word zwierzątek, meaning of the little animals, explanation Neuter diminutive plural},
    {word okien, meaning of the windows, explanation Neuter plural add -en},
    {word muzeów, meaning of the museums, explanation Neuter plural add -ów},
    {word lat, meaning of the years, explanation Neuter plural add -},
    {word źródeł, meaning of the sources, explanation Neuter plural add -},
    {word królestw, meaning of the kingdoms, explanation Neuter plural add -},
    {word imion, meaning of the names, explanation Neuter plural irregular},
    {word
