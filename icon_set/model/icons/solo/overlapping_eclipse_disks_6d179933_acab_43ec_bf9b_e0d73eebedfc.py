"""astronomy eclipse. Plan: overlapping foreground disk and exposed rear crescent share exact top and bottom nodes; HRECT_L (4,8)-(44,40). Lucide eclipse informs coherent intersection topology; source side-by-side overlap preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d179933-acab-43ec-bf9b-e0d73eebedfc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astronomy eclipse_6d179933-acab-43ec-bf9b-e0d73eebedfc.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'overlapping-eclipse-disks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('astronomy', 'eclipse')
    def path(self,n,start,steps,closed=False):
        here=start;members=[]
        for k,step in enumerate(steps):
            ident=f'{n}-{k}';members.append(ident)
            if len(step)==2:
                self.add_line(ident,here,step);here=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep);here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,q=0):
        if q==0:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        else:self.path(n,(l+q,t),[(r-q,t),((r,t+q),q,q,True),(r,b-q),((r-q,b),q,q,True),(l+q,b),((l,b-q),q,q,True),(l,t+q),((l+q,t),q,q,True)],True)
    def build(self):
        self.path('front',(20,8),[((36,24),16,16,True),((20,40),16,16,True),((4,24),16,16,True),((20,8),16,16,True)],True)
        self.add_arc('rear',(20,8),(20,40),radius_x=24,radius_y=16)
        self.relate('connect','front','rear')
