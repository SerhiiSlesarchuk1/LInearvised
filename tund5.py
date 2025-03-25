def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Kui sisend ei ole järjendis[+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisenud ujukomaarvu tüübina
    :param float arv2: Sisenud ujukomaarvu tüübina
    :param str tehe: Sisenud listist [+,-,/,*]
    :rtype: varMääramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
     Tagastab True, kui aasta on liigaasta js False kui aasta on tavaline aasta
    :param int aasta: Sisenud kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v