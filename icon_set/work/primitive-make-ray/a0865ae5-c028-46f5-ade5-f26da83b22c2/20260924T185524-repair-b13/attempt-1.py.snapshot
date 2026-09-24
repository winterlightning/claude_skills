from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a0865ae5-c028-46f5-ade5-f26da83b22c2'
SOURCE_PATH='pictographic-primitives/holidays/vaisakhi harvest_a0865ae5-c028-46f5-ade5-f26da83b22c2.svg'
AUTHOR='gpt-6'
PLAN='Drum hoop series spaced 8; pair of beaters above. Wheat two joints spaced 8; squared drum simplified from curved barrel. No useful exact Lucide match.'
class Drawing(Solo48):
    icon_id='vaisakhi-harvest'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('vaisakhi', 'harvest')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_line('beater-left',(6,6),(12,10))
        self.add_line('beater-right',(30,6),(22,10))
        self.add_polyline('drum',(6,18),(26,18),(26,26),(26,34),(26,42),(6,42),(6,34),(6,26),closed=True)
        for y in (26,34):
            n=f'hoop-{y}';self.add_line(n,(6,y),(26,y));self.relate('connect','drum',n)
        self.add_polyline('wheat',(26,42),(34,34),(42,26),(42,18))
        self.add_polyline('grain',(34,26),(34,34),(42,34))
        self.relate('connect','wheat','grain');self.relate('connect','wheat','drum')

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
