import time 

print("""

                                                                                                                                                    
                                                                                                                                                    
NNNNNNNN        NNNNNNNN                          tttt                                                                                              
N:::::::N       N::::::N                       ttt:::t                                                                                              
N::::::::N      N::::::N                       t:::::t                                                                                              
N:::::::::N     N::::::N                       t:::::t                                                                                              
N::::::::::N    N::::::N   ooooooooooo   ttttttt:::::ttttttt      aaaaaaaaaaaaa      ssssssssss           ppppp   pppppppppyyyyyyy           yyyyyyy
N:::::::::::N   N::::::N oo:::::::::::oo t:::::::::::::::::t      a::::::::::::a   ss::::::::::s          p::::ppp:::::::::py:::::y         y:::::y 
N:::::::N::::N  N::::::No:::::::::::::::ot:::::::::::::::::t      aaaaaaaaa:::::ass:::::::::::::s         p:::::::::::::::::py:::::y       y:::::y  
N::::::N N::::N N::::::No:::::ooooo:::::otttttt:::::::tttttt               a::::as::::::ssss:::::s        pp::::::ppppp::::::py:::::y     y:::::y   
N::::::N  N::::N:::::::No::::o     o::::o      t:::::t              aaaaaaa:::::a s:::::s  ssssss          p:::::p     p:::::p y:::::y   y:::::y    
N::::::N   N:::::::::::No::::o     o::::o      t:::::t            aa::::::::::::a   s::::::s               p:::::p     p:::::p  y:::::y y:::::y     
N::::::N    N::::::::::No::::o     o::::o      t:::::t           a::::aaaa::::::a      s::::::s            p:::::p     p:::::p   y:::::y:::::y      
N::::::N     N:::::::::No::::o     o::::o      t:::::t    tttttta::::a    a:::::assssss   s:::::s          p:::::p    p::::::p    y:::::::::y       
N::::::N      N::::::::No:::::ooooo:::::o      t::::::tttt:::::ta::::a    a:::::as:::::ssss::::::s         p:::::ppppp:::::::p     y:::::::y        
N::::::N       N:::::::No:::::::::::::::o      tt::::::::::::::ta:::::aaaa::::::as::::::::::::::s  ......  p::::::::::::::::p       y:::::y         
N::::::N        N::::::N oo:::::::::::oo         tt:::::::::::tt a::::::::::aa:::as:::::::::::ss   .::::.  p::::::::::::::pp       y:::::y          
NNNNNNNN         NNNNNNN   ooooooooooo             ttttttttttt    aaaaaaaaaa  aaaa sssssssssss     ......  p::::::pppppppp        y:::::y           
                                                                                                           p:::::p               y:::::y            
                                                                                                           p:::::p              y:::::y             
                                                                                                          p:::::::p            y:::::y              
                                                                                                          p:::::::p           y:::::y               
                                                                                                          p:::::::p          yyyyyyy                
                                                                                                          ppppppppp                                 
                                                                                                                                                    
""")


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
    
