import json
from artifact_tool import Blob,SpreadsheetFile
w=SpreadsheetFile.import_xlsx(Blob.load('archivio_cereali_webapp_semafori_estesi.xlsx'))
rows=w.worksheets.items[0].get_range('A1:Q16').values
keys=['id','nome','categoria','natura','sapore','tropismo','azioni','nota','pagina','stato','qi','sangue','yang','yin','umidita','calore','stasi']
data=[]
for row in rows[1:]:
    if not row[0]: continue
    d=dict(zip(keys,row));d['azioni']=[x.strip() for x in (d['azioni'] or '').split(';') if x.strip()]
    data.append(d)
with open('alimenti.json','w',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
