import math
import pygame

def addPoints(score, x, y, ugao):
    #Fukcija koja dodaje poene u zavisnosti od koordinata i menja vrednost poena

    ugao = math.atan(y / x)
    #Računamo ugao na osnovu koordinata

    if(math.sqrt(x**2 + y**2) < 10):
        score -= 50
        return score
    #Ako smo pogodili u centar, funkcija vraća vrednost i ne proverava dalje uslove      
    
    if(math.sqrt(x**2 + y**2) < 23):
        score -= 25
        return score
    #Isti princip kao kod unutrašnjeg kruga

    if(math.sqrt(x**2 + y**2) >253):
        return score
    #Ako smo pogodili van table, poeni se ne menjaju
    
    if(x > 0 and y <= 0):
        #U zavisnosti od toga u kom smo kvadrantu računamo koliko se poena treba dodeliti

        if(ugao > -0.1570):
            #Proveravamo vrednost ugla i na osnovu toga dodeljujemo poene

            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 18
                return score
            #Ako je pogodjeno u površinu x3 zone, vraćamo triput veću vrednost

            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 12
                return score
            #Ako je pogodjeno u površinu x2 zone, vraćamo dvaput veću vrednos

            score -= 6
            return score
            #Ako nije pogodjeno ni u x3 ni x2 zonu, vraćamo originalnu vrednost polja
        if(ugao > -0.4712):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 39
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 26
                return score
            score -= 13
            return score
        if(ugao > -0.7853):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 12
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 8
                return score
            score -= 4
            return score
        if(ugao > -1.0995):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 54
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 36
                return score
            score -= 18
            return score
        if(ugao > -1.4137):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 3
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 2
                return score
            score -= 1
            return score
        if(ugao > -1.5707):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 60
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 40
                return score
            score -= 20
            return score

    if(x > 0 and y > 0):
        if(ugao < 0.1570):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 18
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 12
                return score
            score -= 6
            return score
        if(ugao < 0.4712):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 30
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 20
                return score
            score -= 10
            return score
        if(ugao < 0.7853):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 45
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 30
                return score
            score -= 15
            return score
        if(ugao < 1.0995):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 6
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 4
                return score
            score -= 2
            return score
        if(ugao < 1.4137):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 51
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 34
                return score
            score -= 17
            return score
        if(ugao < 1.5707):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 9
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 6
                return score
            score -= 3
            return score

    if(x <= 0 and y > 0):
        if(ugao > -0.1570):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 33
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 22
                return score
            score -= 11
            return score
        if(ugao > -0.4712):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 24
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 16
                return score
            score -= 8
            return score
        if(ugao > -0.7853):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 48
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 32
                return score
            score -= 16
            return score
        if(ugao > -1.0995):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 21
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 14
                return score
            score -= 7
            return score
        if(ugao > -1.4137):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 57
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 38
                return score
            score -= 19
            return score
        if(ugao > -1.5707):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 9
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 6
                return score
            score -= 3
            return score

    if(x <= 0 and y <= 0):
        if(ugao < 0.1570):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 33
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 22
                return score
            score -= 11
            return score
        if(ugao < 0.4712):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 42
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 28
                return score
            score -= 14
            return score
        if(ugao < 0.7853):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 27
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 18
                return score
            score -= 9
            return score
        if(ugao < 1.0995):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 36
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 24
                return score
            score -= 12
            return score
        if(ugao < 1.4137):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 15
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 10
                return score
            score -= 5
            return score
        if(ugao < 1.5707):
            if(math.sqrt(x**2 + y**2) > 147 and math.sqrt(x**2 + y**2) < 158):
                score -= 60
                return score
            elif(math.sqrt(x**2 + y**2) > 240 and math.sqrt(x**2 + y**2) < 253):
                score -= 40
                return score
            score -= 20
            return score

def buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture) #Učitavamo sliku, kao što smo to radili u loadimage funkciji
    image = pygame.transform.scale(image, (300, 75)) #Pretvaramo je u 300*75 rezoluciju
    imagerect = image.get_rect() #Ovim pravimo "hitbox" našeg dugmeta, odnosno površinu na koju možemo kliknuti, kako bi se program video da smo kliknuli na dugme
    imagerect.topright = coords #Postavljamo gornji desni deo dugmeta na unete koordinate
    surface.blit(image,imagerect) #Ispisujemo sliku na ekran
    return (image,imagerect) #Vraćamo tuple, gde je prva vrednost slika, a druga površina koja joj odgovara
#Funkcija koja uzima slike i pretvara ih u dugmad

def buttonifyOriginalQuality(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)
#Radi po istom principu kao buttonify, samo ne menja rezoluciju slike


def loadImage(Picture, size = None):
    image = pygame.image.load(Picture) #Prvo loadujemo tu sliku, Picture je string sa lokacijom te slike na našem kompjuteru
    image.convert() #Konvertujemo je kako bi se mogla koristiti u programu
    if(size != None): #Proveravamo da li je uneta veličina
        image = pygame.transform.scale(image, size) #Ako je veličina uneta, konvertujemo sliku u tu veličinu
    return image
#Ovo je funkcija za učitavanje slike sa kompjutera kako bi se mogla koristiti u programu