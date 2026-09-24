from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f238b6ea-82d0-5437-a344-0ec38b16a28d'
SOURCE_PATH='pictographic-primitives/health/monitoring heart beat hand_f238b6ea-82d0-5437-a344-0ec38b16a28d.svg'
AUTHOR='gpt-6'
PLAN='Heart-pulse lobes and trace, hand gripping lower right; Lucide heart-pulse and hand principles, deliberate grip asymmetry.'
class Drawing(Solo48):
    icon_id='monitoring-heart-beat-hand'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('monitoring', 'heart', 'beat', 'hand')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('heart',(26,28),[('L',(20,30)),('L',(9,21)),('B',(6,14),(6,18),(6,16)),('B',(14,6),(6,10),(10,6)),('B',(22,11),(18,6),(20,9)),('B',(30,6),(26,7),(26,6)),('B',(38,14),(35,6),(38,10)),('B',(34,23),(38,18),(36,21))])
        self.add_polyline('pulse',(6,18),(12,18),(18,26),(24,18),(37,18))
        self.path('hand',(30,42),[('L',(26,36)),('L',(26,30)),('A',(34,22),6,6,True),('L',(40,28)),('L',(40,36)),('L',(42,42))])

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
