from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import tkinter as tk
import sys
import PIL
from PIL import ImageTk
from PIL import Image
import tkinter.ttk as ttk
from tkinter.ttk import Combobox
from datetime import datetime
import mysql.connector

def quit(ekran):
    ekran.destroy()
    sys.exit(5000)


def kullanici_ekran(veritab, ekran, isim, mycursor):
    kullaniciEkran = Toplevel(ekran)
    kullaniciEkran.title("Kullanıcı Arayüzü")
    kullaniciEkran.geometry("1280x600+20+0")
    kullaniciEkran.resizable(FALSE, FALSE)
    my_image = ImageTk.PhotoImage(Image.open("bgimage.jpg"))
    arkaplan = Label(kullaniciEkran, image=my_image)
    arkaplan.place(x=0, y=0)
    kullaniciEkran.iconbitmap("YICO.ico")


    siparisVer = Button(kullaniciEkran, compound=TOP, text="Sipariş Ver",
                        command=lambda: siparisVerFonk(veritab, kullaniciEkran, my_image, isim),bg="#2a1415",fg="White",font=("helvetica","15","bold"))
    siparisVer.place(x=0, y=120, height=100, width=205)
    siparislerim = Button(kullaniciEkran, text="Siparişlerim", compound=TOP,
                          command=lambda: siparislerimFonk(kullaniciEkran, my_image, isim, mycursor),bg="#2a1415",fg="White",font=("helvetica","15","bold"))
    siparislerim.place(x=0, y=220, height=100, width=205)
    profilim = Button(kullaniciEkran, text="Profilim", compound=TOP,
                          command=lambda: profilimFonk(kullaniciEkran, my_image, isim, mycursor,veritab),bg="#2a1415",fg="White",font=("helvetica","15","bold"))
    profilim.place(x=0, y=320, height=100, width=205)    
    MenulerNeler1 = Label(kullaniciEkran,
                          text="Catering şirketi olarak \n İstanbul’da günlük tabldot yemek servisi hizmetiyle \n birlikte sizlerin yanınızdayız. \n Catering şirketimiz İstanbul 'da yemek üretimi ve servis hizmetlerine \n 1979 yılında Şişli Bomonti iş merkezinde \n küçük çapta bir mutfak ile, yüz kişiye yemek servisi yaparak, çalışmaya başladı.\n Kuruluş zamanımızda geniş çaplı firmalar kurumsal yemek ihtiyaçlarını\n kendi kurumsal bünyeleri içerisinde bir veya iki personel ile karşılıyorlardı. \n Küçük ve orta çaplı firmalar ise ihtiyaçları olan yemeği yeni kurulmakta olan \n tabldot firmalarından veya çevredeki lokantalardan temin ediyorlardı.",font=("helvetica",15),bg="#b89073",fg="black",width=75,height=17, border=0)
    MenulerNeler1.place(x=205,y=120)
    mycursor5=veritab.cursor()
    mycursor5.execute("SELECT ad FROM musteriler WHERE mail = %s", (isim.get(),))
    data4 = mycursor5.fetchall()
    mycursor5.execute("SELECT soyad FROM musteriler WHERE mail = %s", (isim.get(),))
    data5=mycursor5.fetchall()
    textyazisii=("Hoşgeldin",data4 , data5 )
    label2 = Label(master=kullaniciEkran,
                text=textyazisii, bg="#502b26", fg="white",width=25,height=2)
    label2.place(x=205,y=35)
    logo= Image.open("YLOGO_1.png")
    logoyukle = ImageTk.PhotoImage(logo)
    goruntulogo = Label(kullaniciEkran, image=logoyukle ,bg="#2a1415" ,border=0)
    goruntulogo.image = logoyukle
    goruntulogo.place(x=45, y=5)

