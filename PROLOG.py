from pyswip import Prolog
prolog=Prolog()
prolog.consult("ABC.pl")


def KhanFamily():
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|=====================Khan Family Tree:=========================|\n")
    print("|ChoteKhan, ChotiRani, BarreKhan, BarriRani\t\t\t|")
    print("|Salim, Kausar, Nadir, Asad, Nahid, Sumra\t\t\t|")
    print("|Rizwan, Burhan, Rashid, Akram, Salima, Sanam, Rabia\t\t|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n")



def main():
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|\t\t\t\t\t\t\t\t|\n|========================| WELCOME :) |=========================|\n|\t\t\t\t\t\t\t\t|")

    value = None
    exist = False

    while(value!=0):
        display()    
        value=int(input("\n-> Enter the choice for the Relationship that you want to look up\n"))
        if(value==1):
            KhanFamily()
            Y=input("Enter name of person whose Beti you want to find: ")
            Y=Y.lower()
            for val in prolog.query("beti(X,"+Y+")"):
                exist = True
                print("\n''*****************************************************************''")
                print("{0} is the beti of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==2):
            KhanFamily()  
            Y=input("Enter name of person whose Beta you want to find: ")
            Y=Y.lower()
            for val in prolog.query("beta(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the beta of {1}.".format(val["X"], Y))
                print("*****************************************************************")

        if(value==3):
            KhanFamily()  
            Y=input("Enter name of person whose Dada you want to find: ")
            Y=Y.lower()
            for val in prolog.query("dada(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the dada of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==4):
            KhanFamily()  
            Y=input("Enter name of person whose Nana you want to find: ")
            Y=Y.lower()
            for val in prolog.query("nana(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the nana of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==5):
            KhanFamily()  
            Y=input("Enter name of person whose Dadi you want to find: ")
            Y=Y.lower()
            for val in prolog.query("dadi(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the dadi of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==6):
            KhanFamily()  
            Y=input("Enter name of person whose Nani you want to find: ")
            Y=Y.lower()
            for val in prolog.query("nani(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the nani of {1}.".format(val["X"], Y))
                print("*****************************************************************")
            
        if(value==7):
            KhanFamily()  
            Y=input("Enter name of person whose Sala you want to find: ")
            Y=Y.lower()
            for val in prolog.query("sala(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the sala of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==8):
            KhanFamily()  
            Y=input("Enter name of person whose Bahu you want to find: ")
            Y=Y.lower()
            for val in prolog.query("bahu(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the bahu of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                

        if(value==9):
            KhanFamily()  
            Y=input("Enter name of person whose Pota you want to find: ")
            Y=Y.lower()
            for val in prolog.query("pota(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the pota of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==10):
            KhanFamily()  
            Y=input("Enter name of person whose Nawasa you want to find: ")
            Y=Y.lower()
            for val in prolog.query("nawasa(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the nawasa of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==11):
            KhanFamily()  
            Y=input("Enter name of person whose BaapDada you want to find: ")
            Y=Y.lower()
            for val in prolog.query("baapDada(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the baapDada of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                
        if(value==12):
            KhanFamily()  
            Y=input("Enter name of person whose Khala you want to find: ")
            Y=Y.lower()
            for val in prolog.query("khala(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the khala of {1}.".format(val["X"], Y))
                print("*****************************************************************")
                

        if(value==13):
            KhanFamily()  
            Y=input("Enter name of person whose ChachaTaya you want to find: ")
            Y=Y.lower()
            for val in prolog.query("chachataya(X,"+Y+")"):
                exist = True
                print("\n*****************************************************************")
                print("{0} is the chachataya of {1}.".format(val["X"], Y))
                print("*****************************************************************")

        if exist == False:
            print("\n*****************************************************************")
            print(" =======================|Invalid Input! |========================")
            print("*****************************************************************")

        if ContinueorExit() == True:
            continue
        else:
            break
    print("_______________________! Thank You !________________________________\n")
    
    
def ContinueorExit():
    Keypressed = input("\n==========| Enter C to Continue and E to Exit |==========\n")
    if Keypressed == "C" or Keypressed == "c":
        return True
    elif Keypressed == "E"  or Keypressed == "e":
        return False
    else:
        print("=================..... Invalid Input .....==================\n")  


def display():
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|\t\t\t\t\t\t\t\t|\n|                        QUERIES\t\t\t\t|\n|\t\t\t\t\t\t\t\t|")
    print("|      Press 1 for Beti", "Press 2 for Beta\t\t\t|",sep="--------")
    print("|      Press 3 for Dada", "Press 4 for Nana\t\t\t|", sep="--------")
    print("|      Press 5 for Dadi", "Press 6 for Nani\t\t\t|", sep="--------")
    print("|      Press 7 for Sala", "Press 8 for Bahu\t\t\t|", sep="--------")
    print("|      Press 9 for Pota", "Press 10 for Nawasa\t\t|", sep="--------")
    print("|      Press 11 for BaapDada", "Press 12 for Khala\t\t|", sep="-----")
    print("|      Press 13 for Pota", "Press 0 for Exit\t\t|\n|\t\t\t\t\t\t\t\t|", sep="--------")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")       


if __name__=="__main__":
    main()