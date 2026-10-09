import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    "categoria": [
        "Eletrônicos", "Eletrônicos", "Eletrônicos", "Eletrônicos", "Roupas", "Roupas",
        "Roupas", "Roupas", "Alimentos", "Alimentos", "Alimentos", "Alimentos",
        "Livros", "Livros", "Livros", "Livros", "Brinquedos", "Brinquedos",
        "Brinquedos", "Brinquedos",
    ],
    "regiao": [
        "Norte", "Sul", "Leste", "Oeste", "Norte", "Sul",
        "Leste", "Oeste", "Norte", "Sul", "Leste", "Oeste",
        "Norte", "Sul", "Leste", "Oeste", "Norte", "Sul",
        "Leste", "Oeste",
    ],
    "vendas_medias": [
        183.94, 72.57, 258.83, 130.2, 96.63, 60.19, 197.72, 219.39,
        54.15, 178.02, 106.62, 211.29, 93.59, 222.73, 146.68, 284.18,
        84.38, 135.27, 78.37, 281.17,
    ],
})

sns.barplot(data=dados, x="categoria", y="vendas_medias", hue="regiao")
plt.show()
