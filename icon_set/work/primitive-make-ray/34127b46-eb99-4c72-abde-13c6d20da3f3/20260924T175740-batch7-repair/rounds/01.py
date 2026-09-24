from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '34127b46-eb99-4c72-abde-13c6d20da3f3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/path logo_34127b46-eb99-4c72-abde-13c6d20da3f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """The outlined Path P logo.
    Plan: Continuous outer lobe and descending stem with rounded lower hook; inner lobe forms the P counter.
    Reference: No useful Lucide match; custom continuous arcs preserve the logo lobe and hooked stem.
    """
    icon_id = 'path-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('path', 'logo')

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
        # Single outlined P with broad stem, round bowl, hooked foot and one spacious counter.
        self.add_line('top',(12,4),(26,4))
        self.add_arc('bowl-top',(26,4),(40,18),radius_x=14)
        self.add_arc('bowl-bottom',(40,18),(26,32),radius_x=14)
        self.add_line('stem-right',(26,32),(26,36))
        self.add_arc('hook-right',(26,36),(18,44),radius_x=8)
        self.add_line('hook-bottom',(18,44),(12,44))
        self.add_arc('hook-left',(12,44),(8,40),radius_x=4)
        self.add_polyline('return',(8,40),(8,36),(12,36),(12,4))
        self.relate('connect','top','return');self.relate('connect','return','hook-left')
        self.add_contour('main','top','bowl-top','bowl-bottom','stem-right','hook-right','hook-bottom','hook-left')
        self.circle('counter',26,18,5)
