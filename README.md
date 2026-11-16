# Atlante di dietetica cinese

Webapp statica per consultare le schede dei cereali. Fonte: `archivio_cereali_webapp_semafori_estesi.xlsx`.

## Pubblicazione su GitHub Pages
1. Caricare `index.html`, `style.css`, `app.js`, `alimenti.json` nella radice del repository.
2. Aprire Settings → Pages → Build and deployment.
3. Selezionare Deploy from a branch, branch `main`, cartella `/(root)` e Save.
4. Attendere il link mostrato in Settings → Pages.

## Aggiornamento
Modificare il file Excel di origine. Per rigenerare `alimenti.json`, usare `genera_dati.py` in un ambiente Python con `artifact_tool`, oppure chiedere assistenza. Non modificare contemporaneamente i dati JSON e l'Excel.

Questa prima versione non comprende ancora note sintetiche: il campo nell'Excel è vuoto.
