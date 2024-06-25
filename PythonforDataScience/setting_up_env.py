print("hello world")
print("Hello ai"),
9
a=10
c="merve"
#sanal ortamların listelenmesi
#conda env list

#sanal ortam oluşturma
#conda create -n env_name


#sanal ortamı aktif etme
#conda activate env_name

#kütüphane yükleme
#conda install numpy scipy pandas

#paket silme
#conda remove package_name

#belirli bir versiyona göre paket yükleme
#conda install numpy=1.26.3

#paket yükseltme-> en güncel versiyona gider
#conda upgrade numpy

#tüm kütüphaneleri yükseltmek için
#conda upgrade -all

#pip:pypi (python package index) paket yönetim aracı
#pip install paket_adi

#versiyona göre
#pip install pandas==2.2

#paketleri aktarmak yaml dosyası aracılığı ile
#conda env export > environment.yaml

#environment silmek için base de
#conda env remove -n env_name

#aynı paketlerle ortam oluşturmak için, aynı isimle ortam oluşturur
#conda env create -f environment.yaml