"""insurance cheap: fresh spacing repair.
Plan: Rising beam with left coin lower than right medical plus, triangular support attached at shared central node.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Dollar inscription removed; outlined medical cross reduced to open plus.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='58b70697-62ea-4501-873d-8e51b3416d7a'
SOURCE_PATH='pictographic-primitives/health/insurance cheap_58b70697-62ea-4501-873d-8e51b3416d7a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='insurance-cheap'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases=()
    keywords=('insurance', 'cheap')

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

    def build(self):
        self.circle('coin',13,16,6)
        self.cross('medical-cross',36,12,6)
        self.add_polyline('beam',(6,34),(24,30),(42,26))
        self.add_polyline('fulcrum',(24,30),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
