# DerinOgrenme

Öğrenci Numarası: 427627
Adı: Emre
Soyadı: Küçük
GitHub Linki: https://github.com/emrekucuk41/DerinOgrenme
MEME KANSERİ (BREAST CANCER WISCONSIN) SINIFLANDIRMA PROJESİ RAPORU

1. Algoritma Seçimi ve Gerekçesi Bu çalışmada, iyi huylu (benign) ve kötü huylu (malignant) tümörleri sınıflandırmak için makine öğrenmesi algoritmalarından Rastgele Orman (Random Forest) sınıflandırıcısı tercih edilmiştir. Rastgele Orman algoritmasının seçilmesinin temel nedenleri; çok sayıda karar ağacını bir araya getirerek (ensemble) aşırı öğrenme (overfitting) riskini azaltması, veri setindeki (yarıçap, alan, doku vb.) karmaşık özellikler arasındaki doğrusal olmayan ilişkileri çok iyi modelleyebilmesi ve medikal teşhis gibi kritik problemlerde genellikle yüksek doğruluk ve stabilite sunmasıdır.
2. İşlem Adımları Projenin gerçekleştirilmesi aşamasında aşağıdaki adımlar izlenmiştir:
   • Veri Yükleme ve Temizleme: data.csv dosyası projeye dahil edilmiş, modelin öğrenmesini engelleyecek olan gereksiz id sütunu ve boş sütunlar veri setinden çıkarılmıştır.
   • Etiket Dönüşümü: Hedef değişken olan diagnosis (teşhis) sütunundaki 'M' (Malignant) değerleri 1, 'B' (Benign) değerleri ise 0 olarak sayısal formata dönüştürülmüştür.
   • Veri Bölme: Veri seti %80 eğitim ve %20 test verisi olacak şekilde ikiye ayrılmıştır. Bölme işlemi sırasında sınıf dengesinin korunması için stratify parametresi kullanılmıştır.
   • Veri Ölçeklendirme (Standardization): Veri setindeki özelliklerin değer aralıkları (örneğin alan değeri yüzlerdeyken pürüzsüzlük değeri ondalıklıdır) birbirinden çok farklı olduğu için modeli yanıltmaması adına StandardScaler kullanılarak tüm özellikler standartlaştırılmıştır.
   • Model Eğitimi: Random Forest modeli 100 karar ağacı (n_estimators=100) ile eğitim verisi kullanılarak eğitilmiştir.

3. Değerlendirme Metrikleri ve Sonuçlar Eğitilen model test verisi üzerinde denenmiş ve aşağıdaki performans metrikleri elde edilmiştir:
   • Accuracy (Doğruluk): %97.37
   • Precision (Kesinlik): %100.00
   • Recall (Duyarlılık): %92.86
   • F1-Score: %96.30
   Değerlendirme: Model genel olarak %97.37 oranında doğru tahmin yapmıştır. Kesinlik (Precision) değerinin %100 olması, modelin "kötü huylu" dediği tüm tümörlerin gerçekten kötü huylu olduğunu, yani yanlış pozitif (False Positive) tahmini yapmadığını göstermektedir. %92.86'lık Duyarlılık (Recall) değeri ise, gerçekte kötü huylu olan tümörlerin büyük çoğunluğunu başarıyla tespit edebildiğini ortaya koymaktadır. Yüksek F1-Score değeri (%96.30), modelin dengeli ve tıbbi bir veri seti için oldukça güvenilir bir sınıflandırma performansı sergilediğini kanıtlamaktadır.