def profilimFonk(kullaniciEkran, my_image, isim, mycursor,veritab):
    profilimEkran = Toplevel(kullaniciEkran)
    profilimEkran.title("Profilim Arayüzü")
    profilimEkran.geometry("1280x600+20+0")
    profilimEkran.resizable(FALSE, FALSE)
    arkaplan = Label(profilimEkran, image=my_image)
    arkaplan.place(x=0, y=0)
    def limitSizePas(*args):
        value = sifresinir.get()
        if len(value) > 8: sifresinir.set(value[:8])
    sifresinir = StringVar()
    sifresinir.trace('w', limitSizePas)

    sifrelab = Label(profilimEkran, text="Şifreniz : (Max: 8)", width=15, font="30", bg="#2a1415" ,fg="white" )
    sifrelab.place(x=410, y=210)
    
    sifreentt = Entry(profilimEkran, width=25, show="*", textvariable=sifresinir , font="30", bg="#b89073" , border="0")
    sifreentt.place(x=590, y=210)
    
    adlab = Label(profilimEkran, text="Adınız :",width=15, font="30", bg="#2a1415" ,fg="white")
    adlab.place(x=410, y=250)
    
    adentt = Entry(profilimEkran, width=25 , font="30", bg="#b89073" , border="0")
    adentt.place(x=590, y=250)
    
    soyadlab = Label(profilimEkran, text="Soyadınız :",width=15, font="30", bg="#2a1415" ,fg="white")
    soyadlab.place(x=410, y=290)
    
    soyadentt = Entry(profilimEkran, width=25 , font="30", bg="#b89073" , border="0")
    soyadentt.place(x=590, y=290)

    mycursor2=veritab.cursor()
    sifreentry=sifreentt.get()
    adentry=adentt.get()
    soyadentry=soyadentt.get()
    gonderguncelle = Button(profilimEkran, text="GÜNCELLE!", command=lambda: gonderguncelleFonk(profilimEkran,mycursor2,veritab,sifreentt, adentt, soyadentt,isim,kullaniciEkran), font=3, width=18 ,bg="#502b26" ,fg="#b89073")
    gonderguncelle.place(x=590, y=330)


def gonderguncelleFonk(profilimEkran,mycursor2,veritab,sifreentt, adentt, soyadentt,isim,kullaniciEkran):

    mycursor2=veritab.cursor()
 
    if len(adentt.get()) > 0:
        sorgu=("UPDATE musteriler SET ad = %s WHERE mail = %s")
        deger=(adentt.get(),isim.get())
        mycursor2.execute(sorgu,deger) 
        veritab.commit()
        sorgu=("UPDATE siparisler SET ad = %s WHERE musterimail = %s")
        deger=(adentt.get(),isim.get())
        mycursor2.execute(sorgu,deger) 
        veritab.commit()
        
    if len(sifreentt.get()) > 0:
        sorgu=("UPDATE musteriler SET sifre = %s WHERE mail = %s")
        deger=(sifreentt.get(),isim.get())
        mycursor2.execute(sorgu,deger) 
        veritab.commit()

    if len(soyadentt.get()) > 0:
        sorgu=("UPDATE musteriler SET soyad = %s WHERE mail = %s")
        deger=(soyadentt.get(),isim.get())
        mycursor2.execute(sorgu,deger) 
        veritab.commit()
        sorgu=("UPDATE siparisler SET soyad = %s WHERE musterimail = %s")
        deger=(soyadentt.get(),isim.get())
        mycursor2.execute(sorgu,deger) 
        veritab.commit()
    



    messagebox.showinfo("Bilgilendirme", "Güncelleme Başarılı! Yeniden Giriş Yapınız!",parent=profilimEkran)
    kullaniciEkran.destroy()




def siparisvermefonk(siparisverme,veritab,acilan_kutu, acilanicecek, textbox, isim, my_image,deger,yemekadet,icecekadet):

    acilankutu = acilan_kutu.get()
    adreskutu = textbox.get("1.0",END)
    acilanicecek=acilanicecek.get()
    kullanicimail =isim.get()
    katalog=deger.get()
    yemekadeti=yemekadet.get()
    icecekadeti=icecekadet.get()
    if yemekadeti == "Yemek Adeti Seçiniz":
        messagebox.showinfo("Uyarı", "Yemek adeti seçiniz!",parent=siparisverme)
    yfiyatint=int(yemekadeti)
    ifiyatint=int(icecekadeti)
    yfiyat = int(100*yfiyatint)
    ifiyat= int(5*ifiyatint)
    indirimvarmi=False
    cevape="Evet"
    cevaph="Hayır"
    sonuc=""
    if yfiyat+ifiyat <1000:
        toplam = int(yfiyat+ifiyat)
        oncekifiyat="İndirim Yok!"
        aradakiFark="İndirim Yok!"
        indirimvarmi=False
        if indirimvarmi==False:
            sonuc = cevaph
    else:
        oncekifiyat=int(yfiyat+ifiyat)
        toplam=int((yfiyat+ifiyat)*80/100)
        aradakiFark = int(toplam-oncekifiyat)
        indirimvarmi=True
        if indirimvarmi==True:
            sonuc = cevape
    
    
    onay = Toplevel()
    onay.geometry("1280x600+20+0")
    onay.title("Sipariş Onay Ekranı")
    onay.resizable(FALSE,FALSE)
    onay.iconbitmap("YICO.ico")
    frame = Label(master=onay, image=my_image)
    frame.place(x=0,y=0)
    for i in range(1):
        textyazisi=("Seçilen Menü = {} \n Yemek Miktarı = {} \n Seçilen İçecek = {} \n İçecek Miktarı = {} \n Katalog Var Mı = {}\n Teslimat Adresi= {} \n Toplam Tutar = {} \n %20 İndirim Var Mı={} \n İndirimden Önceki Fiyat = {} \n İndirim Tutarı = {} ".format(acilankutu,yemekadeti,acilanicecek,icecekadeti,katalog,adreskutu,toplam,sonuc,oncekifiyat,aradakiFark))
        label = Label(master=onay, text=textyazisi, bg="#2a1415" ,fg="white", border="0",width=100,height=20)
        label.place(x=320,y=125)
    onayButon = Button(
        master= onay, 
        text = "SİPARİŞİ ONAYLA", 
        command = lambda: siparisOnay(onay,veritab,isim,acilankutu,acilanicecek, adreskutu, kullanicimail,katalog,yemekadeti,icecekadeti,toplam),
        bg="white"
    )
    onayButon.place(x=640,y=450)
    onay.wait_window()


