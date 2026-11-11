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


### Paigaldamine
Klooni see repo:
```bash
git clone https://github.com/marionpol/piltide_haldur_py.git
```

Oma terminalis või powerShellis liigu kausta `piltide_haldur_py` ning käivita järgnev:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r teegid.txt
```

Mis need teevad?

Esimene ja teine käsk loovad projekti oma Pythoni keskkonna, kuhu saab lisada projekti põhiste teekide versioone.

Kolmas käsk lisab teegid koos versioonidega, mis on `teegid.txt` failis.

## Kasutamine


Käivita programm projekti kaustast terminalist:

```bash
python vaade.py
```
või kui esimene ei tööta

```bash
python3 vaade.py
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

## Autorid

Marion Poljakov ja Loora Maria Pavlov
