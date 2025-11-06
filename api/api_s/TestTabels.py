from django.db import models
import pandas as pd

class ArquivoResultado(models.Model):
    arquivo = models.FileField(upload_to='resultados/')
    enviado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # salva o arquivo primeiro

        from .models import Resultado  # evita import circular

        # Lê o Excel
        tabela = pd.read_excel(self.arquivo.path)

        # Renomeia colunas conforme o formato do seu arquivo
        tabela.columns = ['posicao', 'numero', 'nome', 'categoria', 'equipe', 'tempo', 'velocidade']
        tabela = tabela.fillna('')

        resultados = [
            Resultado(
                posicao=row['posicao'],
                numero=row['numero'],
                nome=row['nome'],
                categoria=row['categoria'],
                equipe=row['equipe'],
                tempo=str(row['tempo']),
                velocidade=row['velocidade']
            )
            for _, row in tabela.iterrows()
        ]
        Resultado.objects.bulk_create(resultados)

    def __str__(self):
        return f"Arquivo enviado em {self.enviado_em:%d/%m/%Y %H:%M}"
