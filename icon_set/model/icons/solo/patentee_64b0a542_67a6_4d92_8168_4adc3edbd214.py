from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64b0a542-67a6-4d92-8168-4adc3edbd214'
SOURCE_PATH = 'icon_set/work/todo-references/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A patent certificate with a folded corner and ribbon seal.
    Plan: Fold and page share corner nodes; circular seal interrupts the page lower boundary.
    Reference: ticket: coherent document boundary; circular seal and ribbon from the source.
    """
    icon_id = 'patentee'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('patentee',)

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

        self.add_polyline('page',(24,32),(8,32),(8,4),(30,4),(40,14),(40,32))
        self.add_polyline('fold',(30,4),(30,14),(40,14));self.relate('connect','fold','page')
        self.add_line('writing',(17,15),(25,15))
        self.circle('seal',32,32,8);self.relate('connect','seal','page')
        self.add_polyline('ribbon',(26,38),(26,44),(32,41),(38,44),(38,38))