def siparisOnay(onay,veritab,isim,acilankutu,acilanicecek,adreskutu,kullanicimail,katalog,yemekadeti,icecekadeti,toplam):
    mycursor4=veritab.cursor()
    mycursor4.execute("SELECT ad FROM musteriler WHERE mail = %s", (isim.get(),))
    adi= mycursor4.fetchmany(1)
    adii=''.join(str(adi)[1:-1])
    adiii=adii.replace("('","")
    adiiii=adiii[:-3]
    mycursor5=veritab.cursor()
    mycursor5.execute("SELECT soyad FROM musteriler WHERE mail = %s", (isim.get(),))
    soyadi= mycursor5.fetchmany(1)
    soyadii=''.join(str(soyadi)[1:-1])
    soyadiii=soyadii.replace("('","")
    soyadiiii=soyadiii[:-3]

    mycursor3 = veritab.cursor()
    sorgu = "INSERT INTO siparisler (ad,soyad,menu,menu_adet,icecek,icecek_adet,toplam,katalog,adres,musterimail) VALUES (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s)"
    deger = (adiiii,soyadiiii,acilankutu,yemekadeti,acilanicecek,icecekadeti,toplam,katalog,adreskutu,kullanicimail)
    mycursor3.execute(sorgu, deger)
    veritab.commit()
    onay_mesaji=messagebox.showinfo("Uyarı","Siparişiniz Başarıyla Oluşturuldu!",parent=onay)
    

