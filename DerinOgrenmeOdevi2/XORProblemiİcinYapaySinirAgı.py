import numpy as np
import matplotlib.pyplot as plt
import os

# Terminaldeki gereksiz TensorFlow loglarini gizlemek icin
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# 1. VERI SETI (Data)
X = np.array([[0, 0], 
              [0, 1], 
              [1, 0], 
              [1, 1]])

y = np.array([[0], 
              [1], 
              [1], 
              [0]])

# 2. MODEL OLUSTURMA (Pro Yapi)
model = Sequential()
model.add(Input(shape=(2,))) # Uyari almamak icin Input katmani
model.add(Dense(units=16, activation='relu')) # Gizli katman (Daha hizli ogrenmesi icin noron sayisini 16 yaptik)
model.add(Dense(units=1, activation='sigmoid'))

# 3. DERLEME
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. EGITIM
print("Model egitiliyor... Lutfen bekleyin.")
# Egitim surecini history degiskenine kaydediyoruz ki grafigini cizebilelim
history = model.fit(X, y, epochs=1000, verbose=0) 

# 5. TERMINAL CIKTISI (Tertemiz ve TR karaktersiz)
print("\n--- Egitim Tamamlandi ---")
predictions = model.predict(X, verbose=0) # verbose=0 progress bar'i gizler

for i in range(len(X)):
    tahmin = int(round(predictions[i][0]))
    print(f"Girdi: {X[i]} | Beklenen: {y[i][0]} | Ag Ciktisi: {predictions[i][0]:.4f} -> Yuvarlanmis: {tahmin}")

# 6. GORSELLESTIRME (Matplotlib)
plt.figure(figsize=(14, 6))

# Grafik 1: Ogrenme Sureci (Loss Curve)
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], color='red', linewidth=2)
plt.title('Modelin Ogrenme Sureci (Loss Curve)', fontsize=14)
plt.xlabel('Epoch (Egitim Dongusu)', fontsize=12)
plt.ylabel('Hata Payi (Loss)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Grafik 2: Karar Siniri (Decision Boundary)
plt.subplot(1, 2, 2)
# Arka plani boyamak icin izgara olusturuyoruz
xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 100), np.linspace(-0.5, 1.5, 100))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()], verbose=0)
Z = Z.reshape(xx.shape)

# Renkli alanlar
contour = plt.contourf(xx, yy, Z, levels=50, cmap='RdBu', alpha=0.8)
plt.colorbar(contour, label='Tahmin Olasiligi (Probability)')

# Gercek noktalari uzerine ekliyoruz
plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap='bwr', edgecolors='k', s=150, zorder=10)
plt.title('XOR Karar Siniri (Decision Boundary)', fontsize=14)
plt.xlabel('Girdi 1 (x1)', fontsize=12)
plt.ylabel('Girdi 2 (x2)', fontsize=12)

plt.tight_layout()
plt.show()