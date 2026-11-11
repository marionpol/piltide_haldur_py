"""
Projekti teema: Bulk Image Resizer & Editor (Pildihaldur)
Autorid: Loora Maria ja projektipartner
Kirjeldus: Programmi graafiline kasutajaliides (Tkinter), mis võimaldab
           kasutajal valida piltide kausta ja rakendada mass-töötlust.
Juhend: Käivita see fail Pythoni keskkonnas (`python vaade.py`).
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

try:

    from haldur import tootle_kaust
except ImportError:
    def tootle_kaust(
        sisend_kaust,
        valjund_kaust,
        laius=None,
        korgus=None,
        vesimark=None,
        halltoonid=False,
    ):
        pildid = [
            f
            for f in os.listdir(sisend_kaust)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
        if not os.path.exists(valjund_kaust):
            os.makedirs(valjund_kaust)
        return len(pildid)


class PildihaldurGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pildihaldur - Mass-töötlus")
        self.root.geometry("520x480")
        self.root.resizable(False, False)

        self.sisend_kaust = tk.StringVar()
        self.valjund_kaust = tk.StringVar()
        self.muuda_suurust_var = tk.BooleanVar(value=True)
        self.laius_var = tk.StringVar(value="800")
        self.korgus_var = tk.StringVar(value="600")
        self.vesimark_var = tk.StringVar()
        self.halltoonid_var = tk.BooleanVar(value=False)

        self._loo_kasutajaliides()

    def _loo_kasutajaliides(self):
        pad_x = 10
        pad_y = 5

        kaustad_frame = ttk.LabelFrame(self.root, text=" 1. Kaustade valik ")
        kaustad_frame.pack(fill="x", padx=pad_x, pady=pad_y)

        ttk.Label(kaustad_frame, text="Sisendkaust:").grid(
            row=0, column=0, sticky="w", padx=pad_x, pady=pad_y
        )
        ttk.Entry(
            kaustad_frame, textvariable=self.sisend_kaust, width=40
        ).grid(row=0, column=1, padx=pad_x, pady=pad_y)
        ttk.Button(
            kaustad_frame, text="Vali...", command=self._vali_sisend
        ).grid(row=0, column=2, padx=pad_x, pady=pad_y)

        ttk.Label(kaustad_frame, text="Väljundkaust:").grid(
            row=1, column=0, sticky="w", padx=pad_x, pady=pad_y
        )
        ttk.Entry(
            kaustad_frame, textvariable=self.valjund_kaust, width=40
        ).grid(row=1, column=1, padx=pad_x, pady=pad_y)
        ttk.Button(
            kaustad_frame, text="Vali...", command=self._vali_valjund
        ).grid(row=1, column=2, padx=pad_x, pady=pad_y)

        seaded_frame = ttk.LabelFrame(self.root, text=" 2. Töötluse seaded ")
        seaded_frame.pack(fill="x", padx=pad_x, pady=pad_y)

        ttk.Checkbutton(
            seaded_frame,
            text="Muuda pildi suurust (px):",
            variable=self.muuda_suurust_var,
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=pad_x, pady=pad_y)

        ttk.Label(seaded_frame, text="Laius:").grid(
            row=1, column=0, sticky="e", padx=pad_x
        )
        ttk.Entry(seaded_frame, textvariable=self.laius_var, width=8).grid(
            row=1, column=1, sticky="w", padx=pad_x
        )

        ttk.Label(seaded_frame, text="Kõrgus:").grid(
            row=1, column=2, sticky="e", padx=pad_x
        )
        ttk.Entry(seaded_frame, textvariable=self.korgus_var, width=8).grid(
            row=1, column=3, sticky="w", padx=pad_x
        )

        ttk.Label(seaded_frame, text="Vesimärgi tekst:").grid(
            row=2, column=0, sticky="w", padx=pad_x, pady=(10, 5)
        )
        ttk.Entry(
            seaded_frame, textvariable=self.vesimark_var, width=30
        ).grid(row=2, column=1, columnspan=3, sticky="w", padx=pad_x, pady=(10, 5))

        ttk.Checkbutton(
            seaded_frame,
            text="Teisenda halltoonidesse (Must-valge)",
            variable=self.halltoonid_var,
        ).grid(
            row=3, column=0, columnspan=4, sticky="w", padx=pad_x, pady=pad_y
        )

        # 3. Käivitus ja olek
        kaivita_btn = ttk.Button(
            self.root, text="Töötle pildid", command=self._kaivita_tootlus
        )
        kaivita_btn.pack(fill="x", padx=pad_x, pady=15)

        self.olek_label = ttk.Label(
            self.root,
            text="Olek: Ootab kasutaja sisendit...",
            font=("Arial", 9, "italic"),
        )
        self.olek_label.pack(anchor="w", padx=pad_x)

    def _vali_sisend(self):
        kaust = filedialog.askdirectory(title="Vali piltide kaust")
        if kaust:
            self.sisend_kaust.set(kaust)
            if not self.valjund_kaust.get():
                self.valjund_kaust.set(os.path.join(kaust, "toodeldud"))

    def _vali_valjund(self):
        kaust = filedialog.askdirectory(title="Vali väljundkaust")
        if kaust:
            self.valjund_kaust.set(kaust)

    def _kaivita_tootlus(self):
        s_kaust = self.sisend_kaust.get()
        v_kaust = self.valjund_kaust.get()

        if not s_kaust or not os.path.exists(s_kaust):
            messagebox.showerror("Viga", "Palun vali kehtiv sisendkaust!")
            return

        if not v_kaust:
            messagebox.showerror("Viga", "Palun määratle väljundkaust!")
            return

        laius = None
        korgus = None
        if self.muuda_suurust_var.get():
            try:
                laius = int(self.laius_var.get())
                korgus = int(self.korgus_var.get())
            except ValueError:
                messagebox.showerror(
                    "Viga", "Laius ja kõrgus peavad olema täisarvud!"
                )
                return

        vesimark = (
            self.vesimark_var.get().strip() if self.vesimark_var.get() else None
        )
        halltoonid = self.halltoonid_var.get()

        self.olek_label.config(text="Olek: Töötlen pilte...")
        self.root.update_idletasks()

        try:
            arv = tootle_kaust(
                sisend_kaust=s_kaust,
                valjund_kaust=v_kaust,
                laius=laius,
                korgus=korgus,
                vesimark=vesimark,
                halltoonid=halltoonid,
            )
            self.olek_label.config(
                text=f"Olek: Valmis! Töödeldud {arv} pilti."
            )
            messagebox.showinfo(
                "Edukas!", f"Piltide töötlus lõpetatud.\nTöödeldud: {arv} pilti."
            )
        except Exception as e:
            self.olek_label.config(text="Olek: Töötlus ebaõnnestus.")
            messagebox.showerror(
                "Viga töötlusel", f"Tekkis tõrge: {str(e)}"
            )


def main():
    root = tk.Tk()
    app = PildihaldurGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
