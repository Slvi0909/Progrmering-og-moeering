#Bytt alle else i gjettingene med if 2


opplysninger=[] #Lager en tom liste for å samle på opplysninger

def intervju():
    print("Velkommen til spillet. Du er en politietterforsker og har fått i oppgave å løse et mordmysterium. Mordet fant sted i Belltown kl 12 5.november. Det er to mistenkte, det er Petter og Jonas. Du skal nå intervjue dem for å samle opplysninger.vi har fått hint fra sivile om at en peron med rødt skjerf har blitt sett like ved åstedet rundt 11.50. Hvem vil du intervjue først?")
    print("1, Jonas")
    print("2,Petter")
    print("3, orker ikke mere")
    valg=int(input())
    return valg

def intervju2():
    print("Hvilket spørsmål ønsker du å stille?")
    print("1,hvor var du kl 12 en 5.november?")
    print("2, Hva hadde du på deg den kvelden?")
    valg2=int(input())
    return valg2

def orker_ikke_mer():
    print("Du tapte")

def hva_vil_du_gjøre():
    print("Hva vil du gjøre nå")
    print("1,Gjette hvem som er morderen.")
    print("2,Gi opp")
    print("3, Intervjue Jonas") #Jobb med å lage
    print("4,Intervjue petter") #Jobb med å lage
    valg3=int(input())
    return valg3

def gjett_morderen():
    print("Hvem tror du er morderen?")
    print("1, Jonas")
    print("2,Petter")
    gjett=int(input())
    return gjett
    
game=True

