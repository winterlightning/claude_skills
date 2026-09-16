"""A right-facing head profile wears a large circular earcup. A straight headband strip rises over the crown, while the face's projecting nose, chin and neck remain visible.
Symbol plan: Right-facing head with a clear nose, chin, continuous neck and one round earcup. The single band reaches the crown; omit the duplicate band strip and earcup dot. Profile anatomy follows the supplied human render.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: headphones; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87b4dae7-6d5a-504e-b877-c237378af3a1'
SOURCE_PATH = 'pictographic-primitives/audio/headphones human_87b4dae7-6d5a-504e-b877-c237378af3a1.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'person-wearing-headphones-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    aliases = ()
    keywords = ('person', 'wearing', 'headphones', 'in', 'profile')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_arc('back-head',(8,20),(24,4),radius_x=16)
        self.add_arc('forehead',(24,4),(36,16),radius_x=12)
        segments('face',(36,16),(40,28),(34,28),(34,34))
        self.add_arc('chin',(34,34),(28,40),radius_x=6)
        self.add_line('front-neck',(28,40),(28,44))
        self.add_line('back-neck',(16,44),(16,36))
        self.add_arc('nape',(16,36),(8,20),radius_x=8,radius_y=16)
        self.add_contour('head','back-neck','nape','back-head','forehead','face-1','face-2','face-3','chin','front-neck')
        self.add_arc('cup-right',(22,17),(22,27),radius_x=5)
        self.add_arc('cup-left',(22,27),(22,17),radius_x=5)
        self.add_contour('cup','cup-right','cup-left',closed=True)
        self.add_line('headband',(24,4),(22,17))
        self.relate('connect','headband','head');self.relate('connect','headband','cup')
