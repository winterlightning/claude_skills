from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d4aec38-b440-43a0-b4f2-b3a846ae4cb1'
SOURCE_PATH = 'icon_set/work/todo-references/person magnifying glass_8d4aec38-b440-43a0-b4f2-b3a846ae4cb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A magnifying glass framing a small upright person.
    Plan: Lens and exact-circle handle attachment; inner head and narrow rounded upper torso.
    Reference: user-search: rounded head and shoulder construction; magnifier encircles the person as in source.
    """
    icon_id = 'person-magnifying-glass-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('person', 'magnifying', 'glass')
    # Shared human_ref/user.svg inspected. Head bottom y=18, shoulder apex y=26: exact centerline gap 8 / visible ink gap 4. Small upright bust, not a stick figure.

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

        self.add_arc('rim-a',(30,33),(12,9),radius_x=15)
        self.add_arc('rim-b',(12,9),(30,33),radius_x=15)
        self.add_contour('lens','rim-a','rim-b',closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','handle','lens')
        self.circle('person-head',21,15,3)
        self.add_arc('shoulders',(16,31),(26,31),radius_x=5)
        self.add_line('body-left',(16,31),(16,34));self.add_line('body-right',(26,31),(26,34))
        self.relate('connect','shoulders','body-left');self.relate('connect','shoulders','body-right')