while game:
    valg=intervju()
    if valg==1: #velger å intervjue Jonas
        valg2=intervju2()
        if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Jonas. 
            print("Jeg var på nattklubben som heter del Rey.")
            opplysninger.append("Jonas var på nattklubben som heter del Rey da mordet skjedde.")
            valg3=hva_vil_du_gjøre()
            if valg3==1: #Velger å gjette hvem som er morderen
                print("Dine opplysninger som du har samlet er:", opplysninger)
                gjett=gjett_morderen()  #funskjon for å gjette
                if gjett==1: #Gjetter Jonas
                    print("gratulerer du løste myssteriet, Jonas var morderen.")
                    game=False
                if gjett==2:   #Bare tester her bytt tilbake til else
                    print("Du tapte, prøv å spille på nytt")
            if valg3==2: #velger å gi opp
                print("Du tapte")
                game=False
            if valg3==3:  #vil intervjue jonas en gang til
                valg2=intervju2()
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Jonas. 
                    print("Jeg var på nattklubben som heter del Rey.")
                    opplysninger.append("Jonas var på nattklubben som heter del Rey da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
                if valg2==2:  #velger å stille spørsmålet: Hva hadde du på deg den kvellden, til Jonas.
                    print("Jeg hadde på meg en brun jakke, jeans og et rødt skjerf.")
                    opplysninger.append("Jonas hadde på seg en brun jakke, jeans og et rødt skjerf kvelden mordet skjedde.") 
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
            if valg3==4: #vil intervjue Petter som person 2
                valg2=intervju2()   
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Petter
                    print("Jeg var sammen med kjæresten min")
                    opplysninger.append("Petter var med kjæresten sin da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte,prøv å spille på nytt")
                if valg2==2: #velger å stille spørsmålet: Hva hadde du på deg den kvelden, til Petter
                    print("Jeg hadde på meg en sort jakke, jeans og en blå lue")
                    opplysninger.append("Petter hadde på seg en sort jakke, jeans og en blå lue.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")    
        if valg2==2: #velger å stille spørsmålet: Hva hadde du på deg den kvellden, til Jonas.
            print("Jeg hadde på meg en brun jakke, jeans og et rødt skjerf.")
            opplysninger.append("Jonas hadde på seg en brun jakke, jeans og et rødt skjerf kvelden mordet skjedde.")
            valg3=hva_vil_du_gjøre()
            if valg3==1: #Velger å gjette hvem som er morderen
                print("Dine opplysninger som du har samlet er:", opplysninger)
                gjett=gjett_morderen()  #funskjon for å gjette
                if gjett==1: #Gjetter Jonas
                    print("gratulerer du løste myssteriet, Jonas var morderen.")
                    game=False
                if gjett==2: #Gjetter petter
                    print("Du tapte, prøv å spille på nytt")
            if valg3==2: #velger å gi opp
                print("Du tapte")
            game=False
            if valg3==3: #intervjue Jonas gang nr 2 ikke fulført enda
                valg2=intervju2()
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Jonas. 
                    print("Jeg var på nattklubben som heter del Rey.")
                    opplysninger.append("Jonas var på nattklubben som heter del Rey da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt") 
                if valg2==2:  #velger å stille spørsmålet: Hva hadde du på deg den kvellden, til Jonas.
                    print("Jeg hadde på meg en brun jakke, jeans og et rødt skjerf.")
                    opplysninger.append("Jonas hadde på seg en brun jakke, jeans og et rødt skjerf kvelden mordet skjedde.") 
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
            if valg3==4: #vil intervjue Petter som person 2
                valg2=intervju2()   
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Petter
                    print("Jeg var sammen med kjæresten min")
                    opplysninger.append("Petter var med kjæresten sin da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")  
                if valg2==2: #velger å stille spørsmålet: Hva hadde du på deg den kvelden, til Petter
                    print("Jeg hadde på meg en sort jakke, jeans og en blå lue")
                    opplysninger.append("Petter hadde på seg en sort jakke, jeans og en blå lue.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
            
    if valg==2: #velger å intervjue Petter (legg inn på samme måte som i valg==1 for intervju runde 2)
       valg2=intervju2() 
       if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Petter
           print("Jeg var sammen med kjæresten min")
           opplysninger.append("Petter var med kjæresten sin da mordet skjedde.")
           valg3=hva_vil_du_gjøre() #bygge ut  for if valg3==3/4
           if valg3==1: #Velger å gjette hvem som er morderen
                print("Dine opplysninger som du har samlet er:", opplysninger)
                gjett=gjett_morderen()  #funskjon for å gjette
                if gjett==1: #Gjetter Jonas
                    print("gratulerer du løste myssteriet, Jonas var morderen.")
                    game=False
                if gjett==2: #Gjetter Petter
                    print("Du tapte, prøv å spille på nytt")
           if valg3==2: #velger å gi opp
                print("Du tapte")
                game=False
           if valg3==3:  #vil intervjue jonas som person 2
                valg2=intervju2()
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Jonas. 
                    print("Jeg var på nattklubben som heter del Rey.")
                    opplysninger.append("Jonas var på nattklubben som heter del Rey da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
                if valg2==2:  #velger å stille spørsmålet: Hva hadde du på deg den kvellden, til Jonas.
                    print("Jeg hadde på meg en brun jakke, jeans og et rødt skjerf.")
                    opplysninger.append("Jonas hadde på seg en brun jakke, jeans og et rødt skjerf kvelden mordet skjedde.") 
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:  
                        print("Du tapte, prøv å spille på nytt") 
           if valg3==4: #vil intervjue Petter som person 2
                valg2=intervju2()   
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Petter
                    print("Jeg var sammen med kjæresten min")
                    opplysninger.append("Petter var med kjæresten sin da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")   
                if valg2==2: #velger å stille spørsmålet: Hva hadde du på deg den kvelden, til Petter
                    print("Jeg hadde på meg en sort jakke, jeans og en blå lue")
                    opplysninger.append("Petter hadde på seg en sort jakke, jeans og en blå lue.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
       if valg2==2: #velger å stille spørsmålet:Hva hadde du på deg den kvelden, til Petter?
           print("Jeg hadde på meg en sort jakke, jeans og en blå lue.")
           opplysninger.append("Petter hadde på seg en sort jakke, jeans og en blå lue.")
           valg3=hva_vil_du_gjøre() #Bygge ut for if valg3==3/4
           if valg3==1: #Velger å gjette hvem som er morderen
                print("Dine opplysninger som du har samlet er:", opplysninger)
                gjett=gjett_morderen()  #funskjon for å gjette
                if gjett==1: #Gjetter Jonas
                    print("gratulerer du løste myssteriet, Jonas var morderen.")
                    game=False
                if gjett==2: #Gjetter Petter
                    print("Du tapte, prøv å spille på nytt")
           if valg3==2: #velger å gi opp
                print("Du tapte")
                game=False  
           if valg3==3:  #vil intervjue jonas om peron2
                valg2=intervju2()
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Jonas. 
                    print("Jeg var på nattklubben som heter del Rey.")
                    opplysninger.append("Jonas var på nattklubben som heter del Rey da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
                if valg2==2:  #velger å stille spørsmålet: Hva hadde du på deg den kvellden, til Jonas.
                    print("Jeg hadde på meg en brun jakke, jeans og et rødt skjerf.")
                    opplysninger.append("Jonas hadde på seg en brun jakke, jeans og et rødt skjerf kvelden mordet skjedde.") 
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt") 
           if valg3==4: #vil intervjue Petter en gng til
                valg2=intervju2()   
                if valg2==1: #velger å stille spørsmålet: hvor var du kl 12 en 5.november?, til Petter
                    print("Jeg var sammen med kjæresten min")
                    opplysninger.append("Petter var med kjæresten sin da mordet skjedde.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
                if valg2==2: #velger å stille spørsmålet: Hva hadde du på deg den kvelden, til Petter
                    print("Jeg hadde på meg en sort jakke, jeans og en blå lue")
                    opplysninger.append("Petter hadde på seg en sort jakke, jeans og en blå lue.")
                    print("Dine opplysninger som du har samlet er:", opplysninger)
                    gjett=gjett_morderen()
                    if gjett==1: #Gjetter Jonas
                        print("gratulerer du løste myssteriet, Jonas var morderen.")
                        game=False
                    if gjett==2:
                        print("Du tapte, prøv å spille på nytt")
        
    if valg==3: #Velger å ikke orker mer.
       orker_ikke_mer() 
       game=False
        