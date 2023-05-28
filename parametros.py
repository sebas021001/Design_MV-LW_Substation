import numpy as np

#Para el trafo de 1500 KVA
R_1500 = 0.80
X_1500 = 5.50
S_1500 = 1500
#Para el trafo de 2500KVA
R_2500 = 0.72
X_2500 = 5.51
S_2500 = 2500
#Para el trafo de 2000KVA
S_2000 = 2000
#Funcion para interpolar datos
def interpolate_value(x1, y1, x2, y2, x):
    y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return y

# Interpolación de R
R_2000_por = interpolate_value(S_1500, R_1500, S_2500, R_2500, S_2000)

# Interpolación de X
X_2000_por = interpolate_value(S_1500, X_1500, S_2500, X_2500, S_2000)

R_2000 = R_2000_por/100
X_2000 = X_2000_por/100


def impedancias_entrelazadas(resistencia, reactancia):
    Z_he = 0.5*resistencia + 0.8*reactancia*1j
    Z_le = resistencia + 0.4*reactancia*1j
    Z_te = resistencia + 0.4*reactancia*1j
    impedancias = np.array([[Z_he], [Z_le], [Z_te]])
    return impedancias


def impedancias_noentrelazadas(resistencia, reactancia):
    Z_hn = 0.25*resistencia - 0.6*reactancia*1j
    Z_ln = 1.5*resistencia + 3.3*reactancia*1j
    Z_tn = 1.5*resistencia + 3.1*reactancia*1j
    impedancias = np.array([[Z_hn], [Z_ln], [Z_tn]])
    return impedancias

imp_2000_entre = impedancias_entrelazadas(R_2000, X_2000)
imp_2000_noentre = impedancias_noentrelazadas(R_2000, X_2000)
print(imp_2000_entre)
print()
print(imp_2000_noentre)