from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='a89e6154-b80a-49dd-8449-f86a088a5c81'
SOURCE_PATH='pictographic-primitives/other/box pen_a89e6154-b80a-49dd-8449-f86a088a5c81.svg'
AUTHOR='gpt-6'
PLAN='Lucide box: three perspective edges share corner. Increase both side-face heights to open bands; shorten pen while retaining closed nib silhouette and diagonal pose; omit nib division.'
class Drawing(Solo48):
    icon_id='box-pen'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('box', 'pen')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('pencil',(6,12),(12,6),(18,12),(20,20),(12,18),closed=True)
        self.add_polyline('box-edge',(6,26),(6,36),(24,42),(42,32),(42,22),(32,16))
        self.add_polyline('rim',(6,26),(24,32),(42,22))
        self.add_line('corner',(24,32),(24,42))
        for a,b in [('box-edge','rim'),('box-edge','corner'),('rim','corner')]:self.relate('connect',a,b)

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
