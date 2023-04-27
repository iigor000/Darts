import pygame
import math
import random
from utils import *
#Importujemo sve biblioteke koje će nam trebati, utils je drugi falj sa funkcijama koje su potrebne za ovaj program

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0 
#Standardno nameštanje pygame programa

startingScore = 501
player1 = startingScore
player2 = startingScore
player3 = startingScore
player4 = startingScore
randomness = 0
down = True
startScreen = True
playerTurn = 1
mousePosition = 0
firstShot = (0, 0)
secondShot = (0, 0)
thirdShot = (0, 0)
#Deklarišemo sve promenljive koje će nam trebati za program

player = loadImage("assets/dart1.png", (120, 120))
board = loadImage("assets/board.png")
dartSide = loadImage("assets/dartSideIcon.png", (100, 100))
dartInBoard = loadImage("assets/dartInBoard.png", (50, 50))
title = loadImage("assets/title.png")
onePlayerSelectedbtn = loadImage("assets/oneSelected.png", (300, 75))
twoPlayerSelectedbtn = loadImage("assets/twoSelected.png", (300, 75))
threePlayerSelectedbtn = loadImage("assets/threeSelected.png", (300, 75))
fourPlayerSelectedbtn = loadImage("assets/fourSelected.png", (300, 75))
easySelected = loadImage("assets/easySelected.png", (300, 75))
mediumSelected = loadImage("assets/mediumSelected.png", (300, 75))
hardSelected = loadImage("assets/hardSelected.png", (300, 75))
#Učitavamo sve potrebne slike preko funkcije koju smo napravili

playerNumber = 1
mode = 1
#Postavljamo početne vrednosti za broj igrača i mode

