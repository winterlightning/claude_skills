"""embroidery hoop: fresh spacing repair.
Plan: Concentric hoop outlines with 9-unit minimum radial separation. Top clamp joins exposed outer-hoop endpoint, screw is split at clamp.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Paired narrow clamp ears merged into a central clamp; hoop made subtly oval.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='43991475-8f12-5467-b407-e55e5e59e1f3'
SOURCE_PATH='pictographic-primitives/hobbies/embroidery hoop_43991475-8f12-5467-b407-e55e5e59e1f3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='embroidery-hoop'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases=()
    keywords=('embroidery', 'hoop')

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
        points=[(24,14),(40,29),(24,44),(8,29)]
        for i in range(4): self.add_arc(f'hoop-{i}',points[i],points[(i+1)%4],radius_x=16,radius_y=15)
        self.add_contour('outer-hoop',*(f'hoop-{i}' for i in range(4)),closed=True)
        self.circle('inner-hoop',24,29,6)
        self.add_line('clamp',(24,4),(24,14));self.relate('connect','clamp','outer-hoop')
        self.add_polyline('screw',(18,4),(24,4),(36,4));self.relate('connect','screw','clamp')
