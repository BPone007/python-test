n = 10
lis_divizib_pa_2 = [i for i in range(n+1) if i % 2 == 0]
print(lis_divizib_pa_2)


lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print(lis_chenn)


lis_chenn_miniskil = ["kreyasyon", "lis", "chenn"]
lis_chenn_majiskil = [mo.title() for mo in lis_chenn_miniskil]
print(lis_chenn_majiskil)


lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lis_divizib_pa_3 = [lis[i] for i in range(len(lis)) if i % 3 == 0]
print(lis_divizib_pa_3)


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis_tipl = [tuple(lis[i:i+3]) for i in range(0, len(lis), 3)]
print(lis_tipl)

lis = [1, 2, 2, 3, 4, 4, 5]
lis_san_doublon = list(set(lis))
print(lis_san_doublon)


lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_komen = list(set(lis1).intersection(lis2))
print(lis_komen)



lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_distenge = list(set(lis1).symmetric_difference(lis2))
print(lis_distenge)


diksyonè = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_kle = list(diksyonè.keys())
print(lis_kle)

diksyonè = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_valè = list(diksyonè.values())
print(lis_valè)


diksyonè = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
kopi_diksyonè = dict(diksyonè)
print(kopi_diksyonè)


diksyonè = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
nouvo_diksyonè = {kle: f"_{val}_" if isinstance(val, str) else val for kle, val in diksyonè.items()}
print(nouvo_diksyonè)

lis_tipl = [("a", 1), ("b", 2)]
diksyonè = dict(lis_tipl)
print(diksyonè)


diksyonè = {"a": 1, "b": 2}
lis_tipl = list(diksyonè.items())
print(lis_tipl)


diksyonè1 = {"antye": 10, "chenn": "abc", "lis": [1, 2, 3]}
diksyonè2 = {"antye": 5, "chenn": "def", "lis": [4, 5, 6]}

diksyonè_kole = {}
for kle, val1 in diksyonè1.items():
    val2 = diksyonè2.get(kle)
    if isinstance(val1, int):
        diksyonè_kole[kle] = val1 + val2 if val2 is not None else val1
    elif isinstance(val1, (str, list, set)):
        diksyonè_kole[kle] = val1 + val2 if val2 is not None else val1
    else:
        diksyonè_kole[kle] = val1

print(diksyonè_kole)
