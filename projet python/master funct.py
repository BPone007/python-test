import random
import string
import re

def envèse_mo(mo):
    mo_envèse = mo[::-1]
    return mo_envèse

mo = "python"
resultat = envèse_mo(mo)
print(resultat)



def kòd_aleyatwa(n):
    kòd = ''.join(random.choice(string.ascii_letters) for _ in range(n))
    return kòd

n = 10
resultat = kòd_aleyatwa(n)
print(resultat)


def kòd_aleyatwa_san_repetisyon(n):
    kòd = ''.join(random.sample(string.ascii_letters, n))
    return kòd

n = 10
resultat = kòd_aleyatwa_san_repetisyon(n)
print(resultat)



def kòd_aleyatwa_alafanimerik(n):
    karaktè_alafanimerik = string.ascii_letters + string.digits
    kòd = ''.join(random.sample(karaktè_alafanimerik, n))
    return kòd

n = 12
resultat = kòd_aleyatwa_alafanimerik(n)
print(resultat)


def jenere_slug(chenn):
    chenn_san_akseptab = re.sub(r'[^a-zA-Z0-9-]', '', chenn)
    slug = '-'.join(chenn_san_akseptab.split())
    return slug.lower()

chenn = "berlin bon bagay"
resultat = jenere_slug(chenn)
print(resultat)


def separe_let_ak_vijil(mo, vijil):
    mo_separe = vijil.join(mo)
    return mo_separe

mo = "Python"
vijil = "-"
resultat = separe_let_ak_vijil(mo, vijil)
print(resultat)


def kripte_mo(mo):
    mo_kripte = '-'.join(str(ord(let)) for let in mo)
    return mo_kripte

mo = "ALO"
resultat = kripte_mo(mo)
print(resultat)


def dekripte_mo(mo_kripte):
    mo_dekripte = ''.join(chr(int(karakter)) for karakter in mo_kripte.split('-'))
    return mo_dekripte

mo_kripte = "0-11-14"
resultat = dekripte_mo(mo_kripte)
print(resultat)


def retounen_tuple(paramèt1, paramèt2):
    return (paramèt1, paramèt2)

valè1 = "123"
valè2 = "126"
resultat = retounen_tuple(valè1, valè2)
print(resultat)


