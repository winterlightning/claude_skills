from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9647e6a3-625d-460f-ac2c-d7b1a64ebe4d'
SOURCE_PATH = 'icon_set/work/todo-references/pedal_9647e6a3-625d-460f-ac2c-d7b1a64ebe4d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A pedal with a rectangular tread and curved support arm.
    Plan: Rounded top tread and a tapered support with a semicircular bottom.
    Reference: No useful subject match; rounded rectangular and capsule construction follows geometric Lucide principles.
    """
    icon_id = 'pedal'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pedal',)

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

        self.rounded('tread',10,4,30,14,3)
        self.add_line('arm-upper-1',(30, 10),(38, 10))
        self.add_line('arm-upper-2',(38, 10),(38, 18))
        self.add_line('arm-upper-3',(38, 18),(30, 36))
        self.add_line('arm-upper-4',(30, 36),(30, 40))
        self.add_arc('arm-bottom',(30,40),(22,40),radius_x=4)
        self.add_line('arm-left',(22,40),(22,14))
        self.add_contour('arm','arm-upper-1','arm-upper-2','arm-upper-3','arm-upper-4','arm-bottom','arm-left')
        self.relate('connect','arm','tread')
