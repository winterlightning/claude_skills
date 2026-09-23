from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9178ba4e-ed60-49f0-9678-66306d46987a'
SOURCE_PATH = 'icon_set/work/todo-references/percent_9178ba4e-ed60-49f0-9678-66306d46987a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A percent sign with two circular counters.
    Plan: Equal circles mirrored around the canvas center and a diagonal slash.
    Reference: circle-percent: clean slash and circular counters; source has no outer enclosure.
    """
    icon_id = 'percent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('percent',)

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

        for i,c in enumerate((12,36)):self.circle(f'counter-{i}',c,c,6)
        self.add_line('slash',(6,42),(42,6))
