import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    "altura_cm": [
        182, 188.2, 168.9, 179.8, 155.5, 177.8, 168.4, 156.4, 180.3, 151.9,
        150.9, 173.6, 175.7, 179.7, 177.4, 184.8, 177, 168.7, 169.3, 167.2,
        173, 159, 173.4, 169.1, 172.8, 172.8, 145.5, 161, 168.9, 169.4,
        172.6, 173, 185.2, 173.1, 166.9, 154, 156.3, 175.4, 180.6, 185.4,
        161.7, 167, 172.4, 190.5, 171.1, 185.5, 171.7, 181.5, 180.3, 171.7,
        159.8, 167.3, 184.9, 178.8, 165.7, 166.6, 152.7, 184.4, 178.9, 168.6,
        172, 148.3, 165.1, 183.3, 179.8, 173.3, 169.9, 178, 167.2, 153.4,
        169.9, 174, 181.2, 155.6, 168.8, 169.2, 159, 174.9, 177.5, 167.1,
        190.6, 166.8, 165.5, 165.2, 161.8, 164.4, 155.7, 168.1, 170.6, 147.2,
        169, 170.4, 175.1, 182, 178.5, 163.8, 162.6, 175.8, 164.5, 157.7,
        193.7, 166.9, 163.7, 148.1, 178.5, 160.1, 170.3, 179.7, 160.3, 170.8,
        185.2, 145.4, 161.9, 161, 168.1, 169.5, 159.4, 163.5, 162.3, 166.5,
        172.2, 179.1, 180.6, 176.5, 161.3, 170, 193.7, 180.1, 165.6, 185.8,
        166.1, 163.3, 184, 156.9, 150.9, 179.4, 170.3, 171.3, 166.4, 167.6,
        165.4, 163.7, 166.2, 165.9, 161.7, 164.5, 145, 176.8, 173.9, 169.2,
    ],
    "peso_kg": [
        75, 80.7, 58.4, 69.1, 52.6, 71.1, 71.8, 58.9, 77, 42.9,
        43, 61.3, 69.5, 58, 67.4, 74.8, 61.7, 65.8, 56.6, 61.8,
        79.6, 45.1, 65.3, 60.2, 62.5, 69.3, 46.5, 58.7, 58.4, 74.7,
        56.5, 60.6, 77.5, 66.3, 62.6, 56.5, 50.1, 68.4, 69.6, 79.8,
        54, 58.7, 67.9, 86.6, 53, 78.8, 63.2, 78.1, 71, 71,
        50.4, 49.4, 81.7, 66.7, 51.2, 60, 46.2, 80.1, 75.4, 62.2,
        60.4, 44.9, 59.4, 77.9, 67.5, 64, 65.4, 76.4, 65.3, 48.4,
        60.5, 68.6, 67.6, 45.9, 69.4, 64.3, 51.4, 71.5, 76.2, 58.2,
        79.4, 57.4, 63.8, 63.6, 62.6, 63, 41.9, 62.7, 58.2, 39.9,
        62.9, 67.6, 63.2, 62.2, 71.6, 70.6, 55.4, 68.5, 67, 54.9,
        85.5, 62.4, 58.6, 37.6, 64, 63.5, 64.2, 72.2, 53.8, 67.6,
        89.4, 43.5, 52.8, 54.2, 66.7, 59.7, 57.7, 45.5, 54.9, 63,
        71.3, 67.1, 65, 67.6, 49.5, 62.2, 84.3, 65.5, 63.1, 76.5,
        64.9, 47.8, 70.5, 53.8, 41.8, 70.6, 63.3, 64.9, 56.4, 61.6,
        55, 60.7, 59, 60.1, 68.4, 52.6, 47.4, 55.9, 56.1, 56,
    ],
    "sexo": [
        "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Feminino", "Masculino",
        "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Masculino", "Feminino", "Masculino",
        "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Masculino",
        "Masculino", "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino",
        "Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino",
        "Feminino", "Feminino", "Feminino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino", "Feminino",
        "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino", "Masculino",
        "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Feminino", "Feminino", "Feminino",
        "Feminino", "Masculino", "Masculino", "Feminino", "Masculino", "Masculino", "Masculino", "Feminino",
        "Feminino", "Feminino", "Masculino", "Feminino", "Feminino", "Masculino",
    ],
})

sns.scatterplot(data=dados, x="altura_cm", y="peso_kg", hue="sexo")
plt.show()
