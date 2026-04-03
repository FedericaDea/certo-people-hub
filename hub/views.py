from django.shortcuts import render, redirect, get_object_or_404
from .models import Richiesta, Reparto, Ruolo, MotivoRichiesta, OrganicoReparto

def home(request):
    messaggio = ""

    if request.method == "POST":
        nome_richiedente = request.POST.get("nome_richiedente")
        reparto = request.POST.get("reparto")
        ruolo_richiesto = request.POST.get("ruolo_richiesto")
        motivazione = request.POST.get("motivazione")
        urgenza = request.POST.get("urgenza")
        tipo_richiesta = request.POST.get("tipo_richiesta")
        motivo_richiesta = request.POST.get("motivo_richiesta")

        Richiesta.objects.create(
            nome_richiedente=nome_richiedente,
            reparto=reparto,
            ruolo_richiesto=ruolo_richiesto,
            motivazione=motivazione,
            urgenza=urgenza,
            tipo_richiesta=tipo_richiesta,
            motivo_richiesta=motivo_richiesta
        )

        messaggio = "Richiesta salvata correttamente"

    richieste = Richiesta.objects.all().order_by("-data_creazione")
    reparti = Reparto.objects.all().order_by("nome")
    ruoli = Ruolo.objects.all().order_by("nome")
    motivi = MotivoRichiesta.objects.all().order_by("nome")

    return render(request, "hub/home.html", {
        "messaggio": messaggio,
        "richieste": richieste,
        "reparti": reparti,
        "ruoli": ruoli,
        "motivi": motivi
    })


def aggiorna_stato(request, richiesta_id):
    if request.method == "POST":
        richiesta = get_object_or_404(Richiesta, id=richiesta_id)
        nuovo_stato = request.POST.get("stato")
        richiesta.stato = nuovo_stato
        richiesta.save()

    return redirect("home")
import pandas as pd

import pandas as pd

def dashboard(request):
    dati = Richiesta.objects.all().values()
    df = pd.DataFrame(dati)

    if df.empty:
        reparto = {}
        stato = {}
        motivo = {}

        totale_richieste = 0
        inserite = 0
        in_valutazione = 0
        approvate = 0
    else:
        reparto = df["reparto"].value_counts().to_dict()
        stato = df["stato"].value_counts().to_dict()
        motivo = df["motivo_richiesta"].value_counts().to_dict()

        totale_richieste = len(df)
        inserite = stato.get("Inserita", 0)
        in_valutazione = stato.get("In valutazione", 0)
        approvate = stato.get("Approvata", 0)

    organico = OrganicoReparto.objects.all()

    organico_data = []

    for voce in organico:
        organico_data.append({
            "reparto": voce.reparto,
            "ruolo": voce.ruolo,
            "attuali": voce.risorse_attuali,
            "previste": voce.risorse_previste,
            "gap": voce.gap_risorse()
        })
    context = {
        "reparto": reparto,
        "stato": stato,
        "motivo": motivo,
        "organico": organico_data,
        "reparto_labels": list(reparto.keys()),
        "reparto_values": list(reparto.values()),
        "stato_labels": list(stato.keys()),
        "stato_values": list(stato.values()),
        "motivo_labels": list(motivo.keys()),
        "motivo_values": list(motivo.values()),

        "totale_richieste": totale_richieste,
        "inserite": inserite,
        "in_valutazione": in_valutazione,
        "approvate": approvate,
    }

    return render(request, "hub/dashboard.html", context)
