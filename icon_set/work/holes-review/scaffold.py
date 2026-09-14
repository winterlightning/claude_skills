from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/queue.json'
AUTHOR='gpt-6'
p=Path(__file__).parent
mapping=[]
for i in json.loads((p/'queue.json').read_text()):
 if i['id']=='cologne-cathedral-v2':
  dest=ROOT/'icon_set/model/icons/solo/cologne_cathedral_v4.py';newid='cologne-cathedral-v4'
 else:
  dest,newid,text=prepare_variant(i['id'],'solo','Roomier openings — pending review')
  dest.write_text(text)
 mapping.append({'original':i['id'],'candidate':newid,'file':str(dest.relative_to(ROOT)),'source':i['file']})
(p/'mapping.json').write_text(json.dumps(mapping,indent=2))
print('Prepared',len(mapping),'independent candidates')
