"""task list multiple: fresh parallel-spacing repair.
Plan: Two sheets, an asymmetric check and a text rule remain clear at native size.
Keyshape SQUARE: Square envelope preserves the overlapping page arrangement.
Omissions: Repeated checklist rows reduced to one check and one text rule.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d590c41a-0991-45d2-955b-ea0aa00b5b4a'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/task list multiple_d590c41a-0991-45d2-955b-ea0aa00b5b4a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='task-list-multiple'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('task', 'list', 'multiple')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def page(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,8)),('A',(12,4),4)],True)
    def phone(self,band=True):
        self.path('phone',(12,4),[('L',(36,4)),('A',(40,8),4),('L',(40,36)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,36)),('L',(8,8)),('A',(12,4),4)],True)
        if band:
            self.add_line('separator',(8,36),(40,36));self.relate('connect','phone','separator')
    def house(self):
        self.path('house',(6,18),[('L',(24,6)),('L',(42,18)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,18))],True)

    def frame(self):
        self.path('frame',(10,6),[('L',(38,6)),('A',(42,10),4),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4)],True)

    def build(self):
        self.add_polyline('front-top',(18,14),(34,14),(38,14))
        self.add_arc('front-tr',(38,14),(42,18),radius_x=4)
        self.add_line('front-right',(42,18),(42,38))
        self.add_arc('front-br',(42,38),(38,42),radius_x=4)
        self.add_line('front-bottom',(38,42),(18,42))
        self.add_arc('front-bl',(18,42),(14,38),radius_x=4)
        self.add_polyline('front-left',(14,38),(14,34),(14,18))
        self.add_arc('front-tl',(14,18),(18,14),radius_x=4)
        parts=['front-top','front-tr','front-right','front-br','front-bottom','front-bl','front-left','front-tl']
        for a,b in zip(parts,parts[1:]+parts[:1]):self.relate('connect',a,b)
        self.path('rear',(14,34),[('L',(10,34)),('A',(6,30),4),('L',(6,10)),('A',(10,6),4),('L',(30,6)),('A',(34,10),4),('L',(34,14))])
        self.relate('connect','front-top','rear');self.relate('connect','front-left','rear')
        self.add_polyline('check',(23,24),(26,26),(33,22))
        self.add_line('text',(23,34),(33,34))
