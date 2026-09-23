from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b3b9d031-1b14-49cd-b640-12d78e2f90f7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/burrito_b3b9d031-1b14-49cd-b640-12d78e2f90f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medical-capsule'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('medical', 'capsule')

    def build(self):
        # Horizontal capsule outline and bowed left seam, with diagonal end fold. HRECT_M visible (2,8)-(46,40) preserves wide proportions. Shared seam endpoints lie on outline.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        self.add_line('top',(18,10),(30,10))
        self.add_arc('right',(30,10),(30,38),radius_x=14)
        self.add_line('bottom',(30,38),(18,38))
        self.add_arc('left',(18,38),(18,10),radius_x=14)
        self.add_contour('outline','top','right','bottom','left',closed=True)
        self.add_arc('seam',(18,10),(18,38),radius_x=8,radius_y=14)
        self.relate('connect','seam','outline')
        self.add_line('fold',(8,34),(24,18))
