import matplotlib.pyplot as plt
import pandas as pd
import math

dt = pd.read_csv(
    "../res.log",
    sep=',',
    encoding="utf-8-sig",
)

# tableau20[2] arancione
# tableau20[4] verde
# tableau20[6] rosso
# tableau20[8] viola
# tableau20[10] marrone
# tableau20[12] rosa
# tableau20[14] grigio
# tableau20[16] verdino
# tableau20[18] azzurro
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

plt.close()
plt.figure(1, figsize=(16, 7))




# Settaggio griglia asse y
ax = plt.axes()
ax.yaxis.grid(linestyle='--')

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#plt.xlabel('n° di valori non zeri')
plt.xlabel('n° celle matrice')
plt.ylabel('Tempo (s)')

dt = dt.sort_values('rows')
dt = dt.reset_index(drop=True)


x = dt['rows']

a = [3.69419201604257e-08, -9.41399383682348e-08, 0.000368093143035400, 0.0381986233504408]
#x_interpolated = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000, 1500, 2000, 2500, 3000]
#y_interpolated = [0.401054, 0.290296, 0.979843, 2.311794, 4.500351, 10.333815, 12.352358, 18.49247, 26.66356, 36.591357, 37.040442, 125.951585, 297.646099, 575.330919, 998.46681]


#TEMPI

# Scipy
#y = dt['scipy']
#l1, = plt.plot(x, y, color=tableau20[2], dashes=[2, 2], marker='o', label='Scipy DCT')


# Custom
x_interpolated = list(range(100, 3001, 10))
y_interpolated = [sum([a[0]*(x_i**3) + a[1]*(x_i**2) + a[2]*(x_i) + a[3]]) for x_i in x_interpolated]
y_nlogn = [1000*x_i*math.log(x_i) for x_i in x_interpolated]
plt.plot(x, dt['scipy'], color=tableau20[18], marker='o', dashes=[2,2], label='Scipy DCT')
#plt.scatter(x, dt['custom'], color=tableau20[18], marker='o', label='Custom DCT')
#plt.plot(x_interpolated, y_interpolated, label='Interpolated', color=tableau20[2])




plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.xscale('log')
#plt.yscale('log')
plt.subplots_adjust(bottom=0.15, right=0.8)
plt.savefig('scipy_plot.png', trasparent=True)
plt.show()
