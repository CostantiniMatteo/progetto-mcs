import matplotlib.pyplot as plt
import pandas as pd

dt = pd.read_csv(
    "../logs/res2.csv",
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


plt.figure(1, figsize=(16, 7))

# Settaggio griglia asse y
ax = plt.axes()
ax.yaxis.grid(linestyle='--')

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#plt.xlabel('n° di valori non zeri')
plt.xlabel('Dimensione')
plt.ylabel('Errore (%)')


dt = dt.sort_values('nnz')
dt = dt.reset_index(drop=True)

x = list()

for el in dt['name'].unique():
    x.append(dt.loc[dt['name'] == el, 'nnz'].unique().mean())

# x = list(range(1, len(dt['name'].unique()) + 1))
# plt.xticks(x, dt['dim'].unique(), rotation=45)

# Per dimensione
dt = dt.sort_values('dim')
dt = dt.reset_index(drop=True)
x = dt['dim'].unique()


#ERRORE

y_py_w = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'python'),'re']
y_mat_w = dt.loc[(dt['os'] == 'windows') & (dt['lang'] == 'matlab'),'re']

y_py_u = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'python'),'re']
y_mat_u = dt.loc[(dt['os'] == 'ubuntu') & (dt['lang'] == 'matlab'),'re']


# y_u = [sum(y) / 2 for y in zip(y_py_u, y_mat_u)]
# plt.plot(x, y_u, color=tableau20[2], dashes=[2, 2], marker='o', label='Media Ubuntu')

# y_w = [sum(y) / 2 for y in zip(y_mat_w, y_py_w)]
# plt.plot(x, y_w, color=tableau20[18], dashes=[2, 2], marker='o', label='Media Windows')


# plt.plot(x, y_py_w, color=tableau20[4], dashes=[2, 2], marker='o', label='Windows/Python')
# plt.plot(x, y_py_u, color=tableau20[6], dashes=[2, 2], marker='o', label='Ubuntu/Python')

plt.plot(x, y_mat_w, color=tableau20[4], dashes=[2, 2], marker='o', label='Windows/Matlab')
plt.plot(x, y_mat_u, color=tableau20[6], dashes=[2, 2], marker='o', label='Ubuntu/Matlab')


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



plt.yscale('log')
plt.xscale('log')
plt.subplots_adjust(bottom=0.15, right=0.8)
#plt.gca().add_artist(legend1)
#plt.savefig('immagini/Errore-w-vs-u_dim.png')
plt.show()
