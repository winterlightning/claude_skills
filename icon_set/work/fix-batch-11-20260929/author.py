from pathlib import Path
import json
ROOT=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
helpers='''
        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)
'''
designs={
'winking-face-peeling-sticker':('CIRCLE','''
        # Circular sticker with a large joined fold; facial marks occupy the unpeeled area.
        path('outline',(44,24),[('A',(24,4),20,20,False),('A',(4,24),20,20,False),('A',(24,44),20,20,False),('L',(44,24))],True)
        path('fold',(24,44),[('L',(24,36)),('A',(36,24),12,12,True),('L',(44,24))]);join('fold','outline')
        self.add_dot('eye',(14,18))
        path('wink',(26,17),[('A',(32,17),5,3,True)])
        path('smile',(12,28),[('A',(19,32),9,9,False)])
'''),
'wraparound-safety-goggles':('HRECT_L','''
        # Paired curved lens lobes and smooth central bridge; outer protective rim shares axis 24.
        path('rim',(14,40),[('L',(12,40)),('A',(4,32),8,8,True),('L',(4,16)),('A',(12,8),8,8,True),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,32)),('A',(36,40),8,8,True),('L',(34,40))])
        path('lens',(16,17),[('L',(32,17)),('A',(35,20),3,3,True),('L',(35,27)),('A',(31,31),4,4,True),('C',(24,26),(27,31),(28,26)),('C',(17,31),(20,26),(21,31)),('A',(13,27),4,4,True),('L',(13,20)),('A',(16,17),3,3,True)],True)
'''),
'xbox-emblem-batch-086':('CIRCLE','''
        # A broad lower spherical panel, smaller crown, mirrored swept side panels.
        path('top',(14,7),[('A',(34,7),20,20,True),('L',(24,14)),('L',(14,7))],True)
        path('left',(8,12),[('C',(4,24),(5,14),(4,19)),('C',(7,35),(4,28),(5,32)),('C',(17,23),(9,31),(13,26)),('C',(8,12),(15,19),(11,13))],True)
        path('right',(40,12),[('C',(44,24),(43,14),(44,19)),('C',(41,35),(44,28),(43,32)),('C',(31,23),(39,31),(35,26)),('C',(40,12),(33,19),(37,13))],True)
        path('bottom',(12,40),[('C',(24,28),(14,35),(19,30)),('C',(36,40),(29,30),(34,35)),('A',(12,40),20,20,True)],True)
'''),
'woman-wearing-drooping-nightcap':('SQUARE','''
        # Circular face below the cap, asymmetric trailing point, paired open hair wings.
        path('hat',(6,26),[('L',(6,18)),('A',(18,6),12,12,True),('L',(28,6)),('A',(40,18),12,12,True),('L',(40,24)),('L',(30,16)),('L',(30,26)),('L',(6,26))],True)
        path('jaw',(30,26),[('A',(10,26),10,10,True)]);join('jaw','hat')
        circle('pompom',40,27,2);join('pompom','hat')
        path('hair-left',(6,26),[('L',(6,42)),('L',(18,42))]);join('hair-left','hat')
        path('hair-right',(30,26),[('L',(34,42)),('L',(26,42))]);join('hair-right','hat');join('hair-right','jaw')
'''),
'wonder-woman-portrait':('SQUARE','''
        # Circular jaw radius10; shoulder apex36 is four centerline units below jaw32 (touching ink).
        path('crown',(14,18),[('L',(14,14)),('L',(24,6)),('L',(34,14)),('L',(34,18))])
        path('face',(14,18),[('L',(14,22)),('A',(34,22),10,10,False),('L',(34,18))]);join('crown','face')
        self.add_line('tiara',(14,18),(34,18));join('tiara','crown');join('tiara','face')
        path('hair-left',(14,14),[('A',(6,22),8,8,False),('L',(6,42))]);join('hair-left','crown')
        path('hair-right',(34,14),[('A',(42,22),8,8,True),('L',(42,42))]);join('hair-right','crown')
        path('shoulders',(6,42),[('C',(24,36),(10,36),(17,36)),('C',(42,42),(31,36),(38,36))]);join('shoulders','hair-left');join('shoulders','hair-right');join('shoulders','face')
''')}
for r in json.loads((ROOT/'runs.json').read_text()):
 key,body=designs[r['icon_id']];run=Path(r['run'])
 text=f'''"""{r['comparison']}
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={r['source_uuid']!r}
SOURCE_PATH={r['reference_path']!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={r['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(r['concept'].split())!r}
'''
 if r['icon_id']=='wonder-woman-portrait':text+="    human_construction='bust'\n"
 text+='    def build(self):\n'+helpers+body
 (run/(r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py')).write_text(text)
