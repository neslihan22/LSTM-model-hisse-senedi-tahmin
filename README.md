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










