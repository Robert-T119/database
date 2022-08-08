import numpy as np

# define useful values
R = 8.31434  # J/mol.K
F = 96484.56  # C/mol

pO2 = 1  # partial pressures, both in atm
pH2 = 1  # for now =1

#at 298k
delta_G_nip2 = -46400
delta_G_nio2 = -453100
delta_G_nio3 = -541800
delta_G_H3cit = -1243400
delta_G_H2cit = -1226300
delta_G_Hcit = -1199200
delta_G_cit3 = -1162700
delta_G_Nicit = -1239906.03
delta_G_NiHcit = -1264425.91
delta_G_NiH2cit = -1282683.44
delta_G_nin6p2 = -250000
delta_G_nin4p2 = -192000
delta_G_n = -26600
delta_G_ng = -16500
delta_G_nhp = -79370
delta_G_OH = -157293
delta_G_w = -237178
delta_G_o2a = 16300
delta_G_o2 = 16300

k1=1.01*(10**(-3))
k2=1.787*(10**(-5))
k3=4.031*(10**(-7))
k4=2.51*(10**(5))
k5=2.00*(10**(3))
k6=5.62*(10**(1))

def R1(x, T): #NI(2+)+ 2e- = Ni
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltah1 = 64000
    delta_G_R1_0 = -delta_G_nip2
    delta_G_R1 = (T*delta_G_R1_0/298)+T*deltah1*((1/T)-(1/298))
    E_theta_1 = -delta_G_R1/(2*F)
    V1 = E_theta_1 + (C2/2)*np.log10(x)
    return V1


def R2(pH, T): #Ni(OH)2 +2H+ +2e- =Ni + 2H2O
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltah2 = -33560
    delta_G_R2_0 = 2*delta_G_w - delta_G_nio2
    delta_G_R2 = (T*delta_G_R2_0/298)+T*deltah2*((1/T)-(1/298))
    E_theta_2 = -delta_G_R2/(2*F)
    V2 = []
    if type(pH) == list:  # for list(vector), below is only for single value
        for pHval in pH:
            V2.append(E_theta_2 - (C2*2*pHval)/2)
    else:
        V2 = E_theta_2 - (C2*2*pH)/2
    return V2


def R3(pH, nhp, nin4p2, T): #Ni(NH3)4(2+) + 4H+ +2e- = Ni + 4NH4+
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltah3 = -530000
    delta_G_R3_0 = 4*delta_G_nhp - delta_G_nin4p2
    delta_G_R3 = (T*delta_G_R3_0/298)+T*deltah3*((1/T)-(1/298))
    E_theta_3 = - delta_G_R3/(2*F)
    V3 = []
    for pHval in pH:
        V3.append(E_theta_3 - (C2*4*pHval/2) - (C2*4*np.log10(nhp)/2) + (C2*np.log10(nin4p2)/2))
    return V3


def R4(pH, nhp, nin6p2, T): #Ni(NH3)+6H+ +2e-=Ni +6NH4+
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltah4 = -795000
    delta_G_R4_0 = 6*delta_G_nhp - delta_G_nin6p2
    delta_G_R4 = (T*delta_G_R4_0/298)+T*deltah4*((1/T)-(1/298))
    E_theta_4 = -delta_G_R4/(2*F)
    V4 = []
    for pHval in pH:
        V4.append(E_theta_4 - (C2*6*pHval/2) - (C2*6*np.log10(nhp)/2) + (C2*np.log10(nin6p2)/2))
    return V4

def R5(n, nin6p2, T): # Ni(NH3)+6H+ +2e- =Ni + 6NH3
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltah6 = -481740
    delta_G_R6_0 = 6*delta_G_n - delta_G_nin6p2
    delta_G_R6 = (T*delta_G_R6_0/298)+T*deltah6*((1/T)-(1/298))
    E_theta_6 = -delta_G_R6/(F*2)
    V6 = E_theta_6 - (C2*6*np.log10(n)/2) + (C2*np.log10(nin6p2)/2)
    return V6

