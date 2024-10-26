import numpy as np
import matplotlib.pyplot as plt

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

# Plotagem
plt.figure(figsize=(12, 8))

# Sinal modulador
plt.subplot(3, 1, 1)
plt.plot(t, m_t, color='blue')
plt.title('Sinal Modulador (Modulador(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Portadora
plt.subplot(3, 1, 2)
carrier = Ac * np.cos(2 * np.pi * Fc * t)
plt.plot(t, carrier, color='green')
plt.title('Sinal Portadora (Portadora(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Sinal FM
plt.subplot(3, 1, 3)
plt.plot(t, s_fm, color='red')
plt.title('Sinal Modulado em FM (Sinal Modulado(t))')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()