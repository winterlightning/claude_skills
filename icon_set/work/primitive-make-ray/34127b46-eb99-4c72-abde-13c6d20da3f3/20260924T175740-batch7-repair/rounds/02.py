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
        # Open left bowl and a hooked vertical stem retain the distinctive Path monogram.
        self.add_arc('bowl-top',(8,20),(40,20),radius_x=16)
        self.add_arc('bowl-lower',(40,20),(24,36),radius_x=16)
        self.add_contour('bowl','bowl-top','bowl-lower')
        self.add_line('stem',(24,16),(24,36));self.relate('connect','stem','bowl')
        self.add_arc('hook',(24,36),(16,44),radius_x=8)
        self.add_line('foot',(16,44),(8,44));self.relate('connect','hook','foot');self.relate('connect','hook','stem');self.relate('connect','hook','bowl')
