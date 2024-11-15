
from cryptography.fernet import Fernet #här importeras Fernet från cryptography bibliotek. 
import argparse #här importeras argparse bibliotek som mkommer att hjälpa oss att hantera kommandosargument. 
import os #här imprteras os bibliotek för att hjälpa oss att hantera fil och katalogoperationer. 


class Krypteringsverktyg:# här skapar en klass som fungerar som mall för krypteringsverktyg..
    def __init__(self, keyfile="hemlig.key"): #initialisering metod av klassen. 
        # Den här metoden körs när ett objekt av klassen skapas.
        # Den låter oss ange en standardfil för nyckeln, som är "hemlig.key".
        self.keyfile = keyfile  # Här sparar vi namnet på nyckelfilen.
        self.key = None  # Vi har ännu inte en nyckel, så vi sätter den till None:ingenting.

    def generate_key(self):# Den här funktionen genererar en nyckel som sparas i hemlig.key filen. 
        try:#för att hantera fel.
            self.key = Fernet.generate_key()  # Vi skapar en ny hemlig nyckel.
            with open(self.keyfile, "wb") as key_file:  # Vi öppnar en fil där vi sparar nyckeln.
                key_file.write(self.key)  # Vi skriver nyckeln till filen.
            print(f"Nyckel genererad och sparad som {self.keyfile}.")  # Vi berättar att nyckeln är sparad.
        except Exception as e:
            print(f"Fel vid generering av nyckel: {e}") # Om något går fel, säger vi det här.

    def load_key(self):# Den här funktionen laddar nyckeln från filen så att vi kan använda den.
        try:#för att ahntera fel.
            with open(self.keyfile, "rb") as key_file:  # Vi öppnar nyckelfilen för att läsa den.
                self.key = key_file.read()  # Vi läser in nyckeln från filen.
            print(f"Nyckel laddad från '{self.keyfile}'.")  # Vi berättar att nyckeln har laddats.
            return Fernet(self.key)  # returnerar en fernet objekt för kryptering och dekryptering.
        except FileNotFoundError:#för att undvika att programen krashar om filen finns inte.
            print(f"Nyckelfilen '{self.keyfile}' hittades inte. Generera nyckel först.")  # Om filen inte finns, säger vi till.
            return None  # Om vi inte hittar nyckeln, ger vi tillbaka None:inget. 

    
    def encrypt_file(self, filename):# Den här funktionen krypterar en fil, vilket gör den hemlig
        cipher_suite = self.load_key()  # Vi hämtar vår nyckel som ska göra filen hemlig.
        if cipher_suite is None:  # Om vi inte har en nyckel, avbryter vi.
            return

        try: #för att hantera fel som kan uppstå när filen öppnas, läses, krypteras eller sparas. 
            with open(filename, "rb") as file:  # Vi öppnar filen vi vill göra hemlig.
                file_data = file.read()  # Vi läser allt innehåll i filen.
            encrypted_data = cipher_suite.encrypt(file_data)  # Vi gör filen hemlig med hjälp av nyckeln.
            encrypted_file_name = f"{filename}.enc"  # Vi ger den hemliga filen ett nytt namn med .enc i sluitet.
            with open(encrypted_file_name, "wb") as encrypted_file:  # Vi skapar en ny fil för den hemliga datan.
                encrypted_file.write(encrypted_data)  # Vi sparar den hemliga datan i den nya filen.
            print(f"Filen '{filename}' krypterad och sparad som '{encrypted_file_name}'.")  # Vi berättar att filen är hemlig/krypterad nu.
        except Exception as e:
            print(f"Fel vid kryptering av filen '{filename}': {e}")  # Om något går fel, säger vi till.

    def decrypt_file(self, filename):  # Funktion för att dekryptera en fil
        cipher_suite = self.load_key()  # Laddar nyckeln för att dekryptera filen
        if cipher_suite is None:  # Om det inte finns någon nyckel, avbryter vvi.
            return
 
        try:
            with open(filename, "rb") as encrypted_file:  # Öppnar den krypterade filen.
                encrypted_data = encrypted_file.read()  # Läser in den krypterade innehållet.
 
            decrypted_data = cipher_suite.decrypt(encrypted_data)  # Dekrypterar innehållet
 
            # tar bort ".enc" från filnamnet om det finns och lägger till "decrypted_" som prefix.
            decrypted_file_name = os.path.splitext(os.path.basename(filename))[0]  # ta bort sökväg och filändelse
            if decrypted_file_name.endswith(".enc"):  # om filnsmnet slutar med ".enc".
                decrypted_file_name = decrypted_file_name[:-4]  # ta bort ".enc".
            final_decrypted_name = f"decrypted_{decrypted_file_name}"  # lägger till "decrypted_" till filnamnet.
 
            directory = os.path.dirname(filename)  # Hämtar mappens sökväg för att spara den dekrypterade filen
            final_decrypted_path = os.path.join(directory, final_decrypted_name)  #kombinerar sökväg och filnamn. 
 
            with open(final_decrypted_path, "wb") as decrypted_file:#skriver den dekrypterade innehållet till filen. 
                decrypted_file.write(decrypted_data)
 
            print(f"Filen '{filename}' dekrypterades och sparades som '{final_decrypted_path}'.")  # här säger vi till att dekryptering gick bra. 
        except Exception as e:
            print(f"Fel vid dekryptering av filen '{filename}': {e}")  # Hanterar eventuella fel vi dekrypering. 


