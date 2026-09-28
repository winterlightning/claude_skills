from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='12af7a01-21fd-509d-9eae-c7bfcfdaedd2'
SOURCE_PATH='pictographic-primitives/health/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg'
AUTHOR='gpt-6'
PLAN='Capsule tank lower left with two-to-one height, simplified valve stem; hose joins circular timer at left cardinal point. Lucide clock. Valve housing and ticks omitted to retain breathing space.'
class Drawing(Solo48):
    icon_id='oxygen-tank-timer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('oxygen', 'tank', 'timer')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('tank',(10,26),[('A',(14,30),4,4,True),('L',(14,38)),('A',(10,42),4,4,True),('A',(6,38),4,4,True),('L',(6,30)),('A',(10,26),4,4,True)],True)
        self.add_polyline('valve',(10,6),(10,17),(10,26))
        self.add_polyline('valve-top',(6,6),(10,6),(16,6))
        self.circle('timer',31,17,11)
        self.add_line('hose',(10,17),(20,17))
        self.add_polyline('hands',(31,15),(31,17),(33,17))
        for a,b in [('valve','tank'),('valve','valve-top'),('hose','valve'),('hose','timer')]:self.relate('connect',a,b)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start;members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='B':self.add_bezier(eid,at,(*args,end))
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,q=4):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
