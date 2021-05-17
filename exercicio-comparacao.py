print('Quanto tempo leva para o país A ultrapassar o país B em número populacional ?')

paisA = 80000
paisB = 200000
ano = 0

while paisA < paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    ano+=1
    if paisA >= paisB:
        print(f'Em {ano} anos o País A que tinha 80.000 habitantes, passou a ter {paisA:.2f} habitantes.\nE o País B que tinha 200.000 habitantes, passou a ter {paisB:.2f} habitantes.')