while running: #Ovo je glavna petlja, dok je running = True on će izvršavati kod
    mousePosition = pygame.mouse.get_pos() #Ovom funkcijom uzimamo poziciju miša u svakoj iteraciji petlje i sa njom proveravamo gde gadjamo i da li klikćemo dugmad

    if(startScreen): #Proveravamo da li treba učitati početni meni ili igricu
        for event in pygame.event.get():#Uzimamo sve "eventove", to jest bilo šta što je igrač mogao uraditi i shodno sa time koji je event, program koristi odgovarajuću funkciju
            if event.type == pygame.QUIT:
                running = False
            #Ako je igrač zatvorio igricu, running postaju False, odnosno program izlazi iz glavne petlje i igrica se gasi

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Proveravamo da li je event pritiskanje na dugme, ali ovako ne gledamo da li je igrač pritisnuo tačno na dugme
                if onePlayerbtn[1].collidepoint(mousePosition):#Poredimo poziciju miša sa pozicijom dugmeta, i ako se poklapaju, znači da je igrač pritisnuo na dugme; Ova logika se koristi za svako dugme
                    playerNumber  = 1 #Postavljamo broj igrača na odgovarajuću vrednost, po ovom principu rade i ostala dugmad za broj igrača i mode
                    break
                if twoPlayerbtn[1].collidepoint(mousePosition):
                    playerNumber = 2
                    break
                if threePlayerbtn[1].collidepoint(mousePosition):
                    playerNumber = 3 
                    break
                if fourPlayerbtn[1].collidepoint(mousePosition):
                    playerNumber = 4
                    break
                if easybtn[1].collidepoint(mousePosition):
                    mode = 1
                    break
                if mediumbtn[1].collidepoint(mousePosition):
                    mode = 2
                    break
                if hardbtn[1].collidepoint(mousePosition):
                    mode = 3
                    break
                if startbtn[1].collidepoint(mousePosition):
                    startScreen = False #Ako pritisnemo start dugme, program će prestati da učitava meni i preći na igricu
                    break
                
        screen.fill("white") #Postavljamo pozadinu u belo

        screen.blit(title, (285, 20)) #Screen.blit je pygame funkcija koja se koristi za postavljanje slika na ekran, ovim učitavamo naslov

        onePlayerbtn = buttonify('assets/onePlayer.png', (320, 300), screen)
        twoPlayerbtn = buttonify('assets/twoPlayers.png', (635, 300), screen)
        threePlayerbtn = buttonify('assets/threePlayers.png', (950, 300), screen)
        fourPlayerbtn = buttonify('assets/fourPlayers.png', (1265, 300), screen)
        easybtn = buttonify('assets/easy.png', (370, 450), screen)
        mediumbtn = buttonify('assets/medium.png', (780, 450), screen)
        hardbtn = buttonify('assets/hard.png', (1200, 450), screen)
        startbtn = buttonifyOriginalQuality("assets/start.png", (840, 575), screen)
        #Preko buttonify funckije koje smo napravili, uzimamo slike i pretvaramo ih u dugmad

        if(playerNumber == 1): #Proveravamo koje su vrednosti za broj igrača i shodno s time, preko odgovarajućeg dugmeta crtamo isto dugme zelene boje, kako bi igrač mogao da vidi koje je opcije izabrao
            screen.blit(onePlayerSelectedbtn, (20, 300))
        elif(playerNumber == 2):
            screen.blit(twoPlayerSelectedbtn, (335, 300))
        elif(playerNumber == 3):
            screen.blit(threePlayerSelectedbtn, (650, 300))
        elif(playerNumber == 4):
            screen.blit(fourPlayerSelectedbtn, (965, 300))

        if(mode == 1): #Po istom principu kao za broj igrača slikamo dugmad za mode
            screen.blit(easySelected, (70, 450))
        elif(mode == 2):
            screen.blit(mediumSelected, (480, 450))
        elif(mode == 3):
            screen.blit(hardSelected, (900, 450))
        
    else: #Ako je vrednost startScreen False, program učitava igricu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if(firstShot != (0, 0) and secondShot != (0, 0) and thirdShot != (0, 0)): #Ako su sva tri pogotka različita od (0, 0), znači da je igrač bacao strelicu tri puta i sa time završio svoj potez
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if nextTurnbtn[1].collidepoint(mousePosition): #Ako igrač pritisne na dugme za sledeći potez, resetujemo vrednosti za bacanja i prebacujemo potez na sledećeg igrača
                        firstShot = (0, 0)
                        secondShot = (0, 0)
                        thirdShot = (0, 0)
                        if(playerTurn < playerNumber):
                            playerTurn += 1
                        else:
                            playerTurn = 1
                        break

            if event.type == pygame.MOUSEBUTTONDOWN and thirdShot == (0, 0): #Proveravamo da li je igrač pritisnuo levi klik i da li ima još bacanja
                xToAdd = random.randint(- randomness * 2, randomness * 2)
                ytoAdd = random.randint(- randomness * 2, randomness * 2)
                while(math.sqrt((xToAdd)**2 + (ytoAdd)**2) > randomness * 2):
                    xToAdd = random.randint(- randomness * 2, randomness * 2)
                    ytoAdd = random.randint(- randomness * 2, randomness * 2)
                #Generišemo nasumične vrednosti, koje zavise od promenljive randomness i proveravamo da su u obliku kruga

                x = pygame.mouse.get_pos()[0] - 640 + xToAdd
                y = pygame.mouse.get_pos()[1] - 365 + ytoAdd
                #Pošto koordinatni sistem kreće od gornjeg levog ugla, moramo oduzeti vrednosti polovine ekrana, kako bi dobili nulu kao centar ekrana i odatle mogli da računamo poene i dodajemo naše nasumične vrednosti

                if x == 0:
                    x = 1
                #Pošto ćemo deliti y sa x, moramo proveriti da x nije nula, pa ako jeste stavljamo ga na jedan, jer to ne remeti računanje poena

                if(firstShot == (0, 0)):
                    firstShot = (x + 615, y + 365)

                elif(secondShot == (0, 0)):
                    secondShot = (x + 615, y + 365)

                elif(thirdShot == (0, 0)):
                    thirdShot = (x + 615, y + 365)
                #Proveravamo koje je bacanje na redu, i dajemo mu koordinate, kako bi mogli da crtamo
                
                if(playerTurn == 1):
                    player1 = addPoints(player1, x, y)
                    break
                elif(playerTurn == 2):
                    player2 = addPoints(player2, x, y)
                    break
                elif(playerTurn == 3):
                    player3 = addPoints(player3, x, y)
                    break
                else:
                    player4 = addPoints(player4, x, y)
                    break
                #Na osnovu toga čiji je potez odgovarajućem igraču dodeljujemo poene

        font = pygame.font.SysFont('comicsansms', 36)
        #Postavljamo font za tekst

        screen.fill("gray")
        #Postavljamo pozadinu

        screen.blit(board, (0, 0))
        #Crtamo tablu na ekran

        if(playerNumber == 1): #Ako igra samo jedan igrač, pisaće score, u suprotnom player 1
            score_text = font.render(f"Score: {player1}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
        else:
            player1_text = font.render(f'Player 1: {player1}', True, (255, 255, 255))
            screen.blit(player1_text, (10, 10))

        if(playerNumber >= 2):
            player2_text = font.render(f'Player 2: {player2}', True, (255, 255, 255))
            screen.blit(player2_text, (10, 50))
        if(playerNumber >= 3):
            player3_text = font.render(f'Player 3: {player3}', True, (255, 255, 255))
            screen.blit(player3_text, (10, 90))
        if(playerNumber >= 4):
            player4_text = font.render(f'Player 4: {player4}', True, (255, 255, 255))
            screen.blit(player4_text, (10,130))
        #U zavisnosti od toga koliko imamo igrača pišemo odgovarajuć broj poena

        if(firstShot != (0, 0)):
            screen.blit(dartInBoard, firstShot) #Ako je igrač iskoristio bacanje, crtamo srelicu u tabli
        else:
            screen.blit(dartSide, (50, 250)) #Ako nije iskoristio bacanje, crtamo strelicu sa strane, koja pokazuje koliko je bacanja ostalo

        if(secondShot != (0, 0)):
            screen.blit(dartInBoard, secondShot)
        else:
            screen.blit(dartSide, (50, 300))

        if(thirdShot != (0, 0)):
            screen.blit(dartInBoard, thirdShot)
        else:
            screen.blit(dartSide, (50, 350))


        if(firstShot != (0, 0) and secondShot != (0, 0) and thirdShot != (0, 0)):
            nextTurnbtn = buttonify('assets/nextTurnButton.png', (320, 600), screen)
            #Ako su sva tri bacanja iskorišćena, crtamo dugme za prelazak na sledeći potez

        else:
            screen.blit(player, (mousePosition[0] - 60, mousePosition[1] - 5))
            #Ako sva tri bacanja nisu iskorišćena, crtamo strelicu na istoj poziciji kao miš

            if(randomness < 1):
                down = False
            elif(randomness > 100):
                down = True
            if(down == True):
                if(mode == 1):
                    randomness -= 3
                elif(mode == 2):
                    randomness -= 5
                elif(mode == 3):
                    randomness -= 8
            elif(down == False):
                if(mode == 1):
                    randomness += 3
                elif(mode == 2):
                    randomness += 5
                elif(mode == 3):
                    randomness += 8
            #U zavisnosti od izabranog moda menjamo vrednost randomness
            
            pygame.draw.rect(screen, (0, 255, 0), (1100, 50, 100, 600))
            pygame.draw.rect(screen, (255, 0, 0), (1100, 50, 100, randomness * 6))
            #Crtamo dva pravougaonika koja predstavljaju koliko će nasumična bacanja biti

            pygame.draw.circle(screen, (255, 0, 0), mousePosition, randomness * 2, 2)
            #Crtamo okvir kruga oko strelice koji pokazuje površinu na koju mogu pasti strelice

        if(player1 <= 0 or player2 <= 0 or player3 <= 0 or player4 <= 0): #Pošto igrica treba da prestane da se učitava kada neki igrač završi, prvo proveravamo upravo to
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                        if mainMenubtn[1].collidepoint(mousePosition):
                            player1 = startingScore
                            player2 = startingScore
                            player3 = startingScore
                            player4 = startingScore
                            firstShot = (0, 0)
                            secondShot = (0, 0)
                            thirdShot = (0, 0)
                            startScreen = True
                            break
                            #Resetujemo sve vrednosti kako su bile pre početka igre, i vraćamo se na glavni meni
            screen.fill("gray")
            #Postavljamo pozadinu da bude siva

            mainMenubtn = buttonifyOriginalQuality("assets/mainMenu.png", (840, 550), screen)
            #Crtamo dugme za vraćanje na glavni meni

            if(player1 <= 0):
                font = pygame.font.SysFont('comicsansms', 120)
                playerWon = font.render(f'Player 1 WON!!!', True, (150, 0, 0))
                screen.blit(playerWon, (220, 250))
            elif(player2 <= 0):
                font = pygame.font.SysFont('comicsansms', 120)
                playerWon = font.render(f'Player 2 WON!!!', True, (150, 0, 0))
                screen.blit(playerWon, (220, 250))
            elif(player3 <= 0):
                font = pygame.font.SysFont('comicsansms', 120)
                playerWon = font.render(f'Player 3 WON!!!', True, (150, 0, 0))
                screen.blit(playerWon, (220, 250))
            elif(player4 <= 0):
                font = pygame.font.SysFont('comicsansms', 120)
                playerWon = font.render(f'Player 4 WON!!!', True, (150, 0, 0))
                screen.blit(playerWon, (220, 250))
            #U zavisnoti od toga koji igrač je stigao do 0 poena crtamo koji je igrač pobedio

    pygame.display.flip()
    #Brišemo sve sa ekrana

    dt = clock.tick(60) / 1000
    #Pokazuje koliko se puta igrica crta u sekundi (60)

pygame.quit()
#Ako izadjemo iz glavne petlje, program se gasi