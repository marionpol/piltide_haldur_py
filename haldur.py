"""Hulgipiltide haldur (alfa): pildi töötlemise moodul.

Tähtaeg: 2026-11-11
Projekti teema: kausta piltide hulgitöötlus (suuruse muutmine ja
mustvalgeks tegemine).
Autorid: Marion Poljakov, Loora Maria Pavlov
Kasutatud allikad:
    - Pillow dokumentatsioon: https://pillow.readthedocs.io/
"""

import os
 
from PIL import Image
 
MAKS_LAIUS = 800
PILDI_LOPUD = (".png", ".jpg", ".jpeg")
 
 
def muuda_suurust(pilt, max_laius):
    """Vähendab pilti nii, et laius ei ületa max_laius.
 
    Proportsioon säilib. Kui pilt on juba piisavalt kitsas,
    tagastatakse see muutmata kujul.
    """
    if pilt.width <= max_laius:
        return pilt
    uus_korgus = int(pilt.height * max_laius / pilt.width)
    return pilt.resize((max_laius, uus_korgus))
 
 
def mustvalgeks(pilt):
    """Tagastab pildi mustvalgena."""
    return pilt.convert("L")
 
 
def tootle_pilt(pilt, max_laius):
    """Töötleb ühe pildi: muudab suurust ja teeb mustvalgeks."""
    pilt = muuda_suurust(pilt, max_laius)
    pilt = mustvalgeks(pilt)
    return pilt
 
 
def tootle_kaust(
    sisend_kaust,
    valjund_kaust,
    laius=None,
    korgus=None,
    vesimark=None,
    halltoonid=False,
):
    """Töötleb sisendkausta kõik pildid ja salvestab need väljundkausta.
 
    Alfas kasutatakse ainult laiust ja halltoone, parameetrid korgus ja
    vesimark on olemas ainult selleks, et sobida kasutajaliidesega.
    Vigased failid jäetakse vahele. Tagastab töödeldud piltide arvu.
    """
    os.makedirs(valjund_kaust, exist_ok=True)
    toodeldud = 0
 
    for failinimi in os.listdir(sisend_kaust):
        if not failinimi.lower().endswith(PILDI_LOPUD):
            continue
        try:
            pilt = Image.open(os.path.join(sisend_kaust, failinimi))
            if laius:
                pilt = muuda_suurust(pilt, laius)
            if halltoonid:
                pilt = mustvalgeks(pilt)
            if failinimi.lower().endswith((".jpg", ".jpeg")):
                pilt = pilt.convert("RGB") if pilt.mode not in ("RGB", "L") else pilt
            pilt.save(os.path.join(valjund_kaust, failinimi))
            toodeldud += 1
        except Exception as viga:
            print(f"Jäi vahele: {failinimi} ({viga})")
 
    return toodeldud
 
 
def main():
    """Testib töötlemist ühe pildiga (pane oma pildi nimi)."""
    pilt = Image.open("test.jpg")
    tootle_pilt(pilt, MAKS_LAIUS).save("test_valmis.jpg")
 
 
if __name__ == "__main__":
    main()
