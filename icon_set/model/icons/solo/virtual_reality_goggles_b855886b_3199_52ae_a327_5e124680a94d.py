"""Broad visor has smooth rounded ends, a centered nose notch and short lateral straps."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='b855886b-3199-52ae-a327-5e124680a94d'
SOURCE_PATH='pictographic-primitives/devices/device wearable vr goggles_b855886b-3199-52ae-a327-5e124680a94d.svg'
AUTHOR='gpt-6'
PLAN='Widened the visor from 32 to 36 centerline units. Matched radius-10 ends and smooth mirrored nose curves remove the old block-like corners.'
CONSTRUCTION_REFERENCE='glasses original and atomic-debug: paired curves and bilateral balance.'
OMISSIONS='Hollow side straps become short solid tabs. The visor is taller relative to its width than the source because of the prescribed keyshape.'
class Drawing(Solo48):
    icon_id='virtual-reality-goggles'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('device', 'wearable', 'vr', 'goggles')
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')

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
        self.path('visor',(16,10),[('L',(32,10)),('A',(42,20),10,10,True),('L',(42,28)),('A',(32,38),10,10,True),('C',(24,32),(28,38),(28,32)),('C',(16,38),(20,32),(20,38)),('A',(6,28),10,10,True),('L',(6,20)),('A',(16,10),10,10,True)],True)
        for n,a,b in [('left',(4,24),(6,24)),('right',(42,24),(44,24))]:
            self.add_line('strap-'+n,a,b);self.relate('connect','strap-'+n,'visor')
