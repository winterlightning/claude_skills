from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4813164b-bbb2-498a-aa24-70f1ec279cb1'
SOURCE_PATH = 'icon_set/work/todo-references/passport ticket_4813164b-bbb2-498a-aa24-70f1ec279cb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A passport in front of a travel ticket.
    Plan: Foreground passport with a globe; tilted notched ticket behind it, with two writing rules.
    Reference: ticket: notched perimeter; supplied source owns the overlapping arrangement.
    """
    icon_id = 'passport-ticket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('passport', 'ticket')

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

        self.rounded('passport',6,18,26,42,3)
        self.add_line('ticket-left-1',(20, 18),(23, 6))
        self.add_line('ticket-left-2',(23, 6),(30, 8))
        self.add_arc('notch',(30,8),(36,10),radius_x=3,sweep=False)
        self.add_line('ticket-right-1',(36, 10),(42, 12))
        self.add_line('ticket-right-2',(42, 12),(36, 42))
        self.add_line('ticket-right-3',(36, 42),(26, 40))
        self.add_contour('ticket','ticket-left-1','ticket-left-2','notch','ticket-right-1','ticket-right-2','ticket-right-3')
        self.circle('globe',16,29,6)
        self.add_line('equator',(10,29),(22,29));self.relate('connect','equator','globe')
        self.circle('meridian',16,29,2,6);self.relate('connect','meridian','globe');self.relate('connect','equator','meridian')
        for i,y in enumerate((20,28)):self.add_line(f'ticket-text-{i}',(30,y),(35,y+1))
