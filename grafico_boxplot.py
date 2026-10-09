import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    "departamento": [
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "TI", "TI", "TI", "TI", "TI", "TI",
        "TI", "TI", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Marketing", "Marketing", "Marketing", "Marketing", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "RH", "RH",
        "RH", "RH", "RH", "RH", "RH", "RH", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
        "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas",
    ],
    "salario": [
        9257.07, 6542.55, 7210.87, 5199.82, 4763.46, 4123.45, 5450.96, 9716.98,
        4282.73, 6468.81, 4737, 5948.3, 7296.96, 5774.8, 8906.91, 9684.46,
        3064.08, 5804.76, 7103.5, 8970.7, 6205.07, 6965.11, 4975.7, 4317.61,
        9529.42, 3807.88, 11075.08, 8269.01, 8189.95, 8007.07, 6557.8, 7686.15,
        6669.43, 7967.88, 6941.05, 5336.89, 5476.5, 5277.52, 8699.08, 5919.47,
        19600, 21000, 2087.9, 4396.84, 5514.52, 4773.08, 3396.68, 2413.19,
        3865.73, 3840.78, 3030.8, 4551.04, 5846.63, 4222.28, 4160.48, 3062.77,
        5397.41, 3924.86, 3421.04, 4063.69, 4471.96, 4139.22, 5206.15, 4383.97,
        3716.06, 4401.19, 4499.64, 2703.62, 5149.42, 3699.1, 3724.68, 4751.38,
        4747.17, 3299.17, 4802.9, 3439.55, 5819.57, 3171.81, 4239.48, 3217.98,
        6222.7, 2762.18, 11200, 12000, 4524.36, 3265.09, 3645.89, 4453.54,
        5224.58, 5623.4, 2463.05, 4267.75, 5459.49, 2314.69, 4314.38, 3997.92,
        4414.54, 3227.7, 2564.38, 2086.89, 4976.38, 5104.05, 4302.69, 3465.85,
        2376.95, 4563.35, 2899.22, 3288.7, 3413.44, 3802.46, 3240.96, 4033.46,
        3378.18, 4701.37, 5031.06, 4108.54, 4462.63, 6117.86, 2827.4, 2766.53,
        4695, 5946.54, 3739.5, 5726.83, 11200, 12000, 7168.76, 5808.45,
        5266.29, 8101.47, 5398.82, 7142.23, 9771.06, 6463.13, 9299.52, 4874.55,
        6065.66, 4537.5, 7127.74, 8365.14, 7131.58, 9147.34, 5688.94, 7394.35,
        6076.93, 7632.93, 7881.54, 8019.19, 5126.46, 5442.94, 5767.5, 6581.96,
        7152.58, 8239.16, 5515.83, 4198.22, 10772.55, 5019.96, 8463.57, 7054.72,
        7439.78, 6997.29, 6326.53, 7811.95, 6232.47, 9041.03, 19600, 21000,
    ],
})

sns.boxplot(data=dados, x="departamento", y="salario")
plt.show()