def siparisVerFonk(veritab, kullaniciEkran, my_image, isim):
    siparisverme = Toplevel(kullaniciEkran)
    siparisverme.geometry("1280x600+20+0")
    siparisverme.title("Sipariş Verme Ekranı")
    siparisverme.resizable(FALSE, FALSE)
    frame = Label(master=siparisverme, image=my_image)
    frame.pack(expand=True, fill="both")
    siparisverme.iconbitmap("YICO.ico")

    menuler = ["Geleneksel Menü", "Modern Sofra Menü", "Kış Menü"]
    icecekler = ["İÇECEK YOK","KOLA","FANTA","ICE TEA", "LIMONATA","AYRAN"]
    yemekadeti=[1,2,3,4,5,6,7,8,9,10]
    icecekadeti=[0,1,2,3,4,5,6,7,8,9,10]
    acilan_kutu = Combobox(siparisverme, values=menuler, width=37, height=14)
    acilan_kutu.set("MENÜ SEÇİMİ YAPINIZ")
    acilan_kutu.place(x=50, y=100)

    yemekadet = Combobox(siparisverme, values=yemekadeti, width=37, height=50)
    yemekadet.set("Yemek Adeti Seçiniz")
    yemekadet.place(x=50, y=140)

    acilanicecek = Combobox(siparisverme, values=icecekler, width=37, height=50)
    acilanicecek.set("İÇECEK SEÇİMİ YAPINIZ")
    acilanicecek.current(0)
    
    acilanicecek.place(x=50, y=180)


    icecekadet = Combobox(siparisverme, values=icecekadeti, width=37, height=50)
    icecekadet.set("İçecek Adeti Seçiniz")
    icecekadet.current(0)
    icecekadet.place(x=50, y=220)

    deger=StringVar()
    sirketkatalogu=Checkbutton(siparisverme,text="Katalog Gönder",variable=deger,onvalue="Evet",offvalue="Hayır" , bg="White")
    sirketkatalogu.deselect()
    sirketkatalogu.place(x=110,y=470)
    
    adres = Label(siparisverme, text="Adresinizi Giriniz :", font=("bold"),bg="#2a1415" ,fg="white" ,border = 0)
    adres.place(x=50, y=265)
    textbox = Text(siparisverme, bg="#2a1415" ,fg="white", width=30, height=10)
    textbox.place(x=50, y=288)

    siparisverbuton = Button(
        master=siparisverme,
        text="SİPARİŞ VER", bg="white",width=10, height=2,
        command=lambda: siparisvermefonk(siparisverme,veritab,acilan_kutu,acilanicecek, textbox, isim, my_image,deger,yemekadet,icecekadet)
    )
    siparisverbuton.place(x=125, y=500)
    
    resim1 = Image.open("MENU.png")
    yukle = ImageTk.PhotoImage(resim1)
    goruntu1 = Label(siparisverme,text="Menü-1", image=yukle, border=0)
    goruntu1.image = yukle
    goruntu1.place(x=305, y=100)
    resim2 = Image.open("MENU22.png")
    yukle2 = ImageTk.PhotoImage(resim2)
    goruntu2 = Label(siparisverme,text="Menü-2", image=yukle2, border=0)
    goruntu2.image = yukle2
    goruntu2.place(x=535 , y=100)
    resim3 = Image.open("MENU33.png")
    yukle3 = ImageTk.PhotoImage(resim3)
    goruntu3 = Label(siparisverme,text="Menü-3", image=yukle3, border=0)
    goruntu3.image = yukle3
    goruntu3.place(x=765 , y=100)
    resim4 = Image.open("icecek2.png")
    yukle4 = ImageTk.PhotoImage(resim4)
    goruntu4 = Label(siparisverme,text="Menü-4", image=yukle4, border=0)
    goruntu4.image = yukle4
    goruntu4.place(x=995 , y=100)

def siparislerimFonk(kullaniciEkran, my_image, isim, mycursor):
    siparislerim = Toplevel(kullaniciEkran)
    siparislerim.title("Siparişlerim")
    siparislerim.geometry("1280x600+20+0")
    siparislerim.resizable(FALSE, FALSE)
    frame = Label(master=siparislerim, image=my_image)
    frame.place(x=0, y=0)
    siparislerim.iconbitmap("YICO.ico")
    mycursor.execute("SELECT * FROM siparisler WHERE musterimail = %s", (isim.get(),))
    data = mycursor.fetchall()
    columns = ["SiparişId","Ad","Soyad","Seçilen Menü","Sipariş Adeti","İçecek","İçecek Adeti","Toplam","Siparişte Katalog Var Mı", "Adres","Sipariş Tarihi", "Email"]
    treeview_olustur(master=siparislerim, columns=columns, data=data,width=550)

def girisYap(veritab, mycursor, isim, sifre, ekran):
    def kullanici_giris(tup):
        mycursor.execute("SELECT * FROM musteriler WHERE mail=%s AND sifre=%s", tup)
        return (mycursor.fetchall())

    data = ( 
        isim.get(),
        sifre.get()
    )

    if isim.get() == "":
        messagebox.showinfo("Uyarı", "Önce maili giriniz!")
    elif sifre.get() == "":
        messagebox.showinfo("Uyarı", "Önce şifreyi giriniz!")
    else:
        res = kullanici_giris(data)
        if res:
            messagebox.showinfo("Uyarı", "Giriş Başarılı!")
            kullanici_ekran(veritab, ekran, isim, mycursor)
        else:
            messagebox.showinfo("Uyarı", "Eposta/Şifre Hatalı!")


def gonderFonk(uyeol,veritab, mailent, sifreent, adent, soyadent):
    if mailent.get() == "":
        messagebox.showinfo("Uyarı", "Önce maili giriniz!",parent=uyeol)
    elif sifreent.get() == "":
        messagebox.showinfo("Uyarı", "Önce şifreyi giriniz!",parent=uyeol)
    elif adent.get() == "":
        messagebox.showinfo("Uyarı", "Önce adınızı giriniz!",parent=uyeol)
    elif soyadent.get() == "":
        messagebox.showinfo("Uyarı", "Önce soyadınızı giriniz!",parent=uyeol)
    else:
        mycursor = veritab.cursor()
        sorgu = "INSERT INTO musteriler (mail,sifre,ad,soyad) VALUES (%s, %s, %s, %s)"
        deger = (mailent.get(), sifreent.get(), adent.get(), soyadent.get())
        mycursor.execute(sorgu, deger)
        veritab.commit()
        uyari_mesaji = messagebox.showinfo("Bilgilendirme", "Üyeliğiniz Başarılı!",parent=uyeol)


