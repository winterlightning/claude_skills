from pathlib import Path
import json
root=Path(__file__).parent;p=root/'author_batch.py';s=p.read_text()
overrides='''# Final native-size pass: separate ground opening; widen biscuits; align both figures.
D[8]['paths']['outline']='M 4 31 C 4 24 13 8 24 8 C 35 8 44 24 44 31 C 44 43 4 43 4 31 Z'
D[11]['paths'].update({'head-a':circle(12,12,4),'head-b':circle(38,12,4),'torso-a':'M 12 24 L 12 31','torso-b':'M 38 24 L 38 31','left-arm':'M 12 24 L 8 24 L 4 29','raised-arm':'M 12 24 L 22 24 L 25 12','right-arms':'M 30 29 L 33 24 L 38 24 L 41 24 L 44 29','legs-a':'M 6 40 L 12 31 L 18 40','legs-b':'M 32 40 L 38 31 L 44 40'})
D[13]['keyshape']='SQUARE'
D[13]['paths']={'biscuit-a':rect(6,6,14,36,7),'biscuit-b':rect(28,6,14,36,7),'groove-a':'M 13 15 C 10 21 16 27 13 34','groove-b':'M 35 15 C 32 21 38 27 35 34'}
D[16]['paths']['slot-left']='M 19 18 L 19 20'
D[16]['paths']['slot-right']='M 29 18 L 29 20'
D[16]['paths']['ground']='M 20 31 L 20 29 A 4 4 1 28 29 L 28 31 Z'
D[19]['paths']['outer']='M 12 44 C 11 40 10 36 10 32 C 10 28 13 25 15 23 L 23 13 C 26 10 28 15 27 19 L 23 26 C 20 32 25 34 29 29 C 32 25 29 20 30 15 L 30 8 A 4 4 1 38 8 L 38 28 C 38 36 29 38 24 44'
'''
s=s.replace("HELPER='''",overrides+"\nHELPER='''");p.write_text(s)
b=root/'batch.json';rows=json.loads(b.read_text())
for i in [8,11,13,16,19]:
 row=rows[i];old=Path(row['result_dir']);new=old.parent/'20260929T0934-gpt-6';new.mkdir(exist_ok=True);row['result_dir']=str(new)
 for name in ['reference.png','rejected.png']:(new/name).write_bytes((old/name).read_bytes())
 (new/(row['icon_id']+'.metadata.json')).write_text(json.dumps(row,indent=2))
b.write_text(json.dumps(rows,indent=2))