def R6(pH, T, NiH2cit, H3cit): #NiH2cit +H+ +2e = Ni +H3cit
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R2 = delta_G_H3cit - delta_G_NiH2cit
    E_theta_2 = -delta_G_R2/(2*F)
    V2 = []
    if type(pH) == list:  # for list(vector), below is only for single value
        for pHval in pH:
            V2.append(E_theta_2 -(C2*pHval)/2 +(C2*np.log10(NiH2cit))/2 -(C2*np.log10(H3cit))/2)
    else:
        V2 = E_theta_2 -(C2*pH)/2 +(C2*np.log10(NiH2cit))/2 -(C2*np.log10(H3cit))/2
    return V2


def R7(pH, T, NiHcit, H3cit): #NiHcit +2H+ +2e = Ni +H3cit
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R3 = delta_G_H3cit - delta_G_NiHcit
    E_theta_3 = -delta_G_R3/(2*F)
    V3 = []
    for pHval in pH:
        V3.append(E_theta_3 -(C2*2*pHval)/2 +(C2*np.log10(NiHcit))/2 -(C2*np.log10(H3cit))/2)
    return V3


def R8(pH, T, NiHcit, H2cit):  #NiHcit +H+ +2e = Ni +H2cit-
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R4 = delta_G_H2cit - delta_G_NiHcit
    E_theta_4 = -delta_G_R4/(2*F)
    V4 = []
    for pHval in pH:
        V4.append(E_theta_4 -(C2*pHval)/2 +(C2*np.log10(NiHcit))/2 -(C2*np.log10(H2cit))/2)
    return V4


def R9(pH, T, Nicit, H2cit):  #Nicit +2H+ +2e = Ni +H2cit-
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R5 = delta_G_H2cit - delta_G_Nicit
    E_theta_5 = -delta_G_R5/(2*F)
    V5 = []
    for pHval in pH:
        V5.append(E_theta_5 -(C2*2*pHval)/2 +(C2*np.log10(Nicit))/2 -(C2*np.log10(H2cit))/2)
    return V5


def R10(pH, T, Nicit, Hcit):  #Nicit +H+ +2e = Ni +Hcit-
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R6 = delta_G_Hcit - delta_G_Nicit
    E_theta_6 = -delta_G_R6/(2*F)
    V6 = []
    for pHval in pH:
        V6.append(E_theta_6 -(C2*pHval)/2 +(C2*np.log10(Nicit))/2 -(C2*np.log10(Hcit))/2)
    return V6


def R11(T, Nicit, cit3):  #Nicit +2e = Ni +cit3-
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R7 = delta_G_cit3 - delta_G_Nicit
    E_theta_7 = -delta_G_R7/(2*F)
    V7 = E_theta_7 +(C2*np.log10(Nicit))/2 -(C2*np.log10(cit3))/2
    return V7


def R12(pH,T):  #Nio2 +2H+ +2e = Ni+ 2H2O
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    delta_G_R8 = 2*delta_G_w - delta_G_nio2
    E_theta_8 = -delta_G_R8/(2*F)
    V8 = []
    if type(pH) == list:  # for list(vector), below is only for single value
        for pHval in pH:
            V8.append(E_theta_8 - (C2 * 2 * pHval) / 2)
    else:
        V8 = E_theta_8 -(C2*2*pH) / 2
    return V8


def T1(nip2, pH, T): #Ni(OH)3 +3H+ +e- =Ni(2+) +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltaht1 = -243290
    delta_G_T1_0 = 3*delta_G_w + delta_G_nip2 - delta_G_nio3
    delta_G_T1 = (T*delta_G_T1_0/298)+T*deltaht1*((1/T)-(1/298))
    E_theta_T1 = -delta_G_T1/(F)
    if type(pH) == list:
        vt1 = []
        for pHval in pH:
            vt1.append(E_theta_T1 - C2*np.log10(nip2) - C2*3*pHval)
    else:
        vt1 = E_theta_T1 - C2*np.log10(nip2) - C2*3*pH
    return vt1


