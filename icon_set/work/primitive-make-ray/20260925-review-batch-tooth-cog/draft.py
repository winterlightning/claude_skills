from pathlib import Path
import json
B=Path(__file__).parent;rows=json.loads((B/'inputs.json').read_text())
helper=Path('icon_set/work/primitive-make-ray/20260925-review-batch-pin-se/draft_batch.py').read_text().split("HELPERS='''",1)[1].split("'''",1)[0]
bodies=[
'''        # Crown lobes and long rounded roots derive from a shared axis.
        self.path('tooth',(8,13),[('C',(16,4),(8,7),(10,4)),('C',(24,6),(20,4),(21,6)),('C',(32,4),(27,6),(28,4)),('C',(40,13),(38,4),(40,7)),('C',(36,30),(40,20),(36,24)),('C',(32,44),(36,37),(34,44)),('C',(28,34),(30,44),(29,38)),('C',(24,26),(27,29),(27,26)),('C',(20,34),(21,26),(21,29)),('C',(16,44),(19,38),(18,44)),('C',(12,30),(14,44),(12,37)),('C',(8,13),(12,24),(8,20))],True)
        self.path('groove',(17,16),[('C',(24,15),(19,12),(21,15)),('C',(31,13),(27,17),(30,16))])
''',
'''        self.path('pod',(14,14),[('L',(22,14)),('C',(44,24),(32,14),(40,17)),('C',(38,34),(44,30),(44,34)),('L',(14,34)),('A',(14,14),10,10,True)],True)
        self.path('windshield',(22,14),[('C',(32,24),(22,20),(26,24)),('L',(44,24))]);self.relate('connect','pod','windshield')
        self.add_line('mark-top',(13,20),(16,20));self.add_line('mark-bottom',(13,28),(15,28))
''',
'''        self.add_polyline('house',(8,44),(8,18),(24,4),(40,18),(40,44),closed=True)
        self.add_polyline('frame',(16,20),(32,20),(32,36))
        self.add_polyline('door',(16,20),(24,24),(24,32),(16,36),closed=True)
        self.relate('connect','frame','door')
''',
'''        self.path('bottle',(12,44),[('A',(8,40),4,4,True),('L',(8,30)),('C',(16,16),(8,26),(12,16)),('L',(30,21)),('C',(40,32),(36,22),(40,28)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44))],True)
        self.path('cap',(16,16),[('L',(19,9)),('C',(33,14),(21,3),(35,7)),('L',(30,21))]);self.relate('connect','cap','bottle')
        self.add_line('nozzle',(28,8),(30,4));self.relate('connect','cap','nozzle')
        self.path('label',(24,25),[('C',(18,31),(21,25),(18,28)),('L',(18,32)),('A',(21,35),3,3,False),('L',(27,35)),('A',(30,32),3,3,False),('L',(30,31)),('C',(24,25),(30,28),(27,25))],True)
''',
'''        self.path('bottle',(18,20),[('L',(24,20)),('L',(30,20)),('A',(38,28),8,8,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,28)),('A',(18,20),8,8,True)],True)
        self.add_polyline('neck',(18,20),(18,12),(24,12),(30,12),(30,20));self.relate('connect','neck','bottle')
        self.add_line('stem',(24,4),(24,12));self.add_polyline('pump',(18,4),(24,4),(30,4));self.relate('connect','stem','neck');self.relate('connect','stem','pump')
''',
'''        self.path('bowl',(8,25),[('C',(25,4),(8,14),(18,4)),('C',(40,18),(32,4),(40,11)),('L',(40,32)),('C',(24,44),(34,40),(31,44)),('C',(8,25),(13,44),(8,38))],True)
        self.add_line('stem',(40,32),(40,44));self.relate('connect','bowl','stem')
''',
'''        self.path('body',(12,36),[('L',(12,20)),('C',(20,10),(12,14),(20,14)),('L',(20,8)),('A',(28,8),4,4,True),('L',(28,10)),('C',(36,20),(28,14),(36,14)),('L',(36,36))])
        self.path('rim',(12,36),[('L',(36,36)),('A',(36,44),4,4,True),('L',(12,44)),('A',(12,36),4,4,True)],True)
        self.relate('connect','rim','body')
''',
'''        self.circle('head',24,13,7)
        self.add_line('cap-band',(17,13),(31,13));self.relate('connect','head','cap-band')
        self.path('body',(6,42),[('L',(6,32)),('A',(14,24),8,8,True),('L',(24,24)),('L',(26,24)),('L',(34,24)),('A',(42,32),8,8,True),('L',(42,42))])
        self.relate('connect','head','body')
        self.add_line('fastening',(26,24),(26,42));self.relate('connect','fastening','body')
        self.add_polyline('cross-h',(14,34),(16,34),(18,34));self.add_polyline('cross-v',(16,32),(16,34),(16,36));self.relate('connect','cross-h','cross-v')
''',
'''        self.circle('head',24,14,10)
        self.path('body',(14,28),[('A',(8,36),6,8,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,36)),('A',(34,28),6,8,False)])
        self.add_polyline('bow-left',(14,28),(24,32),(14,36),closed=True)
        self.add_polyline('bow-right',(34,28),(34,36),(24,32),closed=True)
        self.relate('connect','bow-left','bow-right');self.relate('connect','body','bow-left');self.relate('connect','body','bow-right')
''',
'''        # Six repeated teeth and root recesses mirror around both axes.
        self.add_polyline('gear',(20,6),(28,6),(31,12),(38,10),(42,18),(38,24),(42,30),(38,38),(31,36),(28,42),(20,42),(17,36),(10,38),(6,30),(10,24),(6,18),(10,10),(17,12),closed=True)
        self.circle('hub',24,24,5)
'''
]
names=['molar-tooth','hyperloop-pod','house-with-open-door','liquid-detergent-bottle','liquid-soap-dispenser','lowercase-a','condom-reference','man-doctor-avatar','man-wearing-bow-tie','cog-interface-essential']
keys=['VRECT_L','CIRCLE','VRECT_L','VRECT_L','VRECT_M','VRECT_L','VRECT_L','SQUARE','VRECT_L','SQUARE']
for i,row in enumerate(rows):
 src=f'''"""Fresh complete reference reconstruction. Shared contour parameters and deliberate reference asymmetry retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={row['source_uuid']!r}
SOURCE_PATH={row['reference_path']!r}
AUTHOR='gpt-6'
PARENT_MODULE={row['parent']!r}
class Drawing(Solo48):
    icon_id={names[i]!r}
    keyshape=Keyshape.{keys[i]}
    semantic_role='MAIN'
    semantic_kind='noun'
    category={'avatars' if i in [7,8] else 'objects'!r}
    aliases=()
    keywords=({row['concept']!r},)
'''+helper+'\n    def build(self):\n'+bodies[i]
 p=Path(row['run'])/(names[i].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py');p.write_text(src);row.update(module=str(p),icon_id=names[i],keyshape=keys[i])
(B/'inputs.json').write_text(json.dumps(rows,indent=2))
