
This code trains a neural network using past Netflix 'Adj Close' (Adjusted Close) prices to predict future prices. The model is structured with LSTM layers to learn dependencies in the time series data based on historical prices.

Main Steps:

Data Preprocessing:
The dataset is loaded, the "Date" column is converted to a date format, and it is set as the index of the DataFrame. Only the "Adj Close" column is selected for analysis. MinMax scaling is applied to normalize the data.

Training and Test Data Split:
The dataset is split into training (80%) and test (20%) sets. A create_dataset function is defined to create input-output pairs using a specific time step (60 days in this case).

Model Definition:
An LSTM model is defined using Keras' Sequential API. The model consists of two LSTM layers to process the time series data, Dropout layers to prevent overfitting, and a Dense layer as the output layer to produce a single value.

Model Training Outputs:
The model was trained for 50 epochs, and the average loss value consistently decreased during each epoch. This indicates that the model continued learning from the data and improved its fit to the training set. The final loss value reached approximately 5.45×10⁻⁵, which is a very low value, indicating high prediction performance.

Prediction Graph:
After comparing the model’s predictions with the actual values on the test data, the results were visualized. In the graph, the green line represents the actual stock prices, and the red line represents the predicted values from the model. Upon examining the graph, it was observed that the model's predictions closely matched the actual values. This suggests that the model performed well on the test data and was able to make predictions close to the real values. However, some minor deviations were present, which is normal for volatile data like stock prices. The LSTM model successfully captured the overall trends but did not perfectly match some sudden price changes.

Based on these results, I am satisfied with the model’s performance. The alignment of predictions with the actual data indicates that the model can successfully forecast stock prices. I also consider experimenting with different hyperparameter settings or alternative models to achieve higher accuracy.




TURKISH:



Bu kod, geçmiş Netflix 'Adj Close' (Düzeltilmiş Kapanış) fiyatlarını kullanarak gelecekteki fiyatları tahmin etmek için bir sinir ağı eğitir. Model, zaman serisi verilerindeki geçmişe dayalı bağımlılıkları öğrenmek için LSTM katmanları ile yapılandırılmıştır.

Ana Adımlar:
Veri Ön İşleme: Veri yükleme, ölçekleme ve model eğitimi için verilerin şekillendirilmesi.
Model Eğitimi: Geçmiş fiyatlara dayalı olarak gelecekteki fiyatları tahmin etmek için bir LSTM modelinin oluşturulması.
Değerlendirme ve Görselleştirme: Modelin tahminlerini gerçek hisse fiyatları ile karşılaştırarak görselleştirme.

Aşamalar:
Veri Yükleme ve Ön İşleme

Veri kümesini yükler, Date sütununu tarih formatına dönüştürür ve veri çerçevesi için indeks olarak ayarlar.
Analiz için yalnızca Adj Close sütununu seçer.
Veriyi normalize etmek için MinMax ölçeklendirmesi uygular.
Eğitim ve Test Verisinin Bölünmesi

Veri kümesini eğitim (%80) ve test (%20) olarak böler.
Belirli bir zaman adımı (burada 60 gün) kullanarak girdi-çıktı çiftleri oluşturmak için create_dataset fonksiyonunu tanımlar.
Model Tanımlama

Keras'ın Sequential API'sini kullanarak bir LSTM modeli tanımlar. Model şunlardan oluşur:
Zaman serisi verisini işlemek için iki LSTM katmanı ve aşırı uyumu (overfitting) önlemek için Dropout katmanları
Sonuç katmanı olarak tek bir çıkış değeri üreten Dense katmanı

Model Eğitimi Çıktıları:

Modeli 50 epoch boyunca eğittim ve her epoch'ta ortalama kayıp değeri (loss) istikrarlı bir şekilde azaldı. Bu durum, modelin verilerden öğrenmeye devam ettiğini ve eğitim setine daha iyi uyum sağladığını gösteriyor.
Son epoch'ta kayıp değeri yaklaşık olarak 
5.45×10üzeri−5 seviyesine düştü. Bu oldukça düşük bir değer, bu yüzden modelin tahmin performansının yüksek olmasını bekliyorum.
Tahmin Grafiği:

Test verileri üzerinde modelin tahminleri ile gerçek değerleri karşılaştırdığımda, sonuçları görselleştirdim. Grafikte yeşil çizgi gerçek hisse senedi fiyatlarını, kırmızı çizgi ise modelin tahmin ettiği değerleri temsil ediyor.
Grafiği incelediğimde, modelin tahminlerinin gerçek değerlere oldukça yakın olduğunu gözlemledim. Bu durum, modelin test verisi üzerindeki performansının genel olarak iyi olduğunu ve gerçek değerlere yakın tahminler yapabildiğini gösteriyor.
Yine de bazı küçük sapmalar mevcut; özellikle hisse senedi gibi volatiliteye sahip verilerde bu tür sapmalar normaldir. LSTM modeli genel trendleri başarılı bir şekilde yakaladı ancak bazı ani fiyat değişimlerinde tam olarak eşleşemedi.
Bu sonuçlara dayanarak, modelin performansından memnunum. Tahminlerin gerçek verilerle uyumlu olması, modelin hisse senedi fiyatlarını başarılı bir şekilde öngörebildiğini gösteriyor. Daha yüksek doğruluk elde etmek için farklı hiperparametre ayarları veya alternatif modeller denemeyi de düşünüyorum.










