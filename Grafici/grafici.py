import matplotlib.pyplot as plt
import pandas as pd

dt = pd.read_csv(
    "../logs/res.log",
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
plt.figure(figsize=(16, 7))

# Settaggio griglia asse y
ax = plt.axes()
ax.yaxis.grid(linestyle='--')

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xlabel('Dimensione')
plt.ylabel('Errore relativo (%) - Tempo (s) - Memoria (MB)')
#plt.ylim(0, max(dt.loc[:, 'time']))
#plt.xlim(0, 16)

lista = list()

x = list(range(1, len(dt['name'].unique()) + 1))
plt.xticks(x, dt['dim'].unique(), rotation=45)

#TEMPI

# Windows/Python
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'python'),'time']
l1, = plt.plot(x, y, color=tableau20[2], dashes=[2, 2], marker='o', label='Windows/Python')
#plt.text(15.2, y.tail(1) , 'Windows/Python', fontsize=12, color=tableau20[2])

# Windows/Matlab
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'matlab'),'time']
plt.plot(x, y, color=tableau20[18], dashes=[2, 2], marker='o', label='Windows/Matlab')
#plt.text(15.2, y.tail(1), 'Windows/Matlab', fontsize=12, color=tableau20[18])

# Ubuntu/Python
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'time']
plt.plot(x, y, color=tableau20[3], dashes=[2, 2], marker='o', label='Ubuntu/Python')
#plt.text(15.2, y.tail(1) , 'Ubuntu/Python', fontsize=12, color=tableau20[3])

# Ubuntu/Matlab
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'matlab'),'time']
plt.plot(x, y, color=tableau20[19], dashes=[2, 2], marker='o', label='Ubuntu/Matlab')
#plt.text(15.2, y.tail(1) - 0.75e1, 'Ubuntu/Matlab', fontsize=12, color=tableau20[19])

# x = list(range(1, len(dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'time']) + 1))
# plt.plot(x, dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'time'])



# MEMORIA

# Windows/Python
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'python'),'memory']
l2, = plt.plot(x, y, color=tableau20[4], marker='o', label='Windows/Python')
#plt.text(15.2, y.tail(1) , 'Windows/Python', fontsize=12, color=tableau20[4])

# Windows/Matlab
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'matlab'),'memory']
plt.plot(x, y, color=tableau20[6], marker='o', label='Windows/Matlab')
#plt.text(15.2, y.tail(1) - 75, 'Windows/Matlab', fontsize=12, color=tableau20[6])

# Ubuntu/Python
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'memory']
plt.plot(x, y, color=tableau20[5], marker='o', label='Ubuntu/Python')
#plt.text(15.2, y.tail(1) , 'Ubuntu/Python', fontsize=12, color=tableau20[5])

# Ubuntu/Matlab
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'matlab'),'memory']
plt.plot(x, y, color=tableau20[7], marker='o', label='Ubuntu/Matlab')
#plt.text(15.2, (y.tail(1)), 'Ubuntu/Matlab', fontsize=12, color=tableau20[7])



# ERRORE RELATIVO

# Windows/Python
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'python'),'re']
l3, = plt.plot(x, y, color=tableau20[8], dashes=[2, 2, 10, 2], marker='o', label='Windows/Python')
#plt.text(15.2, y.tail(1) - 8e-13 , 'Windows/Python', fontsize=12, color=tableau20[8])

# Windows/Matlab
y = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'matlab'),'re']
plt.plot(x, y, color=tableau20[16], dashes=[2, 2, 10, 2], marker='o', label='Windows/Matlab')
#plt.text(15.2, y.tail(1) + 3e-11, 'Windows/Matlab', fontsize=12, color=tableau20[16])

# Ubuntu/Python
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'re']
plt.plot(x, y, color=tableau20[9], dashes=[2, 2, 10, 2], marker='o', label='Ubuntu/Python')
#plt.text(15.2, y.tail(1) - 4e-13 , 'Ubuntu/Python', fontsize=12, color=tableau20[9])

# Ubuntu/Matlab
y = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'matlab'),'re']
plt.plot(x, y, color=tableau20[17], dashes=[2, 2, 10, 2], marker='o', label='Ubuntu/Matlab')
#plt.text(15.2, y.tail(1) + 1.5e-12, 'Ubuntu/Matlab', fontsize=12, color=tableau20[17])


lista.append([l1, l2, l3])

legend1 = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.legend(lista[0], ["Memoria", "Tempo", "Errore relativo"], bbox_to_anchor=(1.05, 0.4), loc=2, borderaxespad=0)
plt.yscale('log')
plt.subplots_adjust(bottom=0.15, right=0.8)
plt.gca().add_artist(legend1)
plt.show()
