import time 

time.sleep(2)
nota1 = int(input("Digite sua nota da primeira avaliação: "))
time.sleep(1)
nota2 = int(input("Digite sua nota da segunda avaliação: "))
time.sleep(1)
nota3 = int(input("Digite sua nota da terceira avaliação: "))
time.sleep(1)
nota4 = int(input("Digite sua nota da quarta avaliação: "))
time.sleep(1)
print("Calculando as suas notas...")
time.sleep(2)

multi1 = nota1 * 2
multi2 = nota2 * 3
multi3 = nota3 * 2
multi4 = nota4 * 3

s = multi1 + multi2 + multi3 + multi4

if s <= 50:
    print("Você não passou 😭")

if s >= 50:
    print("Você passou, Parabéns 😄")

if s == 50:
    print("Você passou, Parabéns 😄")
    
time.sleep(3)
    
