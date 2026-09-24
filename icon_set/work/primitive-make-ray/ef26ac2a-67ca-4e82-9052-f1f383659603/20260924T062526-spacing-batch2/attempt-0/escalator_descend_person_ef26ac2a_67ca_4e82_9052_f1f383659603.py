"""escalator descend person.
Plan: Standing person on diagonal descending escalator with downward corner arrow. human-reference.md/full_body_ref.png: head radius3, bottom12, torso neck20 exact4 ink gap. Genuine torso/rail shared standing point. No useful Lucide exact match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ef26ac2a-67ca-4e82-9052-f1f383659603'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/escalator descend person_ef26ac2a-67ca-4e82-9052-f1f383659603.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='escalator-descend-person'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('escalator', 'descend', 'person')
    def build(self):
        self.circle('head',14,9,3)
        self.add_line('torso',(14,20),(14,30))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.path('rail',(12,30),[('L',(14,30)),('L',(32,12)),('L',(36,12)),('A',(36,24),6,6,True),('L',(18,42)),('L',(12,42)),('A',(12,30),6,6,True)],True)
        self.relate('connect','torso','rail')
        self.add_polyline('down-arrow',(42,32),(42,42),(32,42))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
