### Nama : Hadi Sahrul Fauzi
### Nim : 211351060
### Kelas : Malam A

## Domain Proyek

Prediksi kualitas susu merupakan salah satu aplikasi yang dapat memberikan manfaat bagi industri pengolahan susu. Dengan adanya aplikasi ini, produsen dapat mengetahui kualitas susu sebelum diolah sehingga dapat mengambil tindakan yang tepat untuk meningkatkan kualitas susu.

## Business Understanding

Dalam langkah pertama, kita akan fokus pada pemahaman aplikasi yang bertujuan untuk memprediksi kualitas susu. Tahap ini akan membantu kita mengidentifikasi, merinci, dan memahami secara lebih mendalam masalah yang perlu diatasi oleh aplikasi tersebut.

### Problem Statements
Berikut adalah beberapa masalah yang dapat diatasi dengan aplikasi prediksi kualitas susu: 

- Kesulitan dalam mengidentifikasi faktor-faktor yang mempengaruhi kualitas susu, yang dapat mengarah pada manajemen kualitas yang tidak tepat.
- Kurangnya dukungan dalam mengarahkan produsen pada tindakan perbaikan yang sesuai, seperti peningkatan kualitas bahan baku, proses pengolahan, atau penyimpanan.
- Keterlambatan dalam deteksi kualitas susu yang rendah, yang berpotensi mengakibatkan penurunan kualitas produk susu.

### Goals

Berikut adalah beberapa tujuan dari aplikasi prediksi kualitas susu:

- Meningkatkan identifikasi faktor-faktor yang mempengaruhi kualitas susu untuk pengelolaan kualitas yang lebih tepat.
- Memberikan rekomendasi yang lebih tepat dalam perbaikan kualitas susu, termasuk peningkatan kualitas bahan baku, proses pengolahan, atau penyimpanan.
- Meningkatkan deteksi kualitas susu yang rendah sehingga dapat meningkatkan kualitas produk susu yang baik.

### Solution statements
- Melakukan analisis data yang mendalam untuk mengidentifikasi pola dan tren yang berkaitan dengan kualitas susu. Ini dapat mencakup analisis statistik dan penggunaan teknik seperti data mining.
- Aplikasi prediksi kualitas susu akan memanfaatkan data susu yang relevan, termasuk faktor-faktor yang mempengaruhi kualitas susu, seperti kualitas bahan baku, proses pengolahan, dan penyimpanan. Data ini akan digunakan untuk melatih model machine learning yang dapat memprediksi kualitas susu.
- Model yang dihasilkan dari datasets itu menggunakan model K-Nearest Neighbor (KNN).

## Data Understanding
Dataset ini dikumpulkan secara manual dari observasi. Hal ini membantu kami membuat model pembelajaran mesin untuk memprediksi kualitas susu.
Dataset ini terdiri dari 8 variabel independen yaitu pH, Suhu, Rasa, Bau, Lemak, Kekeruhan, Warna dan Kualitas. Umumnya, Kualitas atau Kualitas susu bergantung pada parameter-parameter ini. Parameter ini memainkan peran penting dalam analisis prediktif susu. Dataset susu berisi 429 contoh kualitas buruk, 374 contoh kualitas menengah, dan 256 contoh kualitas baik.

