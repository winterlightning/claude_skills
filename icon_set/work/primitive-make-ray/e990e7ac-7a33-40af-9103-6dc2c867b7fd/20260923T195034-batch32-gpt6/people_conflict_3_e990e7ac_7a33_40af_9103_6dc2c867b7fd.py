from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e990e7ac-7a33-40af-9103-6dc2c867b7fd'
SOURCE_PATH = 'icon_set/work/todo-references/people conflict 3_e990e7ac-7a33-40af-9103-6dc2c867b7fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """Two people facing each other beneath a conflict burst.
    Plan: Mirrored head profiles and central angular burst; faces intentionally point inward.
    Reference: No useful Lucide match; source-defined opposed profiles with a geometric burst.
    """
    icon_id = 'people-conflict-3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('people', 'conflict', '3')
    # Shared human_ref/user.svg reviewed. Connected head/neck profiles; no detached-head gap applies.

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

        self.add_arc('left-skull',(6,28),(22,28),radius_x=8)
        self.add_polyline('left-back',(6,28),(8,34),(6,42));self.relate('connect','left-back','left-skull')
        self.add_polyline('left-face',(22,28),(24,34),(20,34),(20,38),(16,38),(14,42));self.relate('connect','left-face','left-skull')
        self.add_arc('right-skull',(26,28),(42,28),radius_x=8)
        self.add_polyline('right-face',(26,28),(24,34),(28,34),(28,38),(32,38),(34,42));self.relate('connect','right-face','right-skull')
        self.add_polyline('right-back',(42,28),(40,34),(42,42));self.relate('connect','right-back','right-skull')
        self.add_polyline('burst',(14,14),(14,8),(20,11),(24,6),(28,11),(34,8),(34,14))
