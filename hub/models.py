from django.db import models


class Reparto(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Ruolo(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class MotivoRichiesta(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class OrganicoReparto(models.Model):
    reparto = models.CharField(max_length=100)
    ruolo = models.CharField(max_length=100)
    risorse_attuali = models.IntegerField(default=0)
    risorse_previste = models.IntegerField(default=0)

    def gap_risorse(self):
        return self.risorse_previste - self.risorse_attuali

    def __str__(self):
        return f"{self.reparto} - {self.ruolo}"


class Richiesta(models.Model):
    nome_richiedente = models.CharField(max_length=100)
    reparto = models.CharField(max_length=100)
    ruolo_richiesto = models.CharField(max_length=100)
    motivazione = models.TextField()
    urgenza = models.CharField(max_length=20)
    tipo_richiesta = models.CharField(max_length=100)
    motivo_richiesta = models.CharField(max_length=100, null=True, blank=True)
    stato = models.CharField(max_length=50, default="Inserita")
    data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_richiedente} - {self.ruolo_richiesto}"