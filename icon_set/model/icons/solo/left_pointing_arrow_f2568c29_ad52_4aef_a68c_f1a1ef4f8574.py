from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2568c29-ad52-4aef-a68c-f1a1ef4f8574'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/caret left_f2568c29-ad52-4aef-a68c-f1a1ef4f8574.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-pointing-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('left', 'pointing', 'arrow')

    def build(self):
        # One closed left-arrow outline with an eight-unit shaft and symmetric diagonal arms. HRECT_L ink (2,6)-(46,42) preserves wide proportions; semicircular tail reaches x44.
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
        pts=[(4,24),(20,8),(26,14),(20,20),(40,20)]
        names=[]
        for i in range(len(pts)-1):
            n=f'upper-{i}'; self.add_line(n,pts[i],pts[i+1]); names.append(n)
        self.add_arc('tail',(40,20),(40,28),radius_x=4)
        names.append('tail')
        pts=[(40,28),(20,28),(26,34),(20,40),(4,24)]
        for i in range(len(pts)-1):
            n=f'lower-{i}'; self.add_line(n,pts[i],pts[i+1]); names.append(n)
        self.add_contour('arrow',*names,closed=True)
