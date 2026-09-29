from pathlib import Path
import json
p=Path(__file__).parent/'author_batch.py'
s=p.read_text()
overrides='''# Second visual pass: improve UI openings and preserve natural silhouettes.
D[0]['paths']['cab']='M 9 34 L 4 34 L 4 27 L 8 21 L 16 21 L 16 29'
D[0]['paths']['bed']='M 16 29 L 44 29 L 44 34 L 39 34'
D[0]['paths']['door']='M 27 29 L 27 24 A 4 4 1 35 24 L 35 29'
D[0]['paths']['house']='M 20 17 L 20 29 L 42 29 L 42 17'
D[0]['paths']['roof']='M 18 18 L 31 8 L 44 18'
D[2]['paths']['cab']='M 28 22 L 35 22 L 44 30 L 44 35 L 40 35'
D[2]['paths']['window']='M 33 22 L 33 29 L 43 29'
D[2]['paths']['box']='M 4 21 L 27 21 L 27 34 L 18 34'
D[2]['paths']['house']='M 7 17 L 7 11 L 14 6 L 21 11 L 21 17 Z'
D[3]['paths']['cab']='M 18 25 L 11 25 C 8 25 6 29 6 32 L 6 37 L 8 37'
D[4]['paths']['receiver']='M 16 13 L 21 18 L 18 21 C 20 24 23 27 26 28 L 29 25 L 34 29 C 31 34 26 32 20 27 C 14 22 12 17 16 13 Z'
D[5]['paths']['left-lamp']='M 18 29 L 18 29'
D[5]['paths']['right-lamp']='M 30 29 L 30 29'
D[6]['paths']['arm-right']='M 24 30 L 22 41'
D[6]['paths']['arm-left']='M 24 30 L 13 34 L 10 42'
D[7]['paths']['screen']=rect(12,20,18,12,2)
D[7]['paths']['knob-top']='M 36 22 L 36 22'
D[7]['paths']['knob-bottom']='M 36 30 L 36 30'
D[11]['paths']['raised-arm']='M 14 24 L 21 24 L 24 12'
D[12]['paths'].pop('upper-notch');D[12]['paths'].pop('lower-notch')
D[12]['paths']['upper']='M 15 14 C 15 9 22 13 26 11 C 32 8 33 4 38 7 C 46 14 39 22 29 25 C 19 28 11 23 15 14 Z'
D[12]['paths']['lower']='M 6 31 C 10 25 15 32 21 31 C 27 30 33 27 34 34 C 35 41 23 44 13 41 C 7 40 3 36 6 31 Z'
D[16]['paths']['plate']=rect(4,4,40,40,5)
D[16]['paths']['slot-left']='M 19 19 L 19 22'
D[16]['paths']['slot-right']='M 29 19 L 29 22'
D[16]['paths']['ground']='M 20 33 L 20 30 A 4 4 1 28 30 L 28 33 Z'
D[17]['paths']['water']='M 4 6 C 8 10 12 10 16 6 C 20 10 24 10 28 6 C 32 10 36 10 40 6'
D[17]['paths']['tail']='M 7 23 L 7 16 C 10 14 13 18 15 20'
D[17]['paths']['fin']='M 23 19 L 25 14 L 31 14 L 31 19'
'''
s=s.replace("HELPER='''",overrides+"\nHELPER='''")
p.write_text(s)
b=Path(__file__).parent/'batch.json';rows=json.loads(b.read_text())
for row in rows:
 old=Path(row['result_dir']);new=old.parent/'20260929T0927-gpt-6';new.mkdir(exist_ok=True);row['result_dir']=str(new)
 for name in ['reference.png','rejected.png']:(new/name).write_bytes((old/name).read_bytes())
 (new/(row['icon_id']+'.metadata.json')).write_text(json.dumps(row,indent=2))
b.write_text(json.dumps(rows,indent=2))
