Öğrenci Numarası: 427627
Adı: Emre
Soyadı: Küçük
GitHub Linki: https://github.com/emrekucuk41/DerinOgrenme

XOR PROBLEMİNİN YAPAY SİNİR AĞLARI İLE ÇÖZÜLMESİ PROJESİ RAPORU

1. Algoritma Seçimi ve Gerekçesi
   Bu çalışmada, tek katmanlı algılayıcıların (Single-Layer Perceptron) çözemediği XOR problemini çözmek için Çok Katmanlı Yapay Sinir Ağı (Multi-Layer Perceptron - MLP) mimarisi tercih edilmiştir. XOR kapısı çıktılarının iki boyutlu düzlemde tek bir doğru ile birbirinden ayrılamaması (doğrusal olarak ayrılamaz - non-linearly separable olması) geleneksel yöntemleri yetersiz kılmaktadır. Bu mimarinin seçilmesinin temel nedeni, araya eklenen "gizli katman" (hidden layer) ve doğrusal olmayan "ReLU" aktivasyon fonksiyonu sayesinde ağın karmaşık veri yapılarını öğrenebilmesi ve doğrusal olmayan problemleri yüksek doğrulukla modelleyebilmesidir.

2. İşlem Adımları
   Projenin gerçekleştirilmesi aşamasında Python ve TensorFlow/Keras kütüphaneleri kullanılarak aşağıdaki adımlar izlenmiştir:

Veri Seti Hazırlığı: XOR probleminin 4 farklı girdi durumu (0-0, 0-1, 1-0, 1-1) ve bu durumlara karşılık gelen beklenen çıktılar (0, 1, 1, 0) NumPy dizileri olarak tanımlanmıştır.

Model Mimarisinin Kurulması: Sequential API kullanılarak model inşa edilmiştir. Modelin veri uzayını bükebilmesi için 2 girdili ve 16 nörona sahip, 'ReLU' aktivasyon fonksiyonlu bir gizli katman eklenmiştir. Çıktı katmanında ise ikili sınıflandırma (0 veya 1) yapılacağı için 'Sigmoid' fonksiyonuna sahip tek bir nöron kullanılmıştır.

Modelin Derlenmesi (Compilation): Kayıp (loss) fonksiyonu olarak ikili sınıflandırmalarda en iyi sonucu veren binary_crossentropy, optimizasyon algoritması olarak ise adam seçilmiştir.

Model Eğitimi: Ağın hata payını en aza indirmesi ve ağırlıkları doğru güncelleyebilmesi için model 1000 iterasyon (epoch) boyunca eğitilmiştir.

3. Değerlendirme Metrikleri ve Sonuçlar
   Eğitilen model, XOR girdileri üzerinde test edilmiş ve aşağıdaki sonuçlar elde edilmiştir:

Doğruluk (Accuracy): %100.00

Ağın Olasılık Çıktıları: Model; [0,0] ve [1,1] girdileri için sıfıra çok yakın olasılıklar (0.14 ve 0.06), [0,1] ve [1,0] girdileri için ise bire çok yakın olasılıklar (0.93) üreterek beklenen değerleri kusursuz şekilde yakalamıştır.

Grafik Değerlendirmesi: Raporun sonundaki görsellerde yer alan Öğrenme Süreci (Loss Curve) grafiği, modelin eğitim boyunca hata payını düzenli olarak düşürdüğünü kanıtlamaktadır. XOR Karar Sınırı (Decision Boundary) grafiği ise, modelin veriyi sadece düz bir çizgi ile değil, doğrusal olmayan karmaşık bir sınır çizerek (kırmızı ve mavi bölgeler) başarıyla sınıflandırdığını net bir şekilde göstermektedir.

GÖRSEL EKLER
Figure_1.png
