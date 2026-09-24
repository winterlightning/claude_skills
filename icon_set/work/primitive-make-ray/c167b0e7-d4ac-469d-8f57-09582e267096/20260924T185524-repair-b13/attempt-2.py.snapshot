from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c167b0e7-d4ac-469d-8f57-09582e267096'
SOURCE_PATH='pictographic-primitives/mobile/force touch press_c167b0e7-d4ac-469d-8f57-09582e267096.svg'
AUTHOR='gpt-6'
PLAN='Lucide hand rounded fingertip; widened bent index silhouette, omitted small secondary knuckle and impact rays. Deliberate directional asymmetry; no detached head.'
class Drawing(Solo48):
    icon_id='force-touch-press'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('force', 'touch', 'press')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('finger',(22,6),[('B',(10,22),(18,8),(14,16)),('A',(18,28),5,5,False),('L',(28,14)),('B',(36,10),(30,12),(32,10))])
        self.add_line('surface-left',(6,38),(10,38))
        self.add_line('surface-right',(38,38),(42,38))
        self.add_line('press',(24,34),(24,42))
        self.add_polyline('arrow',(20,38),(24,42),(28,38));self.relate('connect','press','arrow')

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
