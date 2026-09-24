"""Desktop monitor with a diagonal editing pencil.
Plan: SQUARE includes screen, stand and pencil.
Reduction: Pencil shortened within the screen opening; small tip divider omitted; eraser band retained.
Construction: pencil: coherent diagonal shaft and cap; monitor: screen and centered stand. Intentional pencil diagonal.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '242c5167-10ea-4717-a24b-bd22d2cf9483'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pencil edit desktop_242c5167-10ea-4717-a24b-bd22d2cf9483.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pencil-edit-desktop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pencil', 'edit', 'desktop')

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

        self.add_polyline('screen',(18,16),(6,16),(6,34),(20,34),(34,34),(34,24))
        self.add_line('stand',(20,34),(20,42));self.relate('connect','stand','screen')
        self.add_polyline('foot',(12,42),(20,42),(28,42));self.relate('connect','foot','stand')
        self.add_line('pencil-a-1',(14, 24),(18, 16))
        self.add_line('pencil-a-2',(18,16),(24,11))
        self.add_line('pencil-a-3',(24,11),(30,6))
        self.add_arc('eraser',(30,6),(42,18),radius_x=12)
        self.add_line('pencil-b-1',(42,18),(34,24))
        self.add_line('pencil-b-mid',(34,24),(26,24))
        self.add_line('pencil-b-2',(26, 24),(14, 24))
        self.add_contour('pencil','pencil-a-1','pencil-a-2','pencil-a-3','eraser','pencil-b-1','pencil-b-mid','pencil-b-2',closed=True)
        self.add_line('band',(24,11),(34,24));self.relate('connect','band','pencil')

        self.relate("connect","screen","pencil")