def T2(pH, T): #Ni(OH)3 +H+ +e- =Ni(OH)2 +H2O
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltaht2 = -145730
    delta_G_T2_0 = delta_G_nio2 + delta_G_w - delta_G_nio3
    delta_G_T2 = (T*delta_G_T2_0/298)+T*deltaht2*((1/T)-(1/298))
    E_theta_T2 = -delta_G_T2/F
    if type(pH) == list:
        vt2 = []
        for pHval in pH:
            vt2.append(E_theta_T2 - (C2*1*pHval)/1)
    else:
        vt2 = E_theta_T2 - (C2*1*pH)/1
    return vt2


def T3(nhp, nin4p2, pH, T): #Ni(OH)3 +4NH4+ +e- =Ni(Nh3)4(2+) +3H2O +H+
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltaht3 = 350710
    delta_G_T3_0 = 3*delta_G_w + delta_G_nin4p2 - 4*delta_G_nhp - delta_G_nio3
    delta_G_T3 = (T*delta_G_T3_0/298)+T*deltaht3*((1/T)-(1/298))
    E_theta_T3 = - delta_G_T3/F
    if type(pH) == list:
        vt3 = []
        for pHval in pH:
            vt3.append(E_theta_T3 + C2*pHval + C2*4*np.log10(nhp) - C2*np.log10(nin4p2))
    else:
        vt3 = E_theta_T3 + C2*pH + C2*4*np.log10(nhp) - C2*np.log10(nin4p2)
    return vt3


def T4(pH, nhp, nin6p2, T): #Ni(OH)3 +6NH4+ +e- =Ni(Nh3)6(2+) +3H2O +H+
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltaht4 = 615710
    delta_G_T4_0 = 3*delta_G_w + delta_G_nin6p2 - 6*delta_G_nhp - delta_G_nio3
    delta_G_T4 = (T*delta_G_T4_0/298)+T*deltaht4*((1/T)-(1/298))
    E_theta_T4 = -delta_G_T4/F
    if type(pH) == list:
        vt4 = []
        for pHval in pH:
            vt4.append(E_theta_T4 + C2*3*pHval + C2*6*np.log10(nhp) - C2*np.log10(nin6p2))
    else:
        vt4 = E_theta_T4 + C2*3*pH + C2*6*np.log10(nhp) - C2*np.log10(nin6p2)
    return vt4


def T5(n, pH, nin6p2, T): #Ni(OH)3 +6NH3 +3H +e- =Ni(Nh3)6(2+) +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltaht5 = 302450
    delta_G_T5_0 = 3*delta_G_w + delta_G_nin6p2 - 6*delta_G_n - delta_G_nio3
    delta_G_T5 = (T*delta_G_T5_0/298)+T*deltaht5*((1/T)-(1/298))
    E_theta_T5 = -delta_G_T5/F
    if type(pH) == list:
        vt5 = []
        for pHval in pH:
            vt5.append(E_theta_T5 + 6*C2*np.log10(n) - 3*C2*pHval - C2*np.log10(nin6p2))
    else:
        vt5 = E_theta_T5 + 6*C2*np.log10(n) - 3*C2*pH - C2*np.log10(nin6p2)
    return vt5


def T6(pH,NiH2cit,H3cit,T): #Ni(OH)3 +H3cit +2H +e- =NiH2cit+ +3H2O
    C1 = -np.log(10) * R * T
    C2 = -C1 / F
    delta_G_T2 = delta_G_NiH2cit + 3*delta_G_w - delta_G_H3cit - delta_G_nio3
    E_theta_T2 = -delta_G_T2/F
    if type(pH) == list:
        vt2 = []
        for pHval in pH:
            vt2.append(E_theta_T2 +C2*np.log10(H3cit)-C2*2*pHval-C2*np.log10(NiH2cit))
    else:
        vt2 = E_theta_T2 +C2*np.log10(H3cit)-C2*2*pH-C2*np.log10(NiH2cit)
    return vt2


def T7(pH,NiHcit,H3cit,T): #Ni(OH)3 +H3cit +H +e- =NiHcit+ +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T3 = delta_G_NiHcit + 3*delta_G_w - delta_G_H3cit - delta_G_nio3
    E_theta_T3 = -delta_G_T3/F
    if type(pH) == list:
        vt3 = []
        for pHval in pH:
            vt3.append(E_theta_T3 +C2*np.log10(H3cit)-C2*pHval-C2*np.log10(NiHcit))
    else:
        vt3 = E_theta_T3 +C2*np.log10(H3cit)-C2*pH-C2*np.log10(NiHcit)
    return vt3


