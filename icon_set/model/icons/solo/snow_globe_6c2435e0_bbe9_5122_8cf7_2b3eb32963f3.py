from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='6c2435e0-bbe9-5122-8cf7-2b3eb32963f3'
SOURCE_PATH='pictographic-primitives/holidays/snow globe_6c2435e0-bbe9-5122-8cf7-2b3eb32963f3.svg'
AUTHOR='gpt-6'
PLAN='Globe lower arc terminates at pedestal joints instead of overlapping base. Symmetric about x24. Lucide tree-pine triangle reduced to one tier; trunk retained.'
class Drawing(Solo48):
    icon_id='snow-globe'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases=()
    keywords=('snow', 'globe')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('globe',(14,36),[('B',(8,20),(10,32),(8,26)),('A',(40,20),16,16,True),('B',(34,36),(40,26),(38,32))])
        self.add_polyline('base',(8,44),(10,36),(14,36),(34,36),(38,36),(40,44),closed=True)
        self.relate('connect','base','globe')
        self.add_polyline('tree',(24,13),(18,25),(24,25),(30,25),closed=True)
        self.add_line('trunk',(24,25),(24,27));self.relate('connect','trunk','tree')

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
