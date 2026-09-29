from pathlib import Path
import json
b=Path(__file__).parent;p=b/'author_batch.py';s=p.read_text()
overrides='''# Native-size revision: retain source layout while opening safe clearances.
D[3]['paths']['arrow']='M 15 24 L 32 24'
D[4]['paths']['shaft']='M 15 25 L 33 25'
D[4]['paths']['head']='M 27 19 L 33 25 L 27 31'
D[6]['paths']['check']='M 15 25 L 21 32 L 33 16'
D[7]['paths']['bar']='M 15 24 L 33 24'
D[8]['paths']['bar']='M 15 17 L 33 17'
D[8]['paths']['ring']=circle(24,29,4)
D[15]['paths']['torso']='M 25 8 C 30 8 22 13 22 18 C 22 22 25 26 29 29'
D[15]['paths']['legs']='M 29 29 L 23 34 L 23 44'
D[15]['paths']['back-leg']='M 29 29 L 31 35 L 31 44'
D[18]['paths']['question']='M 17 18 C 17 11 31 11 31 18 C 31 23 24 23 24 27'
D[18]['paths']['dot']='M 24 35 L 24 35'
'''
s=s.replace("HELPER='''",overrides+"\nHELPER='''");p.write_text(s)
p=b/'batch.json';rows=json.loads(p.read_text())
for i in [3,4,6,7,8,15,18]:
 r=rows[i];old=Path(r['result_dir']);new=old.parent/'20260929T091947Z-fix-b-gpt-6';new.mkdir(exist_ok=False);r['result_dir']=str(new)
 for n in ['reference.png','rejected.png']:(new/n).write_bytes((old/n).read_bytes())
 (new/(r['icon_id']+'.metadata.json')).write_text(json.dumps(r,indent=2))
p.write_text(json.dumps(rows,indent=2))
