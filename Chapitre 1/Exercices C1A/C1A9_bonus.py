# En sachant que les fréquences des notes suivantes :
# Do = 130
# Ré = 146
# Mi = 164
# Fa = 174
# Sol = 196
# La = 220
# Si = 246
# Sol (grave) = 98
# Essayez de reproduire frère jacques avec la fonction winsound.Beep(), Les notes composants frères jacques sont:
# Do Ré Mi Do Do Ré Mi Do Mi Fa Sol Mi Fa Sol Sol la Sol Fa Mi Do Sol La Sol Fa Mi Do Do Sol(grave) Do Do Sol(grave) Do
# Pour faire un silence, utilisez la fréquence la plus basse possible de la fonction Beep, essayez de régler
# la durée des notes pour que ça sonne le mieux ! (Si vous vous connaissez en musique, n'hésitez pas à 
# réaliser une autre musique à la place de frère jacques !)

import winsound 

do = 130 
re = 146 
mi = 164 
fa = 174 
sol = 196
la = 220 
si = 246 
sol2 = 96

blanche = 500
noire = 250
croche = 125

melody = [do, re, mi, do, do, re, mi, do, mi, fa, sol, mi, fa, sol, sol, la, sol, fa, mi, do, sol, la, sol, fa, mi, do, do, sol2, do, do, sol2, do]
duration = [noire, noire, noire, noire, noire, noire,noire,noire, noire,noire, blanche, noire, noire, blanche, croche, croche,croche, croche,croche, noire, croche, croche,croche,croche,croche, noire, noire, noire, blanche, noire, noire, blanche]


i = 0 
for item in melody :
    winsound.Beep(item,duration[i])
    i += 1