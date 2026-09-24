"""insurance expensive: fresh spacing repair.
Plan: Descending balance beam puts coin above the medical plus; tall central triangle protects negative space.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Dollar inscription omitted; medical cross simplified to plus.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48'
SOURCE_PATH='pictographic-primitives/health/insurance expensive_bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='insurance-expensive'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('insurance', 'expensive')

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
        self.circle('coin',13,12,6)
        self.cross('medical-cross',36,16,6)
        self.add_polyline('beam',(6,26),(24,30),(42,34))
        self.add_polyline('fulcrum',(24,30),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
