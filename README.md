Krypteringsverktyg!😁⚙️🔐🌸

Ett enkelt krypteringsverktyg för att generera nycklar, kryptera och dekryptera filer.👌🔑🔓🔒

Funktioner: 

1-Generera en säker krypteringsnyckel och spara den i en fil.🔑
2-Kryptera valfria filer för att göra dem säkra.🔒😊
3-Dekrypterar krypterade filer för att återfå originalinnehållet.🔓🔐🖼️

Verktyget är byggt med Python och använder Fernet-kryptering från cryptography-biblioteket för att säkerställa att dina filer hanteras på ett säkert sätt.🐍🌸

Hur fungerar koden?
Koden är uppdelad i flera delar för att hantera specifika uppgifter:👌

-Klassen Krypteringsverktyg:🌸

Ansvarar för att skapa, läsa och använda krypteringsnyckeln.
Har metoder för att kryptera och dekryptera filer.

-Kommandoradsgränssnitt:⌨️💻

Koden använder argparse för att låta användaren interagera med programmet via terminalen.
Du kan välja att generera en nyckel, kryptera en fil eller dekryptera en fil genom att använda olika kommandon och flaggor.

-Felhantering:❌‼️✅

Koden hanterar vanliga problem, som att nyckelfilen saknas eller om en fil inte kan hittas.
Koden är enkel att använda och designad för att hjälpa användare att skydda sina filer med minimal ansträngning.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Installation⚙️🌸
-Klona eller ladda ner repository

git clone https://github.com/ditt-repo/krypteringsverktyg.git

-Installera beroenden🐍🐍🌸💻
Se till att du har Python installerat (version 3.6 eller högre), och installera cryptography-biblioteket:
pip install cryptography

-Kör programmet✅💻
Programmet är klart att användas direkt från terminalen.

-Användning⚙️🪛🖱️📖
Generera en nyckel🔑
Skapa en krypteringsnyckel och spara den i standardfilen hemlig.key:
python script.py generate_key

-Kryptera en fil🔐
Kryptera en fil och skapa en ny fil med tillägget .enc:
python script.py encrypt -f <filnamn>
Exempel:
python script.py encrypt -f test.txt

-Dekryptera en fil🔓
Dekryptera en fil och spara den som en ny fil med prefixet decrypted_:
python script.py decrypt -f <filnamn>
Exempel:
python script.py decrypt -f test.txt.enc

-Anpassa nyckelfil🔑🔏
Om du vill använda en annan nyckelfil än standard:
python script.py <kommando> -k <nyckelfil>
Exempel:
python script.py encrypt -f test.txt -k annan_nyckel.key

-Felhantering❌‼️🪛✅
Om nyckelfilen saknas:
Kör generate_key för att skapa en ny.

Om dekrypteringen misslyckas:🥲✅🔑🖼️🔐
Kontrollera att du använder rätt nyckel och att filen är korrekt krypterad.

Sarai H🌸🔐🐍🔑🖼️
https://github.com/Sali-30
