num_multi = 11,7,9,8,15,25,67,95,74

def multi(*args):
    total = 1
    for num in num_multi:
        total *= num
    return total

res_multi = multi(num_multi)

print(res_multi)

num_verif = input('Digite um numero :')

def verif_par_impar(x):
    num = int(x) % 2
    if num :
        print(x,' é um numero impar !!!')
    else:
        print(x,' é um numero par !!!')
        

res_par_impar = verif_par_impar(num_verif)