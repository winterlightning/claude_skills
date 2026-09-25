"""Robot officer head with peaked cap and two sensor eyes. Square envelope. Lucide bot informs sparse face; cap retained, tiny badge omitted and side ears reduced to attached tabs to preserve clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b8b3014-0977-5eed-b161-f3d906254bd2'
SOURCE_PATH = 'pictographic-primitives/technology/robot police hat_4b8b3014-0977-5eed-b161-f3d906254bd2.svg'
AUTHOR = 'gpt-6'

class RobotPoliceOfficerHead(Solo48):
    icon_id = 'robot-police-officer-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('robot', 'police', 'cap', 'security', 'officer', 'head', 'guard')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        poly('cap',(10,20),(6,12),(24,6),(42,12),(38,20),(10,20),closed=True)
        arc('face-left',(10,20),(10,28),14,14,sweep=False)
        arc('face-bottom',(10,28),(38,28),14,14,sweep=False)
        arc('face-right',(38,28),(38,20),14,14,sweep=False)
        contour('face','face-left','face-bottom','face-right');connect('face','cap')
        self.add_dot('left-eye',(19,29));self.add_dot('right-eye',(29,29))
        line('left-ear',(6,28),(10,28));line('right-ear',(38,28),(42,28));connect('left-ear','face');connect('right-ear','face')
