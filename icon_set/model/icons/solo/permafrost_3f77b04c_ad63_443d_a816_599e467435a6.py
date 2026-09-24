from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f77b04c-ad63-443d-a816-599e467435a6'
SOURCE_PATH = 'icon_set/work/todo-references/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A snowflake inside a rounded square for permafrost.
    Plan: Six snowflake arms sharing one center; repeated forked branch construction.
    Reference: snowflake: repeated six-way arms and branches; rounded enclosure from monitor.
    """
    icon_id = 'permafrost'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('permafrost',)

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)

    def build(self):

        self.rounded('frame',6,6,42,42)
        ends=[(24,14),(33,19),(33,29),(24,34),(15,29),(15,19)]
        for i,p in enumerate(ends):self.add_line(f'arm-{i}',(24,24),p)
        self.relate('connect',*(f'arm-{i}' for i in range(6)))
        forks=[((20,14),(24,18),(28,14)),((33,15),(30,21),(36,22)),((36,26),(30,27),(33,33)),((20,34),(24,30),(28,34)),((15,33),(18,27),(12,26)),((12,22),(18,21),(15,15))]
        for i,pts in enumerate(forks):
            self.add_polyline(f'fork-{i}',*pts)
