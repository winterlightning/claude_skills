"""Notched pass and rising aircraft, preserving asymmetric direction and side cutouts. Lucide tickets-plane informs open plane construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9cbe2481-852f-43a0-a967-6cc8e7df1295'
SOURCE_PATH = 'pictographic-primitives/travel/plane boarding pass_9cbe2481-852f-43a0-a967-6cc8e7df1295.svg'
AUTHOR = 'gpt-6'
PLAN = 'Notched pass and rising aircraft, preserving asymmetric direction and side cutouts. Lucide tickets-plane informs open plane construction.'
OMISSIONS = ['Tear-off divider omitted; airplane outline reduced to open strokes.']
class Drawing(Solo48):
    icon_id = 'plane-boarding-pass'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('plane', 'boarding', 'pass')
    def build(self):
        self.add_line('top-1',(4,20),(4,8))
        self.add_line('top-2',(4,8),(44,8))
        self.add_line('top-3',(44,8),(44,20))
        self.add_arc('right-notch',(44,20),(44,28),radius_x=4,sweep=False)
        self.add_line('bottom-1',(44,28),(44,40))
        self.add_line('bottom-2',(44,40),(4,40))
        self.add_line('bottom-3',(4,40),(4,28))
        self.add_arc('left-notch',(4,28),(4,20),radius_x=4,sweep=False)
        self.add_contour('ticket','top-1','top-2','top-3','right-notch','bottom-1','bottom-2','bottom-3','left-notch',closed=True)
        self.add_polyline('fuselage',(15,27),(19,31),(27,25),(32,19))
        self.add_polyline('wing',(20,17),(27,25))
        self.relate('connect','fuselage','wing')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)
