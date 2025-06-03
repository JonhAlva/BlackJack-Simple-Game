#START: MAY 22 / 2025
#FREE TIME PROGRAMING BY JONH ALVA
#VERSION 1.0: MAY 23 / 2025

import random
import os
import Carta
import DealerCount
import PlayerCount
import History
import time

flag = True
globalPlayerCardList = []
globalDealerCardList = []
HistoryList = []
ContadorD = DealerCount.DealerCount()
ContadorP = PlayerCount.PlayerCount()
PlayerName = "Player"

#Juego de blackjack simple
def Mensaje():
    print(" █▄▀▄▀▄▀▄▀▄▀▄▀▄▀█  BLACKJACK GAME  █▀▄▀▄▀▄▀▄▀▄▀▄▀▄█ ")
    print("                     Version 1.3                    \n")
    print(" === === === === » TYPE AN OPTION « === === === === ")
    print("             1.         Play            ")
    print("             2.        History          ")
    print("             3.       Change Name       ")
    print("             4.         Exit            ")
    print(" === === === === === === === === === === === === ===")

def randomSymbol():
    #*Generar un numero aleatorio
    ran = random.randint(1, 4)

    #*Dependiendo el numero retornamos un simbolo de carta
    if ran == 1:
        return "♥"
    elif ran == 2:
        return "♦"
    elif ran == 3:
        return "♣"
    elif ran == 4:
        return "♠"
    else:
        return "Null"

def cartValue():
    #*Generar un numero aleatorio para valor de cartas
    RanNum = random.randint(1, 11)
    LetterValue = ["J", "Q", "K"]
    As = "A"
    #? print("DEBUG RANNUM: " + str(RanNum))

    if RanNum == 10:
        #* Generar un numero random para devolver una letra
        RanLetter = random.randint(0, 2)
        return LetterValue[RanLetter]
    
    if RanNum == 11 or RanNum == 1:
        return As
    
    return RanNum

def ReturnNumericValue(value):
    if value == "J" or value == "Q" or value == "K":
        return 10
    else:
        return value
    #! EL retorno del As se maneja en el juego ya que este puede agarrar dos valores dependiendo de la mano

def CartaDealer():
    nuevaCarta = Carta.Carta(cartValue(), randomSymbol())
    dealerCart = f"║ {str(nuevaCarta.getCartaSymbol())} {str(nuevaCarta.getCartaValor())} ║"
    globalDealerCardList.append(dealerCart)

    if nuevaCarta.getCartaValor() == "A":
        if ContadorD.count+11 > 21: # * Si se pasa de 21 entonces toma valor de 1
            ContadorD.sumarValor(1)
        elif ContadorD.count+11 == 21: # * Si da exactamente 21 toma el valor de 11
            ContadorD.sumarValor(11)
        elif ContadorD.count+11 < 21: # * Si no se pasa e 21 entonces...
            if ContadorD.count+11 > 21: # * Se agrega 11 si no se pasa
                ContadorD.sumarValor(1)
            else:
                ContadorD.sumarValor(11) # * Se agrega 1 si se pasa
        else:
            ContadorD.sumarValor(1) # * Si no hay coincidencias toma el valor de 1
    else:
        num = ReturnNumericValue(nuevaCarta.getCartaValor())
        ContadorD.sumarValor(num) #! Suma la mano del dealer

def CartaPlayer():
    nuevaCarta = Carta.Carta(cartValue(), randomSymbol())
    playerCart = f"║ {str(nuevaCarta.getCartaSymbol())} {str(nuevaCarta.getCartaValor())} ║"
    globalPlayerCardList.append(playerCart)

    if nuevaCarta.getCartaValor() == "A":
        if ContadorP.count+11 > 21:
            ContadorP.sumarValor(1)
        elif ContadorP.count+11 == 21:
            ContadorP.sumarValor(11)
        elif ContadorP.count+11 < 21:
            if ContadorP.count+11 > 21:
                ContadorP.sumarValor(1)
            else:
                ContadorP.sumarValor(11)
        else:
            ContadorP.sumarValor(1)
    else:
        num = ReturnNumericValue(nuevaCarta.getCartaValor())
        ContadorP.sumarValor(num)

def AnotherPlay():
    global globalPlayerCardList
    globalPlayerCardList.clear()
    global globalDealerCardList  
    globalDealerCardList.clear()
    ContadorD.count = 0
    ContadorP.count = 0

def DefeatMessage():
    print(" ■ » » » » » » YOU LOSE « « « « « « ■ ")
    print(f"┌ Dealer Count: {ContadorD.count}")
    print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")
    HistoryItem = History.History(ContadorD.count, ContadorP.count, "DEFEAT", PlayerName)
    HistoryList.append(HistoryItem)

def VictoryMessage():
    print(" ■ » » » » » » YOU WIN « « « « « « ■ ")
    print(f"┌ Dealer Count: {ContadorD.count}")
    print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")
    HistoryItem = History.History(ContadorD.count, ContadorP.count, "VICTORY ", PlayerName)
    HistoryList.append(HistoryItem)

def DrawMessage():
    print(" ■ » » » » » » DRAW « « « « « « ■ ")
    print(f"┌ Dealer Count: {ContadorD.count}")
    print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")
    HistoryItem = History.History(ContadorD.count, ContadorP.count, "DRAW", PlayerName)
    HistoryList.append(HistoryItem)