def uyeol(veritab, ekran, my_image):
    uyeol = Toplevel(ekran)
    uyeol.geometry("1280x600")
    uyeol.title("Uye Ol")
    uyeol.resizable(FALSE, FALSE)
    frame = Label(master=uyeol, image=my_image)
    frame.pack(expand=True, fill="both")
    uyeol.iconbitmap("YICO.ico")
    
    
    mailab = Label(uyeol, text="Mail Adresiniz  : ",width=15, font="30", bg="#2a1415" ,fg="white" )
    mailab.place(x=410,y=170)

    mailent = Entry(uyeol, width=25,font="30", bg="#b89073" , border="0")
    mailent.place(x=590, y=170)

    def limitSizePas(*args):
        value = sifresinir.get()
        if len(value) > 8: sifresinir.set(value[:8])
    sifresinir = StringVar()
    sifresinir.trace('w', limitSizePas)

    sifrelab = Label(uyeol, text="Şifreniz : (Max: 8)", width=15, font="30", bg="#2a1415" ,fg="white" )
    sifrelab.place(x=410, y=210)
    
    sifreent = Entry(uyeol, width=25, show="*", textvariable=sifresinir , font="30", bg="#b89073" , border="0")
    sifreent.place(x=590, y=210)
    
    adlab = Label(uyeol, text="Adınız :",width=15, font="30", bg="#2a1415" ,fg="white")
    adlab.place(x=410, y=250)
    
    adent = Entry(uyeol, width=25 , font="30", bg="#b89073" , border="0")
    adent.place(x=590, y=250)
    
    soyadlab = Label(uyeol, text="Soyadınız :",width=15, font="30", bg="#2a1415" ,fg="white")
    soyadlab.place(x=410, y=290)
    
    soyadent = Entry(uyeol, width=25 , font="30", bg="#b89073" , border="0")
    soyadent.place(x=590, y=290)

    gonder = Button(uyeol, text="UYE OL!", command=lambda: gonderFonk(uyeol,veritab, mailent, sifreent, adent, soyadent), font=3, width=18 ,bg="#502b26" ,fg="#b89073")
    gonder.place(x=590, y=330)
    uyeol.wait_window()    


def menubar(master):
    def hakkindaFonk():
        messagebox.showinfo("Hakkında", " Bu uygulama \n Karadeniz Teknik Üniversitesi \n İktisadi ve İdari Bilimler Fakültesi \n Yönetim Bilişim Sistemleri Bölümü öğrencilerinden \n Oğuzcan Uzunöner ve Canan Arabacı \n tarafından geliştirilmiştir." , parent=master)

    menubar = Menu(master)
    hakkinda= Menu (menubar,tearoff = 0)
    hakkinda.add_command(label="Hakkında", command=hakkindaFonk)
    menubar.add_cascade(label="Uygulama", menu = hakkinda)
    master.config(menu=menubar)

    


    
def veriye_odaklan(treeview,master):
    item = treeview.item(treeview.selection())
    ciktii =list(item["values"])
    if len(ciktii) > 2:
        text=ciktii[9]
        messagebox.showinfo("Tam Adres", text,parent=master)



def treeview_olustur(master, columns, data, width):
    
    y_scrollbar = Scrollbar(master=master, orient="vertical")
    y_scrollbar.pack(side="right", fill="y")
    
    
    x_scrollbar = Scrollbar(master=master, orient="horizontal")
    x_scrollbar.pack(side="bottom", fill="x")
    

    treeview = Treeview(master=master, columns=columns, show="headings")
    treeview.pack(expand=True, fill="both")
    
    
    x_scrollbar["command"] = treeview.xview
    y_scrollbar["command"] = treeview.yview
    
    
    treeview["yscrollcommand"] = y_scrollbar.set
    treeview["xscrollcommand"] = x_scrollbar.set


    for i, j in enumerate(columns):
        
        treeview.column(
            column=f"#{i + 1}",  
            width=width,         
            anchor=CENTER     
        )
        
        treeview.heading(
            column=f"#{i + 1}",  
            text=j               
        )   

    
    for index, row in enumerate(data):
        treeview.insert(
            parent="",           
            index=index,         
            values=row          
        )


    
    treeview.bind(
        sequence="<Double-Button-1>", 
        func=lambda event: veriye_odaklan(treeview,master)
    )
