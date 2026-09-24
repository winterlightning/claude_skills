"""Passport booklet overlapping a notched travel ticket.
Plan: SQUARE fits the complete overlap and exposed ticket edge.
Reduction: Ticket straightened; notch moved to the exposed side; writing lines and small globe grid omitted, leaving a circular cover seal.
Construction: ticket: open semicircular notch; supplied reference: front passport and rear ticket arrangement. Deliberate overlap asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4813164b-bbb2-498a-aa24-70f1ec279cb1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/passport ticket_4813164b-bbb2-498a-aa24-70f1ec279cb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
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
        # Passport cover and occluded ticket share two exact overlap nodes.
        self.add_polyline('passport',(6,14),(22,14),(30,14),(30,38),(30,42),(6,42),closed=True)
        self.add_polyline('ticket-upper',(22,14),(22,6),(42,6),(42,18))
        self.add_arc('ticket-notch',(42,18),(42,26),radius_x=4,sweep=False)
        self.add_polyline('ticket-lower',(42,26),(42,38),(30,38))
        self.relate('connect','passport','ticket-upper');self.relate('connect','passport','ticket-lower')
        self.relate('connect','ticket-upper','ticket-notch');self.relate('connect','ticket-lower','ticket-notch')
        self.circle('globe',18,28,3)
