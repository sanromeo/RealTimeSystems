import random
from math import sin, cos, pi
import matplotlib.pyplot as plt
import timeit
from numpy import fft
N = 256
n = 8
W = 2000

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

if __name__ == "__main__":
    X = stat_random_signal()
    time_start = timeit.default_timer()
    dft = get_DFT(X)
    print("Розрахунок часу DFT: {}".format(timeit.default_timer() - time_start))
    time_start_np_DFT = timeit.default_timer()
    dft_np = fft.fft(X)
    print("Розрахунок часу numpy DFT: {}".format(timeit.default_timer() - time_start_np_DFT))

    figure, (plot_GenRandSignal_1, plot_DFT) = plt.subplots(2, figsize=(15, 15))
    figure, (plot_GenRandSignal_2, plot_DFT_NP) = plt.subplots(2, figsize=(15,15))

    plot_GenRandSignal_1.plot(range(N), X, "g")
    plot_GenRandSignal_1.title.set_text("Згенерований випадковий сигнал")
    plot_GenRandSignal_2.plot(range(N), X, "g")
    plot_GenRandSignal_2.title.set_text("Згенерований випадковий сигнал")

    plot_DFT_NP.plot(range(N), dft_np, "b")
    plot_DFT.plot(range(N), dft, "r")
    plot_DFT.title.set_text("Дискретне перетворення Фур'є")
    plot_DFT_NP.title.set_text("Дискретне перетворення Фур'є (numpy)")
    plt.show()
#Завдання: Порівняти із numpy DFT
#Висновок: Графіки - однакові, numpy DFT - швидше.