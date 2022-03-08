import matplotlib.pyplot as plt
import cv2
import numpy as np

class histogram:
    def __init__(self,gambar:str):
        self.gambar = gambar

    #ekstrak pixel dari gambar
    def getPixel(self):
        self.pic = cv2.imread(self.gambar)
        self.pic_togrey = cv2.cvtColor(self.pic, cv2.COLOR_RGB2GRAY)
        #self.resize = cv2.resize(self.pic_togrey,(500,500)) #to resize image
        return self.pic_togrey #change the return to self.resize if you resize the image

    def pencerahanGambar (self, value:int, terang=True):
        if terang:
            pix = self.getPixel()
            ukuran = pix.shape
            for i in range(ukuran[0]):
                for j in range(ukuran[1]):
                    temp=pix[i][j]+value
                    if temp>255:
                        pix[i][j]=255
                    elif temp<0:
                        pix[i][j]=0
                    else:
                        pix[i][j]=temp
            return pix
        else:
            pix = self.getPixel()
            ukuran = pix.shape
            for i in range(ukuran[0]):
                for j in range(ukuran[1]):
                    temp = pix[i][j] - value
                    if temp > 255:
                        pix[i][j] = 255
                    elif temp < 0:
                        pix[i][j] = 0
                    else:
                        pix[i][j] = temp
            return pix

    def kontras (self, value, pixels):
        ar = pixels
        ukuran = ar.shape
        for i in range(ukuran[0]):
            for j in range(ukuran[1]):
                temp = ar[i][j] * value
                if temp > 255:
                    ar[i][j] = 255
                elif temp < 0:
                    ar[i][j] = 0
                else:
                    ar[i][j] = temp
        return ar

    def kombinasiCerahKontras(self, valueCerah, valueKontras, terang=True):
        a = self.pencerahanGambar(valueCerah,terang)
        b = self.kontras(valueKontras, a)
        return b

    def membalikCitra(self, pixels):
        ar = np.array(pixels)
        ukuran = ar.shape
        for i in range(ukuran[0]):
            for j in range(ukuran[1]):
                temp = 255-ar[i][j]
                if temp > 255:
                    ar[i][j] = 255
                elif temp < 0:
                    ar[i][j] = 0
                else:
                    ar[i][j] = temp
        return ar

    def pemetaanNonlinier(self, pixels):
        c = np.array(pixels)
        d = np.float_(c)
        c2 = np.log(1+d)
        out = np.zeros(c2.shape, np.double)
        normal = cv2.normalize(c2, out,1,0,cv2.NORM_MINMAX)

        return normal

    def showPicture(self,winname:str, pixels):
        self.show = cv2.imshow(winname, pixels)
        cv2.waitKey(0)

    def get_histogram(self, pixels):
        test = []
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                test.append(round(pixels[i][j]))
        plt.hist(test, bins=max(test) ,range= [0,256])
        plt.show()


#pencerahan gambar
#ambil nilai piksel dari gambar asli
picture = histogram('pict.jpg')
pixels = picture.getPixel() #dapatkan pixel dari gambar original
showOri = picture.showPicture('before_pencerahan', pixels) #menampilkan gambar sebelum
histogramOri = picture.get_histogram(pixels=pixels) #menampilkan histogram dari gambar asli

#proses pencerahan
pencerahan_gambar = picture.pencerahanGambar(60) #nilai pixel setelah dicerahkan
show_pencerahan = picture.showPicture('Pencerahan Gambar', pencerahan_gambar) #menampilkan gambar sesudah pencerahan
getHistogram = picture.get_histogram(pencerahan_gambar) #histogram gambar sesudah pencerahan

#Proses Kontras
kontras = picture.kontras(3,pixels)
show_kontras = picture.showPicture('Kontras', kontras)
histoKontras = picture.get_histogram(kontras)

#proses Kombinasi cerah kontras
kombinasi = picture.kombinasiCerahKontras(30, 3, False) #kombinasi menggelapkan gambar dan kontras
show_kombinasi = picture.showPicture('Kombinasi', kombinasi)
histoKombinasi = picture.get_histogram(kombinasi)

#proses Membalik citra
balikCitra = picture.membalikCitra(pixels)
show_balikCitra = picture.showPicture('Balik Citra', balikCitra)
histoBalik = picture.get_histogram(balikCitra)

#proses pemetaan nonlinier
nonLinier = picture.pemetaanNonlinier(pixels)
show_nonLinier = picture.showPicture('nonLinier',nonLinier)
histoNonLinier = picture.get_histogram(nonLinier)












