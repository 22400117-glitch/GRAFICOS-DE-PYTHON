import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.DataFrame(
    {
        "8:00": [
            90, 33, 88, 51, 63, 142, 113,
        ],
        "10:00": [
            89, 75, 93, 31, 97, 74, 49,
        ],
        "12:00": [
            84, 47, 58, 49, 54, 139, 199,
        ],
        "14:00": [
            83, 98, 68, 25, 44, 144, 49,
        ],
        "16:00": [
            44, 71, 81, 22, 60, 64, 151,
        ],
        "18:00": [
            26, 85, 33, 30, 55, 49, 197,
        ],
        "20:00": [
            52, 30, 60, 97, 28, 164, 78,
        ],
    },
    index=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
)

sns.heatmap(data=dados)
plt.show()
