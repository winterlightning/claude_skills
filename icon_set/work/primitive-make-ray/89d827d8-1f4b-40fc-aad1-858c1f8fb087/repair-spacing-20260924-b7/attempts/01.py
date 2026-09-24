"""kanda matsuri: fresh spacing repair.
Plan: Three inward pointing heart forms share a central tip geometrically; initial spacing trial retains separate loops, with no connection exemptions.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: Hanging tassel marks and stems omitted; circle enlarged to protect three heart forms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='89d827d8-1f4b-40fc-aad1-858c1f8fb087'
SOURCE_PATH='pictographic-primitives/holidays/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='kanda-matsuri'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('kanda', 'matsuri')

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
        self.circle('medallion',24,24,20)
        self.add_bezier('heart-top',(24,16),((16,10),(16,20),(24,24)),((32,20),(32,10),(24,16)))
        self.add_bezier('heart-left',(18,28),((10,22),(18,18),(24,24)),((24,34),(14,36),(18,28)))
        self.add_bezier('heart-right',(30,28),((38,22),(30,18),(24,24)),((24,34),(34,36),(30,28)))
