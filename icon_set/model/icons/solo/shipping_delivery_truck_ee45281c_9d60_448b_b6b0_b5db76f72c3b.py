"""Cargo rectangle and rounded cab with wheel-sized gaps in the chassis; equal circular wheels attach on horizontal diameters."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH='pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR='gpt-6'
PLAN='Equal wheel centers (16,36),(32,36), radius 4. Chassis ends at wheel sides rather than continuing behind or tangent along them. Rounded cab retained.'
CONSTRUCTION_REFERENCE='truck original and atomic-debug: horizontal chassis segments attach at wheel sides; coherent curved cab.'
OMISSIONS='Cargo divider stops above the chassis to leave wheel clearance. Wheels moved inward and reduced slightly.'

class Drawing(Solo48):
    icon_id='shipping-delivery-truck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
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
        self.path('cargo',(12,36),[('L',(4,36)),('L',(4,8)),('L',(24,8)),('L',(24,16)),('L',(24,24))])
        self.path('cab',(24,16),[('L',(34,16)),('C',(44,26),(39,16),(44,21)),('L',(44,36)),('L',(36,36))])
        self.add_line('chassis',(20,36),(28,36))
        for x in (16,32):self.circle(f'wheel-{x}',x,36,4)
        self.relate('connect','cargo','wheel-16')
        self.relate('connect','cab','cargo')
        self.relate('connect','chassis','wheel-16')
        self.relate('connect','chassis','wheel-32')
        self.relate('connect','cab','wheel-32')
