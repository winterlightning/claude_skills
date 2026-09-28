"""Cargo rectangle and rounded cab with wheel-sized gaps in the chassis; equal circular wheels attach on horizontal diameters."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH='pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR='gpt-6'
PLAN='Cargo rectangle and rounded cab with wheel-sized gaps in the chassis; equal circular wheels attach on horizontal diameters.'
CONSTRUCTION_REFERENCE='truck: segmented chassis ending at wheel sides'
OMISSIONS='No omissions.'

class Drawing(Solo48):
    icon_id='shipping-delivery-truck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('truck',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.path('cargo',(6,34),[('L',(4,34)),('L',(4,8)),('L',(26,8)),('L',(26,16)),('L',(26,24))])
        self.path('cab',(26,16),[('L',(34,16)),('C',(44,26),(39,16),(44,21)),('L',(44,28)),('L',(42,28))])
        self.add_line('chassis',(18,34),(30,34))
        for x in (12,36):self.circle(f'wheel-{x}',x,34,6)
        self.relate('connect','cargo','wheel-12')
        self.relate('connect','cab','cargo')
        self.relate('connect','chassis','wheel-12')
        self.relate('connect','chassis','wheel-36')
        self.relate('connect','cab','wheel-36')