def personelekran(veritab,isim, mycursor,personelekrangiris,my_image):
    personelEkran = Toplevel(personelekrangiris)
    personelEkran.title("Personel Arayüzü")
    personelEkran.geometry("1280x600+20+0")
    personelEkran.resizable(FALSE, FALSE)
    arkaplan = Label(personelEkran, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor.execute("SELECT ad FROM personel WHERE mail = %s", (isim.get(),))
    data4 = mycursor.fetchall()
    mycursor.execute("SELECT soyad FROM personel WHERE mail = %s", (isim.get(),))
    data5=mycursor.fetchall()
    textyazisii=("Hoşgeldin",data4 , data5)
    label2 = Label(master=personelEkran, text=textyazisii, font=("Helvetica","15","bold"),bg="#b89073", fg="white",width=30,height=5)
    label2.place(x=250,y=50)
    mycursor.execute("SELECT SUM(toplam) FROM siparisler")
    kazanc=mycursor.fetchone()
    toplamkazanctext=("Kazancınız", kazanc)
    ToplamKazanc = Label(master=personelEkran,text=toplamkazanctext,font=("Helvetica","15","bold"),bg="#b89073", fg="white",width=30,height=5).place(x=650,y=50)
    geleneksel = Button(personelEkran)
    geleneksel.config(text="Geleneksel Menü Rapor", command=lambda: gelenekselFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    geleneksel.place(x=250, y=200)

    kis = Button(personelEkran)
    kis.config(text="Kış Menü Rapor", command=lambda: kisFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    kis.place(x=522, y=200)

    modern = Button(personelEkran)
    modern.config(text="Modern Sofra Menü Rapor", command=lambda: modernFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    modern.place(x=794, y=200)
    kola = Button(personelEkran)
    kola.config(text="Kola Rapor", command=lambda: kolaFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    kola.place(x=25, y=250)
    fanta = Button(personelEkran)
    fanta.config(text="Fanta Rapor", command=lambda: fantaFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    fanta.place(x=275, y=250)
    icetea = Button(personelEkran)
    icetea.config(text="Ice Tea Rapor", command=lambda: iceteaFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    icetea.place(x=525, y=250)
    limonata = Button(personelEkran)
    limonata.config(text="Limonata Rapor", command=lambda: limonataFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    limonata.place(x=775, y=250)
    ayran = Button(personelEkran)
    ayran.config(text="Ayran Rapor", command=lambda: ayranFonk(veritab,personelEkran,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    ayran.place(x=1025, y=250)
    
    mycursor.execute("SELECT * FROM siparisler")
    data = mycursor.fetchall()
    columns = ["SiparişId","Ad","Soyad","Seçilen Menü","Sipariş Adeti","İçecek","İçecek Adeti","Toplam","Siparişte Katalog Var Mı", "Adres","Sipariş Tarihi", "Email"]
    frame =Frame(personelEkran, width=500,height=150)
    frame.pack(side="bottom")
    treeview_olustur(master=frame, columns=columns, data=data,width=330)

def gelenekselFonk(veritab,personelEkran,my_image):
    gelenekselRapor = Toplevel(personelEkran)
    gelenekselRapor.title("Personel Arayüzü")
    gelenekselRapor.geometry("1280x600+20+0")
    gelenekselRapor.resizable(FALSE, FALSE)
    arkaplan = Label(gelenekselRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT menu, SUM(menu_adet) as 'menü adeti' FROM siparisler WHERE menu = 'Geleneksel Menü'")
    data = mycursor.fetchall()
    columns = ["Menü", "Satılan Adet"]
    treeview_olustur(master=gelenekselRapor, columns=columns, data=data,width=550)

def kisFonk(veritab,personelEkran,my_image):
    kisRapor = Toplevel(personelEkran)
    kisRapor.title("Personel Arayüzü")
    kisRapor.geometry("1280x600+20+0")
    kisRapor.resizable(FALSE, FALSE)
    arkaplan = Label(kisRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT menu, SUM(menu_adet) as 'menü adeti' FROM siparisler WHERE menu = 'Kış Menü'")
    data = mycursor.fetchall()
    columns = ["Menü", "Satılan Adet"]
    treeview_olustur(master=kisRapor, columns=columns, data=data,width=550)

def modernFonk(veritab,personelEkran,my_image):
    modernRapor = Toplevel(personelEkran)
    modernRapor.title("Personel Arayüzü")
    modernRapor.geometry("1280x600+20+0")
    modernRapor.resizable(FALSE, FALSE)
    arkaplan = Label(modernRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT menu, SUM(menu_adet) as 'menü adeti' FROM siparisler WHERE menu = 'Modern Sofra Menü'")
    data = mycursor.fetchall()
    columns = ["Menü", "Satılan Adet"]
    treeview_olustur(master=modernRapor, columns=columns, data=data,width=550)

def kolaFonk(veritab,personelEkran,my_image):
    kolaRapor = Toplevel(personelEkran)
    kolaRapor.title("Personel Arayüzü")
    kolaRapor.geometry("1280x600+20+0")
    kolaRapor.resizable(FALSE, FALSE)
    arkaplan = Label(kolaRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT icecek, SUM(icecek_adet) as 'İçecek adeti' FROM siparisler WHERE icecek = 'KOLA'")
    data = mycursor.fetchall()
    columns = ["İçecek", "Satılan Adet"]
    treeview_olustur(master=kolaRapor, columns=columns, data=data,width=550)
def fantaFonk(veritab,personelEkran,my_image):
    fantaRapor = Toplevel(personelEkran)
    fantaRapor.title("Personel Arayüzü")
    fantaRapor.geometry("1280x600+20+0")
    fantaRapor.resizable(FALSE, FALSE)
    arkaplan = Label(fantaRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT icecek, SUM(icecek_adet) as 'İçecek adeti' FROM siparisler WHERE icecek = 'FANTA'")
    data = mycursor.fetchall()
    columns = ["İçecek", "Satılan Adet"]
    treeview_olustur(master=fantaRapor, columns=columns, data=data,width=550)
def iceteaFonk(veritab,personelEkran,my_image):
    iceteaRapor = Toplevel(personelEkran)
    iceteaRapor.title("Personel Arayüzü")
    iceteaRapor.geometry("1280x600+20+0")
    iceteaRapor.resizable(FALSE, FALSE)
    arkaplan = Label(iceteaRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT icecek, SUM(icecek_adet) as 'İçecek adeti' FROM siparisler WHERE icecek = 'ICE TEA'")
    data = mycursor.fetchall()
    columns = ["İçecek", "Satılan Adet"]
    treeview_olustur(master=iceteaRapor, columns=columns, data=data,width=550)
def limonataFonk(veritab,personelEkran,my_image):
    limonataRapor = Toplevel(personelEkran)
    limonataRapor.title("Personel Arayüzü")
    limonataRapor.geometry("1280x600+20+0")
    limonataRapor.resizable(FALSE, FALSE)
    arkaplan = Label(limonataRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT icecek, SUM(icecek_adet) as 'İçecek adeti' FROM siparisler WHERE icecek = 'LIMONATA'")
    data = mycursor.fetchall()
    columns = ["İçecek", "Satılan Adet"]
    treeview_olustur(master=limonataRapor, columns=columns, data=data,width=550)
def ayranFonk(veritab,personelEkran,my_image):
    ayranRapor = Toplevel(personelEkran)
    ayranRapor.title("Personel Arayüzü")
    ayranRapor.geometry("1280x600+20+0")
    ayranRapor.resizable(FALSE, FALSE)
    arkaplan = Label(ayranRapor, image=my_image)
    arkaplan.place(x=0, y=0)
    personelEkran.iconbitmap("YICO.ico")
    mycursor=veritab.cursor()
    mycursor.execute("SELECT icecek, SUM(icecek_adet) as 'İçecek adeti' FROM siparisler WHERE icecek = 'AYRAN'")
    data = mycursor.fetchall()
    columns = ["İçecek", "Satılan Adet"]
    treeview_olustur(master=ayranRapor, columns=columns, data=data,width=550)



    



def personelgirisYap(veritab, mycursor, isim, sifre,personelekrangiris,my_image):
    def kullanici_giris(tup):
        mycursor.execute("SELECT * FROM personel WHERE mail=%s AND sifre=%s", tup) 
        return (mycursor.fetchall())

    data = (
        isim.get(),
        sifre.get()
    )

    if isim.get() == "":
        messagebox.showinfo("Uyarı", "Önce maili giriniz!")
    elif sifre.get() == "":
        messagebox.showinfo("Uyarı", "Önce şifreyi giriniz!")
    else:
        res = kullanici_giris(data)
        if res:
            messagebox.showinfo("Uyarı", "Giriş Başarılı!")
            personelekran(veritab,isim, mycursor,personelekrangiris,my_image)
        else:
            messagebox.showinfo("Uyarı", "Eposta/Şifre Hatalı!")


def personelgirisi(veritab,ekran):
    ekran.destroy()
    personelekrangiris=Tk()
    personelekrangiris.title("Personel Ekranı")
    personelekrangiris.geometry("1280x600+20+0")
    personelekrangiris.resizable(FALSE, FALSE)
    my_image = ImageTk.PhotoImage(Image.open("bgimage.jpg"))
    arkaplan = Label(master=personelekrangiris, image=my_image)
    arkaplan.place(x=0, y=0)
    personelekrangiris.iconbitmap("YICO.ico")
    mycursor = veritab.cursor()
    isimSor = Label(personelekrangiris, text="Mail :",font="30", width=15, bg="#2a1415" ,fg="#b89073" )
    isimSor.place(x=430,y=210)

    isim = Entry(personelekrangiris ,font="30", bg="#b89073")
    isim.place(x=628,y=210)

    sifreSor = Label(personelekrangiris, text="Şifreniz(Max:8) :  ", font="30", width=15 ,bg="#2a1415" ,fg="#b89073"  )
    sifreSor.place(x=430, y=250)

    def limitSizePas(*args):
        value = sifresinir.get()
        if len(value) > 8: sifresinir.set(value[:8])
    sifresinir = StringVar()
    sifresinir.trace('w', limitSizePas)

    sifre = Entry(personelekrangiris, show="*",textvariable=sifresinir ,font="30" , width=20 , bg="#b89073")
    sifre.place(x=628, y=250)

    buton = Button(personelekrangiris)
    buton.config(text="Giriş yap!", command=lambda: personelgirisYap(veritab, mycursor, isim, sifre,personelekrangiris,my_image), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    buton.place(x=510, y=290)


    personelekrangiris.mainloop()





def main():
    veritab = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="catering"
)
    mycursor = veritab.cursor()
    ekran = Tk()
    ekran.title("Catering Sistemi")
    ekran.geometry("1280x600+20+0")
    ekran.resizable(FALSE, FALSE)
    menubar(ekran)
    my_image = ImageTk.PhotoImage(Image.open("bgimage.jpg"))
    arkaplan = Label(ekran, image=my_image)
    arkaplan.place(x=0, y=00)
    ekran.iconbitmap("YICO.ico")
    karsilama = Label(ekran)
    karsilama.config(text="Catering Sistemimize Hoş Geldiniz", font="25",width=38 , bg="#2a1415" ,fg="#b89073" )
    karsilama.place(x=430, y=170)

    isimSor = Label(ekran, text="Mail :",font="30", width=15, bg="#2a1415" ,fg="#b89073" )
    isimSor.place(x=430,y=210)

    isim = Entry(ekran ,font="30", bg="#b89073" , border="0")
    isim.place(x=628,y=210)

    sifreSor = Label(ekran, text="Şifreniz(Max:8) :  ", font="30", width=15 ,bg="#2a1415" ,fg="#b89073"  )
    sifreSor.place(x=430, y=250)

    def limitSizePas(*args):
        value = sifresinir.get()
        if len(value) > 8: sifresinir.set(value[:8])
    sifresinir = StringVar()
    sifresinir.trace('w', limitSizePas)

    sifre = Entry(ekran, show="*",textvariable=sifresinir ,font="30" , width=20 , bg="#b89073", border="0")
    sifre.place(x=628, y=250)

    buton = Button(ekran)
    buton.config(text="Giriş Yap", command=lambda: girisYap(veritab, mycursor, isim, sifre, ekran), font="30"
                 , width=23 ,bg="#502b26" ,fg="#b89073" )
    buton.place(x=510, y=290)

    uye = Button(ekran)
    uye.config(text="Üye Ol", command=lambda: uyeol(veritab, ekran, my_image),font="30",
               width=23, bg="#502b26" ,fg="#b89073" )
    uye.place(x=510, y=335 )
    personel = Button(ekran)
    personel.config(text="Personel Girişi", command=lambda : personelgirisi(veritab,ekran),font="30",width=23, bg="#502b26" ,fg="#b89073" )
    personel.place(x=1000,y=30)
    ekran.mainloop()






main()
