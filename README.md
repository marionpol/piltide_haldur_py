# Piltide haldur

Lihtne pildi halduri programm, mis kasutab Pythoni Pillow teeki ja
Tkinteri graafilist kasutajaliidest. Hetkel on alfa versioon.

## Mida alfaversioon teeb

- avab akna, kus saab valida sisend- ja väljundkausta;
- töötleb sisendkausta kõik `.png`, `.jpg` ja `.jpeg` failid;
- vähendab pildi laiuse määratud väärtuseni (vaikimisi 800 px), säilitades
  proportsioonid; juba piisavalt kitsast pilti ei muudeta;
- soovi korral teeb pildid mustvalgeks (märkeruut aknas);
- salvestab töödeldud pildid väljundkausta samade failinimedega, originaale
  ei muudeta;
- jätab vigased failid vahele ja kuvab nende nimed terminalis.

Kõrguse ja vesimärgi väljad on vaate aknas olemas, kuid hallid ja lukustatud.
Need tulevad järgmises versioonis.

## Kasutamine

Esiteks tuleb installida vajalik teek:
```bash
python -m pip install -r requirements.txt
```

Käivita programm projekti kaustast:

```bash
python vaade.py
```

1. Kirjuta **Sisendkausta** nimi (hetkel test_pildid) ning lisa ka väljund kaust
2. Määra laius ja vajadusel märgi halltoonid.
3. Vajuta **Töötle pildid**.
4. Töödeldud pildid ilmuvad väljundkausta.

### Ainult halduri testimine

Põhi projekti kausta tuleb panna pilt nimega `test.jpg`:

```bash
python haldur.py
```

Tulemus salvestatakse faili `test_valmis.jpg`.

## Alfa piirangud

- kõrgus ja vesimärk pole kasutusel;
- puudub eelvaade ja edenemisriba;
- suure kausta puhul võib aken töötlemise ajal hanguda;
- alamkaustu ei töödelda.

## Plaanis

1. Kõrguse ja kärpimise valik
2. Vesimärk
3. Edenemisriba ja töötlemine taustalõimes
4. Eelvaate paneel
5. Uued faili formaadid?
6. Veel midagi huvitavat?

## Test_pildid kaust
Kasutusel on pildid www.unsplash.com leheküljelt, kust on võimalik kasutada tasuta pilte, mis ei nõua litsentse.
Pildi nimetused on jäetud originaalidena.

## Muu
Nõutud on, et kõik vajalikud failid oleksid saadaval, mistõttu jätame hetkel virtuaalkeskkonna venv .gitignore failist välja, kuid tulevikus eemaldame selle, kuna iga projekti kloonimisel tuleb vajalikud 

### Paigaldamine

Soovitatav on kasutada virtuaalkeskkonda:

```bash
python3 -m venv venv
source venv/bin/activate
```

Uues terminalis tuleb enne käivitamist `source venv/bin/activate` uuesti
käivitada.


## Autorid

Marion Poljakov ja Loora Maria Pavlov
