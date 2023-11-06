chenn = "tout rèv ayisyen c ale Biden"
chenn_miniskil = chenn.lower()
print(chenn_miniskil)


chenn = "tout rèv ayisyen c ale Biden."
chenn_koupe = chenn.split()
print(chenn_koupe)


chenn = "tout rèv ayisyen c ale Biden."
chenn_majiskil = chenn.title()
print(chenn_majiskil)


chenn = "tout rèv ayisyen c ale Biden"
chenn_ranplase = chenn.replace("a", "@")
print(chenn_ranplase)


chenn = "Ayiti"
chenn_nouvo = chenn[::-1].upper()
print(chenn_nouvo)


chenn = "Ayiti pap peri"
endeks = chenn.index("a")
print(endeks)

chenn = "Ayiti pap peri"
total_endeks = [i for i, char in enumerate(chenn) if char.lower() == 'a']
print(len(total_endeks))

chenn = "Ayiti pap peri"
endeks_miniskil = [i for i, char in enumerate(chenn) if char == 'a']
print(endeks_miniskil)

chenn = "Ayiti pap peri."
chenn_sans_espas = chenn.replace(" ", "")
print(chenn_sans_espas)
