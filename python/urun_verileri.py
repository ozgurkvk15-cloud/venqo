# 1. ürün bilgileri
urun1={
    "id":1,
    "ad": "Oversize Tişört",
    "marka":"VENQO",
    "kategori": "Tişört",
    "beden": "L",
    "renk":"Siyah",
    "fiyat": 499,
    "stok":10,
    "indirim":True,
    "favori":True,
}


# 2. ürün bilgileri
urun2={
    "id":2,
    "ad": "Kargo Pantolon",
    "marka":"VENQO",
    "kategori": "Pantolon",
    "beden": "M",
    "renk":"Haki",
    "fiyat": 899,
    "stok":20,
    "indirim":False,
    "favori":True
}

#3.ürün bilgileri 

urun3={
    "id":3,
    "ad": "Kapüşonlu Hoodie",
    "marka":"VENQO",
    "kategori": "Sweatshirt",
    "beden": "XL",
    "renk":"Gri",
    "fiyat": 1099,
    "stok":12,
    "indirim":True,
    "favori":True,
}



# 4. ürün bilgileri
urun4={
    "id":4,
    "ad": "Eşofman Altı",
    "marka":"VENQO",
    "kategori": "Alt Giyim",
    "beden": "L",
    "renk":"Lacivert",
    "fiyat": 699,
    "stok":18,
    "indirim":False,
    "favori":False,
}


# ürünler listesi oluşturuldu
urunler = [
    urun1,
    urun2,
    urun3,
    urun4
]   


# urun1 stoğu güncellendi
urun1["stok"]=7       

# urun2 fiyatı güncellendi
urun2["fiyat"]=799
urunler[0]["stok"] = urunler[0]["stok"] - 1      

print(urunler[0]["ad"])     # liste üzerinde işlem yapma
print(urunler[3]["stok"])

print(urunler[1]["ad"])
print(urunler[3]["fiyat"])
