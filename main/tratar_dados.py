import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\aluno noturno\Desktop\grupo03\Arquivo-trabalho\Documento-Limpo-grupo03.csv', delimiter=',', encoding='UTF-8')

# tambaqui, pacu, tambacu, tilápia e pirarucu sobrevivem em um intervalo relativamente grande de temperatura
# (de 80C - 100C, até cerca de 400C - 450C).
# Entretanto, a temperatura ótima para o crescimento dessas espécies situa-se entre 250C e 320C.

# Para um ótimo crescimento e desempenho de peixes tropicais 
# (tambaqui, pacu, Etc.)
# é desejável uma concentração de OD na água maior que 5 mg/l

# Dias nublados, onde a incidência de luz sobre os viveiros é menor, 
# também fazem com que a quantidade de oxigênio produzido seja menor. 

# pH geralmente variam entre 4 e 8. O meio é considerado ideal quando o pH está na faixa entre 6,5 e 7,5. 
# Vários fatores afetam o pH da água dos viveiros de piscicultura: tipo de solo, concentração de dióxido de carbono, 
# condições climáticas, etc.

# Valores de alcalinidade menores que 20 mg/l são considerados baixos e acima deste valor, satisfatórios. 
# O solo é o fator que mais influencia na alcalinidade das águas. Solos pobres e ácidos tendem a ter baixas alcalinidades.

# O calcário agrícola, calcítico ou magnesiano, 
# é preferido por se solubilizar lentamente e não elevar o pH a um valor maior que 8,3. 
# A quantidade do material a ser usada na calagem depende do tipo de solo.

# A concentração da forma tóxica aumenta com a elevação do pH e da temperatura. 
# Concentração acima de 0,01 mg/l passa a afetar o crescimento e a resistência a doenças. 
# O único tratamento economicamente eficiente para reduzir níveis de amônia em viveiros é a renovação de água.

# no geral, bons resultados na produção são
# alcançados em temperaturas da água entre 26 e 30°C, podendo variar de espécie para espécie.

# Meça a temperatura usando um termômetro ou aparelho
# digital pela manhã (6 h) e à tarde (17 h)