[Milk Quality Prediction] (https://www.kaggle.com/datasets/cpluzshrijayan/milkquality).


### Variabel-variabel pada Milk Quality Prediction Dataset adalah sebagai berikut:
- **pH**            : Fitur ini menentukan pH susu, yang berada pada kisaran 3 hingga 9,5. [float64] 
- **temperature**   : Fitur ini menentukan suhu susu, dan kisarannya adalah dari 34'C hingga 90'C.[int64] 
- **taste**         : Fitur ini mendefinisikan rasa susu dan mengambil nilai yang mungkin: 1 (baik) atau 0 (buruk).[int64] 
- **odor**          : Fitur ini mendefinisikan bau susu dan mengambil nilai yang mungkin: 1 (baik) atau 0 (buruk).[int64] 
- **fat**           : Fitur ini mendefinisikan kandungan lemak susu dan mengambil nilai yang mungkin: 1 (Tinggi) atau 0 (Rendah).[int64] 
- **turbidity**     : Fitur ini menentukan kekeruhan susu dan mengambil nilai yang mungkin: 1 (Tinggi) atau 0 (Rendah).[int64] 
- **colour**        : Fitur ini menentukan warna susu, yang berkisar antara 240 hingga 255.[int64] 
- **grade**         : Ini adalah target dan mengambil nilai: kualitas_rendah, kualitas_sedang, atau kualitas_tinggi.[object] 


## Data Preparation
Pada tahap ini, saya menggunakan metode EDA untuk melakukan preparasi data.
### Data Collection
Untuk data collection ini, saya mendapatkan dataset dari website kaggle dengan nama dataset [Milk Quality Prediction](https://www.kaggle.com/datasets/cpluzshrijayan/milkquality). jika anda tertarik dengan datasetnya, anda bisa click link tersebut.

### Data Discovery And Profiling
Karena kita menggunakan google colab untuk mengerjakannya maka kita akan import files,
``` bash
from google.colab import files
files.upload()
```
Setelah mengupload filenya, maka kita akan lanjut dengan membuat sebuah folder untuk menyimpan file kaggle.json yang sudah diupload tadi,
``` bash
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```
Lalu mari kita download datasetsnya,
``` bash
!kaggle datasets download -d cpluzshrijayan/milkquality
```
Selanjutnya kita harus extract file yang tadi telah didownload,
``` bash
!mkdir milkquality
!unzip milkquality.zip -d milkquality
!ls milkquality
```
Kita mengimport semua library yang dibutuhkan, 
``` bash
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,confusion_matrix
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```
Lanjut dengan memasukkan file csv yang telah diextract pada sebuah variable
```bash
data = pd.read_csv('milkquality/milknew.csv')
```
Lalu melihat 5 data paling atas dari datasetsnya,
```bash
data.head(5)
```
Kemudian saya akan melihat tipe data yang ada pada masing-masing kolom pada dataset tersebut dengan perintah,
``` bash
data.info()
```
Disini saya merubah typedata 'pH' yang awalnya float menjadi integer
``` bash
data.pH=data.pH.astype("int64")
```
kita lihat typedata yang sudah dirubah
``` bash
data.info()
```
## EDA
Buat Korelasi heatmap
``` bash
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
```
![](./assets/heatmap.png) <br>

Kita lihat jumlah data kualitas susu berdasarkan ph nya
``` bash
sns.countplot(x=data['pH'],hue=data['Grade'], palette = "tab10")
```
![](./assets/counplot1.png) <br>

Kita lihat jumlah data kualitas susu berdasarkan Odor nya
``` bash
sns.countplot(x=data['Odor'],hue=data['Grade'], palette = "tab10")
```
![](./assets/counplot2.png) <br>

Kita visualisasikan data 'pH' dan 'colour' menggunakan scatterplot
``` bash
sns.scatterplot(data=data, x='pH', y='Colour', hue='Grade')
```
![](./assets/scaterplot.png) <br>

Kita lihat jumlah data kualitas susu berdasarkan Turbidity nya
``` bash
sns.pairplot(data,hue='Grade');
```
![](./assets/pairplot.png) <br>

Kita visualisasikan data 'Grade' menggunakan diagram lingkaran atau pie untuk melihat persentase datanya,
``` bash
plt.figure(figsize=(30,10))
plt.pie(data['Grade'].value_counts(), labels=data['Grade'].value_counts().index,
          autopct='%1.1f%%', textprops={ 'fontsize': 15,
                                        'color': 'black',
                                        'weight': 'bold',
                                        'family': 'serif' })
hfont = {'fontname':'serif', 'weight': 'bold'}
plt.show()
```
![](./assets/pie.png) <br>

## Prepocessing
Lalu lakukan pemisahan data menjadi variabel dependen (target) dan variabel independen (fitur) yang umum dalam pemodelan data. Dalam hal ini, y akan menjadi target atau label, dan x akan menjadi fitur atau atribut yang digunakan untuk memprediksi target,
``` bash
features = ['pH','Temprature','Taste','Odor','Fat ','Turbidity','Colour']
x = data[features]
y = data['Grade']
x.shape, y.shape
``` 
Selanjutnya kita akan menentukan berapa persen dari datasets yang akan digunakan untuk test dan untuk train
``` bash
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=90)
y_test.shape
```
## Modeling

membuat, melatih, dan mengukur akurasi model menggunakan  K-Nearest Neighbor (KNN)
``` bash
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)
y_pred1=model.predict(x_test)
```

Mengukur akurasi model  K-Nearest Neighbor (KNN) pada seluruh dataset,
``` bash
score = model.score(x_test, y_test)
print('akurasi model knn = ', score)
```
Ternyata mendapatkan score akurasi model knn =  0.9509433962264151 95%

Saya akan coba lakukan pengetesan menggunakan data dumy seperti dibawah ini
``` bash
input_data = np.array([[6.6, 37, 0, 0, 0, 0, 255]])

prediction = model.predict(input_data)
print('Prediksi Kualitas susu:', prediction)
```
Prediksi kualitas susu : ['medium']

Setelah pengetesan berhasil, dan modelnya sudah selesai dibuat, kita akan export sebagai sav agar nanti bisa kita gunakan pada project web streamlit kita.
``` bash
import pickle

filename = "prediksi_milk.sav"
pickle.dump(rf,open(filename,'wb'))
```

## Evaluation
Matrik evaluasi yang saya gunakan disini adalah confusion matrix, karena sangat cocok untuk kasus pengkategorian seperti kasus ini. Dengan membandingkan nilai aktual dengan nilai prediksi.
``` bash
lr= linear_model.LogisticRegression(random_state = 42,max_iter= 100)
knn_preds = lr.fit(x_train, y_train).predict(x_test)
cm = confusion_matrix(y_test,rf_preds)

ax= plt.subplot()
sns.heatmap(cm, annot=True, fmt='g', ax=ax);
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax.set_title('Confusion Matrix');
ax.xaxis.set_ticklabels(['low','medium','high']); ax.yaxis.set_ticklabels

```
![](./assets/evaluasi.png) <br>



## Deployment
Berikut adalah aplikasi prediksi kualitas susu yang sudah saya buat menggunakan Streamlit
[My Milk Quality Prediction App](https://prediksi-susu.streamlit.app/).

![](./assets/app.png)



