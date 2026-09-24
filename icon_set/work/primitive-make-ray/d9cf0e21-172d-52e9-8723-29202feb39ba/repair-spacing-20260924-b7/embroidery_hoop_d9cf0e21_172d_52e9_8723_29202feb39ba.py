"""embroidery hoop: fresh spacing repair.
Plan: Broad clamp continuous with hoop; true split screw attachment; inner ring centered on outer bowl.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Inner ring reduced by one unit; screw-head oval reduced to a straight bar.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d9cf0e21-172d-52e9-8723-29202feb39ba'
SOURCE_PATH='pictographic-primitives/hobbies/embroidery hoop_d9cf0e21-172d-52e9-8723-29202feb39ba.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='embroidery-hoop-d9cf0e21'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
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
        self.add_line('neck-left',(16,4),(16,16))
        self.add_arc('shoulder-left',(16,16),(8,28),radius_x=8,radius_y=12,sweep=False)
        self.add_arc('lower-ring',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_arc('shoulder-right',(40,28),(32,16),radius_x=8,radius_y=12,sweep=False)
        self.add_line('neck-right-lower',(32,16),(32,8))
        self.add_line('neck-right-upper',(32,8),(32,4))
        self.add_line('clamp-top',(32,4),(16,4))
        self.add_contour('hoop','neck-left','shoulder-left','lower-ring','shoulder-right','neck-right-lower','neck-right-upper','clamp-top',closed=True)
        self.circle('inner-ring',24,28,6)
        self.add_line('screw',(32,8),(40,8));self.relate('connect','screw','hoop')
        self.add_polyline('screw-head',(40,4),(40,8),(40,12));self.relate('connect','screw','screw-head')
