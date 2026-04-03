import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Legge il file Excel
df = pd.read_excel("richieste_personale.xlsx")

print("\n--- DATAFRAME RICHIESTE ---")
print(df.head())

print("\n--- CONTEGGIO STATI ---")
conteggio_stati = df["Stato"].value_counts()
print(conteggio_stati)

# Grafico
conteggio_stati.plot(kind="bar")
plt.title("Richieste per stato")
plt.xlabel("Stato")
plt.ylabel("Numero richieste")
plt.tight_layout()
plt.show()

print("\n--- CONTEGGIO PER REPARTO ---")
conteggio_reparti = df["Reparto"].value_counts()
print(conteggio_reparti)

conteggio_reparti.plot(kind="bar")
plt.title("Richieste per reparto")
plt.xlabel("Reparto")
plt.ylabel("Numero richieste")
plt.tight_layout()
plt.show()

print("\n--- INSIGHT AUTOMATICO ---")

if conteggio_stati.get("In validazione HR", 0) > conteggio_stati.get("Approvata", 0):
    print("⚠️ Processo rallentato: molte richieste in attesa HR")
else:
    print("✔️ Processo fluido")