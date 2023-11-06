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


lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]
lis_reyini = list(set(lis1 + lis2 + lis3))
print(lis_reyini)
