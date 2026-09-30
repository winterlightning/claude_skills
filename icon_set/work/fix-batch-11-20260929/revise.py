from pathlib import Path
import json,shutil
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text())
for r in rs:
 if r['icon_id']=='wraparound-safety-goggles':continue
 old=Path(r['run']);new=old.parent/'20260929-batch11-attempt02';new.mkdir(exist_ok=False)
 for f in old.glob('*.metadata.json'):shutil.copy(f,new/f.name)
 shutil.copy(old/'comparison.txt',new/'comparison.txt')
 f=next(old.glob('*.py'));s=f.read_text()
 if r['icon_id']=='winking-face-peeling-sticker':
  s=s.replace("(26,17),[('A',(32,17),5,3,True)]","(25,16),[('A',(31,16),5,3,True)]").replace("(12,28),[('A',(19,32),9,9,False)]","(12,27),[('A',(18,29),8,8,False)]")
 elif r['icon_id']=='wonder-woman-portrait':
  s=s.replace("(14,14),[('A',(6,22),8,8,False),('L',(6,42))]","(14,18),[('A',(6,26),8,8,False),('L',(6,42))]").replace("(34,14),[('A',(42,22),8,8,True),('L',(42,42))]","(34,18),[('A',(42,26),8,8,True),('L',(42,42))]")
  s=s.replace("join('hair-left','crown')","join('hair-left','crown');join('hair-left','face')").replace("join('hair-right','crown')","join('hair-right','crown');join('hair-right','face')")
  s=s.replace("[('C',(24,36),(10,36),(17,36)),('C',(42,42),(31,36),(38,36))]","[('A',(24,36),18,6,True),('A',(42,42),18,6,True)]")
 elif r['icon_id']=='woman-wearing-drooping-nightcap':
  s=s.replace("('L',(30,16)),('L',(30,26)),('L',(6,26))","('L',(28,16)),('L',(28,26)),('L',(12,26)),('L',(6,26))")
  s=s.replace("(30,26),[('A',(10,26),10,10,True)]","(28,26),[('A',(12,26),8,8,True)]")
  a=s.index("        path('hair-left'")
  s=s[:a]+"        path('hair-left',(6,34),[('A',(14,42),8,8,False)])\n        path('hair-right',(34,36),[('A',(28,42),6,6,True)])\n"
 elif r['icon_id']=='xbox-emblem-batch-086':
  a=s.index("        path('top'")
  s=s[:a]+"""        path('top',(16,6),[('A',(32,6),20,20,True),('L',(24,13)),('L',(16,6))],True)
        path('left',(7,15),[('C',(4,24),(5,17),(4,20)),('C',(6,32),(4,27),(5,30)),('C',(16,23),(9,28),(13,25)),('C',(7,15),(13,19),(10,16))],True)
        path('right',(41,15),[('C',(44,24),(43,17),(44,20)),('C',(42,32),(44,27),(43,30)),('C',(32,23),(39,28),(35,25)),('C',(41,15),(35,19),(38,16))],True)
        path('bottom',(12,40),[('C',(24,29),(15,35),(20,30)),('C',(36,40),(28,30),(33,35)),('A',(12,40),20,20,True)],True)
"""
 (new/f.name).write_text(s);r['run']=str(new)
(root/'runs.json').write_text(json.dumps(rs,indent=2))