def main():
    # Huvudfunktionen hanterar användarens kommandon
    parser = argparse.ArgumentParser(description="Krypterings verktyg för att generera nyckel, kryptera och dekryptera en fil.") #Förklarar för användaren vad programmet är till
    parser.add_argument("kommando", choices=["generate_key", "encrypt", "decrypt"], help="Ange 'generate_key' för att skapa en nyckel, 'encrypt' för att kryptera en fil, eller 'decrypt' för att dekryptera en fil.")
    # den första argument styr vad programmet ska göra, alltså vilken kommando ska köras. 
    parser.add_argument("-f", "--file", help="Fil som ska krypteras eller dekrypteras.")# 2 set för att skriva kommando 
    #Eftersom användaren kanske vill ange en specifik fil att kryptera eller dekryptera, behöver programmet veta vilken fil som ska användas.
    parser.add_argument("-k", "--keyfile", default="hemlig.key",help="Fil som innehåller krypteringsnyckeln som är hemlig.key")
    #default är för att om användaren inte anger en fil kommer programet att använda hemlig key som standard. 
    #Genom att ge ett standardvärde (hemlig.key) gör jag det enklare för användaren som inte behöver ange nyckelfilen om de använder standardnamnet.

    args = parser.parse_args()  # Vi läser in vad användaren skrev i kommandot.


    # Vi skapar ett nytt krypteringsverktyg och skickar med var vi ska spara nyckeln.
    tool = Krypteringsverktyg(args.keyfile)

    # Här bestämmer vi vad programmet ska göra beroende på vad användaren valde.
    if args.kommando == "generate_key":
        tool.generate_key()  # Vi skapar en ny nyckel.
    elif args.kommando == "encrypt":
        if args.file:
            tool.encrypt_file(args.file)  # Vi krypterar (gör hemlig) filen användaren valde.
        else:
            print("Ange en fil att kryptera med -f + filnamn")
    elif args.kommando == "decrypt":
        if args.file:
            tool.decrypt_file(args.file)  # Vi dekrypterar (gör läsbar) filen användaren valde.
        else:
            print("Ange en fil att dekryptera med -f + filnamn")

if __name__ == "__main__":# Detta körs när vi startar programmet.
     main()  # Vi kör huvudprogrammet som hanterar alla kommandon.