def T8(pH,NiHcit,H2cit,T): #Ni(OH)3 +H2cit +2H +e- =NiHcit +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T4 = delta_G_NiHcit + 3*delta_G_w - delta_G_H2cit - delta_G_nio3
    E_theta_T4 = -delta_G_T4/F
    if type(pH) == list:
        vt4 = []
        for pHval in pH:
            vt4.append(E_theta_T4 +C2*np.log10(H2cit)-C2*2*pHval-C2*np.log10(NiHcit))
    else:
        vt4 = E_theta_T4 +C2*np.log10(H2cit)-C2*2*pH-C2*np.log10(NiHcit)
    return vt4


def T9(pH,Nicit,H2cit,T): #Ni(OH)3 +H2cit +H +e- =Nicit +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T5 = delta_G_Nicit + 3*delta_G_w - delta_G_H2cit - delta_G_nio3
    E_theta_T5 = -delta_G_T5/F
    if type(pH) == list:
        vt5 = []
        for pHval in pH:
            vt5.append(E_theta_T5 +C2*np.log10(H2cit)-C2*pHval-C2*np.log10(Nicit))
    else:
        vt5 = E_theta_T5 +C2*np.log10(H2cit)-C2*pH-C2*np.log10(Nicit)
    return vt5


def T10(pH,Nicit,Hcit,T): #Ni(OH)3 +Hcit +2H +e- =Nicit +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T6 = delta_G_Nicit + 3*delta_G_w - delta_G_Hcit - delta_G_nio3
    E_theta_T6 = -delta_G_T6/F
    if type(pH) == list:
        vt6 = []
        for pHval in pH:
            vt6.append(E_theta_T6 +C2*np.log10(Hcit)-C2*2*pHval-C2*np.log10(Nicit))
    else:
        vt6 = E_theta_T6 +C2*np.log10(Hcit)-C2*2*pH-C2*np.log10(Nicit)
    return vt6

def T11(pH,Nicit,cit3,T): #Ni(OH)3 +cit3 +3H +e- =Nicit +3H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T7 = delta_G_Nicit + 3*delta_G_w - delta_G_cit3- delta_G_nio3
    E_theta_T7 = -delta_G_T7/F
    if type(pH) == list:
        vt7 = []
        for pHval in pH:
            vt7.append(E_theta_T7 +C2*np.log10(cit3)-C2*3*pHval-C2*np.log10(Nicit))
    else:
        vt7 = E_theta_T7 +C2*np.log10(cit3)-C2*3*pH-C2*np.log10(Nicit)
    return vt7

def T12(pH,T): #Ni(OH)3 +H +e- =Ni02 +H2O
    C1 = -np.log(10)*R*T
    C2 = -C1 / F
    delta_G_T8 = delta_G_nio2 + delta_G_w -delta_G_nio3
    E_theta_T8 = -delta_G_T8/F
    if type(pH) == list:
        vt8 = []
        for pHval in pH:
            vt8.append(E_theta_T8 -C2*pHval)
    else:
        vt8 = E_theta_T8 -C2*pH
    return vt8

def W1(pH, T): #O2+ 4H+ +4e- =2H20
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    deltahw1 = -571660
    delta_G_W1_0 = 2*delta_G_w
    delta_G_W1 = (T*delta_G_W1_0/298)+T*deltahw1*((1/T)-(1/298))
    E_theta_W1 = -delta_G_W1/(4*F)
    VW1 = []
    for pHval in pH:
        VW1.append(E_theta_W1 - (C2*4*pHval/4) + (C2*1*np.log10(pO2)/4))
    return VW1


def W2(pH, T):   #2H+ 2e- = H2
    C1 = -np.log(10)*R*T
    C2 = -C1/F
    VW2 = []
    for pHval in pH:
        VW2.append(-(C2*2*pHval/2) - (C2*1/2))
    return VW2
