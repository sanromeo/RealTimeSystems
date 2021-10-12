import random
from math import sin, cos, pi
import matplotlib.pyplot as plt
import timeit

N = 256
n = 8
W = 2000

#Функція генерації випадкого сигналу
def stat_random_signal():
    x_signal_array = [0] * N
    for i in range(1, n + 1):
        A = random.random()
        phi = random.random()
        for j in range(N):
            x_signal_array[j] += A * sin(W / i * (j + 1) + phi)
    return x_signal_array


#Функція дискретного перетворення Фур'є (DFT)
def get_DFT(signal: list):
    length = len(signal)
    return [sum((X[j] * complex(cos(-2 * pi * i * j / length), sin(-2 * pi * i * j / length)) for j in range(length))) for i in range(N)]


#Функція швидкого перетворення Фур'є (FFT)
def get_FFT(signal, length_of_s, start = 0, step_count = 1):
    if length_of_s == 1:
        return [signal[start]]
    hn, sd = length_of_s // 2, step_count*2
    rs = get_FFT(signal, hn, start, sd) + get_FFT(signal, hn, start + step_count, sd)
    for p in range(hn):
        e = complex(cos(-2*pi*p/length_of_s), sin(-2*pi*p/length_of_s))
        rs[p], rs[p + hn] = rs[p] + e * rs[p + hn], rs[p] - e * rs[p + hn]
    return rs


if __name__ == "__main__":
    X = stat_random_signal()
    time_start = timeit.default_timer()
    dft = get_DFT(X)
    print("Розрахунок часу DFT: {}".format(timeit.default_timer() - time_start))
    time_start = timeit.default_timer()
    fft = get_FFT(X, len(X))
    print("Розрахунок часу FFT: {}".format(timeit.default_timer() - time_start))
    figure, ((plot_GenRandSignal_1, plot_DFT), (plot_GenRandSignal_2, plot_FFT)) = plt.subplots(2, 2, figsize=(15, 15))
    plot_GenRandSignal_1.plot(range(N), X, "g")
    plot_GenRandSignal_1.title.set_text("Згенерований випадковий сигнал")
    plot_DFT.plot(range(N), dft, "r")
    plot_DFT.title.set_text("DFT")
    plot_GenRandSignal_2.plot(range(N), X, "g")
    plot_GenRandSignal_2.title.set_text("Згенерований випадковий сигнал")
    plot_FFT.plot(range(N), fft, "r")
    plot_FFT.title.set_text("FFT")
    plt.show()
#Завдання: Порівняти час DFT i FFT
#Висновок: FFT швидше за DFT. Cкрін часу додав у репозиторій.