import matplotlib.pyplot as plt
import numpy as np

# Sua matriz
cm = np.array([[120, 80],
                [21, 179]])

fig, ax = plt.subplots(figsize=(4, 4))

# Matriz de cor
cax = ax.matshow(cm, cmap=plt.cm.Blues)

# Ticks
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['False', 'True'])
ax.set_yticklabels(['False', 'True'])

# Eixos e títulos
ax.set_xlabel('Predicted Class', fontsize=12, labelpad=12)
ax.set_ylabel('Actual Class', fontsize=12, labelpad=12)
ax.xaxis.set_label_position('bottom')
ax.xaxis.set_ticks_position('bottom')
ax.set_title('Has error', fontsize=14, pad=20)

# Centralizando os valores na célula
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center", fontsize=20, color="black")

# Layout
plt.tight_layout()
plt.show()