os.system("cls")
while flag == True:
    #Inicio del menú
    Mensaje()
    option = int(input())

    if option == 1:
        #! Primera Mano ----------------------------------------------------------------------
        os.system("cls")
        print("////////////////////////////////////////////////////////////////////////" + "\n")
        print(" DEALER HAND ══════════════════════════════════════════════ ")
        CartaDealer()
        globalDealerCardList.append("║  ?  ║")
        DealerResult = " ".join(globalDealerCardList)
        print(DealerResult + "\n")
        print(" YOUR HAND ════════════════════════════════════════════════ ")
        CartaPlayer() #Genera una nueva carta para el player y la añade a su lista
        CartaPlayer()
        PlayerResult = " ".join(globalPlayerCardList)
        print(PlayerResult + "\n")
        print(f"┌ Dealer Count: {ContadorD.count}")
        print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")
        print("////////////////////////////////////////////////////////////////////////")
        #!--------------------------------------------------------------------------------------

        while ContadorP.count <= 21:

            print(" ■ » » 1. STAND ■■ 2. HIT « « ■ ")
            Choice = int(input())

            #! STAND ----------------------------------------------------------------------------------------------------------
            if Choice == 1: #* Cuando el jugador ya no quiere mas cartas se hace el desenlace
                os.system("cls")
                globalDealerCardList.pop() #* Sacamos la ultima carta que es la de ?
                CartaDealer()
                #* Si al "voltear" la primera carta ya supera la mano del jugador automaticamente pierde
                if ContadorP.count < ContadorD.count:
                    print("////////////////////////////////////////////////////////////////////////" + "\n")
                    print(" DEALER HAND ══════════════════════════════════════════════ ")
                    DealerResult = " ".join(globalDealerCardList)
                    print(DealerResult + "\n")
                    print(" YOUR HAND ════════════════════════════════════════════════ ")
                    print(PlayerResult + "\n")
                    DefeatMessage()
                    print("////////////////////////////////////////////////////////////////////////")
                    break

                if ContadorD.count <= 17 or ContadorD.count < 21: #primero verificar si es menor a 21 y luego si es superior a 17 o no
                    while ContadorD.count <= 21:
                        CartaDealer()
                        if ContadorP.count < ContadorD.count or ContadorD.count == 21:
                            break
                
                print("////////////////////////////////////////////////////////////////////////" + "\n")
                print(" DEALER HAND ══════════════════════════════════════════════ ")
                DealerResult = " ".join(globalDealerCardList)
                print(DealerResult + "\n")
                print(" YOUR HAND ════════════════════════════════════════════════ ")
                print(PlayerResult + "\n")

                if ContadorD.count == ContadorP.count:
                    DrawMessage()
                    break

                if ContadorD.count > ContadorP.count and ContadorD.count < 21 or ContadorD.count == 21:
                    DefeatMessage()
                    #* ---
                    if len(globalDealerCardList) >= 6:
                        print(" Oh boy, are you okey?... ")
                    #* ---
                    break

                if ContadorD.count > 21:
                    VictoryMessage()
                    break

                print(f"┌ Dealer Count: {ContadorD.count}")
                print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")

                print("////////////////////////////////////////////////////////////////////////")

            #! CARD ----------------------------------------------------------------------------------------------------------
            elif Choice == 2:
                os.system("cls")
                print("////////////////////////////////////////////////////////////////////////" + "\n")
                print(" DEALER HAND ══════════════════════════════════════════════ ")
                DealerResult = " ".join(globalDealerCardList)
                print(DealerResult + "\n")
                print(" YOUR HAND ════════════════════════════════════════════════ ")
                CartaPlayer()
                PlayerResult = " ".join(globalPlayerCardList)
                print(PlayerResult + "\n")

                #if ContadorP.count == 21:
                #    print("* * * * * * * YOU WIN * * * * * * * ")

                #    print(f"-> Dealer Count: {ContadorD.count}")
                #    print(f"-> Player Count: {ContadorP.count}" + "\n")
                #    HistoryItem = History.History(ContadorD.count, ContadorP.count, "VICTORY")
                #    HistoryList.append(HistoryItem)
                #    break

                if ContadorP.count > 21:
                    DefeatMessage()
                    break

                print(f"┌ Dealer Count: {ContadorD.count}")
                print(f"└ {PlayerName} Count: {ContadorP.count}" + "\n")

                print("////////////////////////////////////////////////////////////////////////")

        input("-> Press Enter to return Menu")
        os.system("cls")
        AnotherPlay()
    elif option == 2:
        os.system("cls")
        if len(HistoryList) == 0:
            print("     ? ¿ ? ¿ - THERE ARE NO MATCHES YET - ? ¿ ? ¿ \n")
        else:
            contador = 0
            for partidas in HistoryList:
                contador += 1
                print(contador, partidas)
            input("\n -> Press Enter to Return")
            os.system("cls")
    
    elif option == 3:
        PlayerName = input("\n -> Type new Name: ")
        os.system("cls")
        print(" ▀ ▄ ▀ ▄ ▀ NAME CHANGED SUCCESSFULLY ▀ ▄ ▀ ▄ ▀ ")
        time.sleep(1.5)
        os.system("cls")
    
    elif option == 4:
        os.system("cls")
        print(" ♥ ♦ ♣ ♠ - Thanks for Playing - ♠ ♣ ♦ ♥ ")
        time.sleep(2)
        flag = False
    else:
        os.system("cls")
        print("         Ø X Ø X Ø X Ø - INVALID INPUT - Ø X Ø X Ø X Ø \n")