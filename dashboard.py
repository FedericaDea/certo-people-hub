import pandas as pd
import os
import django
import matplotlib.pyplot as plt

# setup django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peoplehub_web.settings')
django.setup()

from hub.models import Richiesta

# dati
dati = Richiesta.objects.all().values()
df = pd.DataFrame(dati)

print("\n--- KPI ---")

# REPARTO
print("\nRichieste per reparto:")
reparto = df["reparto"].value_counts()
print(reparto)

# STATO
print("\nRichieste per stato:")
stato = df["stato"].value_counts()
print(stato)

# MOTIVO
print("\nRichieste per motivo:")
motivo = df["motivo_richiesta"].value_counts()
print(motivo)

# 📊 GRAFICI

# 1. Reparto
reparto.plot(kind="bar")
plt.title("Richieste per Reparto")
plt.xlabel("Reparto")
plt.ylabel("Numero richieste")
plt.show()

# 2. Stato
stato.plot(kind="bar")
plt.title("Richieste per Stato")
plt.xlabel("Stato")
plt.ylabel("Numero richieste")
plt.show()

# 3. Motivo
motivo.plot(kind="bar")
plt.title("Richieste per Motivo")
plt.xlabel("Motivo")
plt.ylabel("Numero richieste")
plt.show()