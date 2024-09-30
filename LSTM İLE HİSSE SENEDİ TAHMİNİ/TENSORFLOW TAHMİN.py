import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

data = pd.read_csv('hissesenedi\\NETFLİXHİSSE\\netflix.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

data = data[['Adj Close']]

ölcekleyici = MinMaxScaler(feature_range=(0, 1))
ölcekleyicidata = ölcekleyici.fit_transform(data)

# Eğitim ve test verileri için ayırma
train_size = int(len(ölcekleyicidata) * 0.8)
train_data = ölcekleyicidata[:train_size]
test_data = ölcekleyicidata[train_size:]

# Eğitim ve test verileri oluşturma fonksiyonu
def create_dataset(data, time_step=60):
    X, y = [], []
    for i in range(time_step, len(data)):
        X.append(data[i-time_step:i, 0])  # Zaman serisi verisi
        y.append(data[i, 0])  # Bir adım sonraki değer
    return np.array(X), np.array(y)

time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Verileri LSTM modeli için yeniden şekillendir
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# LSTM modeli
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))  # Overfitting'i önlemek için dropout katmanı
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=25))
model.add(Dense(units=1))  # Çıkış katmanı (tek bir çıktı)

# Modeli derle egit
model.compile(optimizer='adam', loss='mean_squared_error')


model.fit(X_train, y_train, batch_size=32, epochs=50)

tahminler = model.predict(X_test)
# Tahmin edilen veriyi orijinal ölçekte geri çevir
tahminler = ölcekleyici.inverse_transform(tahminler)

# Gerçek test verilerini orijinal şekle döndür
y_test_scaled = ölcekleyici.inverse_transform(y_test.reshape(-1, 1))

plt.figure(figsize=(14, 7))
plt.plot(y_test_scaled, label='Gerçek Değerler', color='green')
plt.plot(tahminler, label='Tahminler',color='red')
plt.title('Netflix Hisse Senedi Fiyat Tahmini')
plt.xlabel('Zaman')
plt.ylabel('Kapanış Fiyatı')
plt.legend()
plt.show()
