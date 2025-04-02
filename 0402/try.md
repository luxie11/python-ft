### **Užduotis 1: Klaidų suvaldymas naudojant `try-except`**  
Parašykite Python programą, kuri paprašytų vartotojo įvesti du skaičius ir juos sudaugintų.  
- Jei vartotojas įveda ne skaičių, turi būti sugauta `ValueError` klaida ir išspausdintas atitinkamas pranešimas.  
- Jei vartotojas įveda neigiamą skaičių, turi būti sugauta `ValueError` klaida su pranešimu „Neigiami skaičiai neleidžiami“.  

 **Papildoma užduotis**: Naudokite `finally` bloką, kuris visada išspausdins „Programa baigė darbą“.  

---

### **Užduotis 2: `raise` naudojimas patikrinant duomenis**  
Sukurkite funkciją `tikrink_amziu(amzius: int)`, kuri:  
- Jei `amzius` nėra sveikas skaičius, iššauks `TypeError` klaidą.  
- Jei `amzius` yra mažesnis nei 18, iššauks `ValueError` klaidą su pranešimu „Amžius per mažas“.  
- Jei `amzius` tinkamas, išspausdins „Amžius tinkamas registracijai“.  

 **Papildoma užduotis**: Naudokite `try-except` bloką, kad sugautumėte klaidas ir atspausdintumėte atitinkamus pranešimus.