"""Open hand beside a microchip; shared8-unit finger pitch and one pin on each chip side.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: One tall finger, palm decoration, and second pin per side removed for spacing.
Construction: Shared human_ref hand/limb vocabulary; Lucide cpu: square body and cardinal pins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='40415ff8-ab5e-4613-9886-33d055540f90'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/technology hand chip_40415ff8-ab5e-4613-9886-33d055540f90.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='technology-hand-chip'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('technology', 'hand', 'chip')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('hand',(4,40),[('L',(4,20)),('A',(12,20),4,4,True),('L',(12,12)),('A',(20,12),4,4,True),('L',(20,34)),('A',(28,34),4,4,True),('L',(28,36)),('A',(24,40),4,4,True)])
        self.add_line('finger-division',(12,20),(12,26));self.relate('connect','finger-division','hand')
        self.add_polyline('chip',(30,10),(36,10),(42,10),(42,16),(42,22),(36,22),(30,22),(30,16),closed=True)
        for name,a,b in [('top',(36,8),(36,10)),('bottom',(36,22),(36,24)),('left',(29,16),(30,16)),('right',(42,16),(44,16))]:
            self.add_line('pin-'+name,a,b);self.relate('connect','pin-'+name,'chip')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def path(self,n,start,ops,closed=False):
        p=start;members=[]
        for i,op in enumerate(ops):
            name=f'{n}-{i}';end=op[1]
            if op[0]=='L':self.add_line(name,p,end)
            elif op[0]=='A':self.add_arc(name,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            elif op[0]=='B':self.add_bezier(name,p,(op[2],op[3],end))
            members.append(name);p=end
        if closed and p!=start:
            self.add_line(n+'-close',p,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
