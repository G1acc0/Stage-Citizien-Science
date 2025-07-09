from Backend_Citizien_Science import res
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dati = json.loads(res())
df = pd.DataFrame(dati, columns=["ID", "Orario", "Val Inquinanti"])

sns.barplot(x="Orario", y="Val Inquinanti", data=df)

plt.title("Valori per Orario")
plt.show()