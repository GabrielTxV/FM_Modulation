import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Função para criar um filtro passa-baixa
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs  # Frequência de Nyquist
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Função para aplicar o filtro passa-baixa
def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Parâmetros do sinal
Am = 5         # Amplitude do sinal modulador
Fm = 2          # Frequência do sinal modulador (Hz)
Ac = 1          # Amplitude da portadora
Fc = 50         # Frequência da portadora (Hz)
kf = 75         # Índice de modulação (constante de sensibilidade)
duration = 2    # Duração do sinal (s)
sampling_rate = 5000  # Taxa de amostragem (samples/s)

# Eixo do tempo
t = np.linspace(0, duration, int(sampling_rate * duration))

# Sinal modulador (sinal de mensagem)
m_t = Am * np.sin(2 * np.pi * Fm * t)

# Sinal FM (sinal de portadora modulado)
integral_m_t = np.cumsum(m_t) / sampling_rate
s_fm = Ac * np.cos(2 * np.pi * Fc * t + kf * integral_m_t)

# Aplicar filtro passa-baixa ao sinal FM
cutoff_frequency = 200  # Frequência de corte do filtro passa-baixa (Hz)
s_fm_filtered = lowpass_filter(s_fm, cutoff_frequency, sampling_rate)

# Plotagem
plt.figure(figsize=(12, 8))

# Sinal modulador
plt.subplot(4, 1, 1)
plt.plot(t, m_t, color='blue')
plt.title('Sinal Modulador (m(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Portadora
plt.subplot(4, 1, 2)
carrier = Ac * np.cos(2 * np.pi * Fc * t)
plt.plot(t, carrier, color='green')
plt.title('Sinal Portadora (c(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Sinal FM
plt.subplot(4, 1, 3)
plt.plot(t, s_fm, color='red')
plt.title('Sinal Modulado em FM (Sinal FM(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Sinal FM Filtrado
plt.subplot(4, 1, 4)
plt.plot(t, s_fm_filtered, color='purple')
plt.title('Sinal Modulado em FM Filtrado (Sinal Filtrado(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()