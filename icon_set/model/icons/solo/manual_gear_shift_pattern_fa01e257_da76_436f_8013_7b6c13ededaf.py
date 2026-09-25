from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa01e257-da76-436f-8013-7b6c13ededaf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/car dashboard gear_fa01e257-da76-436f-8013-7b6c13ededaf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'manual-gear-shift-pattern'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('manual', 'gear', 'shift', 'pattern')

    def build(self):
        # Three equal circular nodes joined by one orthogonal stepped loop; shared radius4 and explicit cardinal attachment points. SQUARE visible (4,4)-(44,44). Deliberate stepped asymmetry follows reference.
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
        for n,x,y in [('lower',10,38),('middle',26,26),('upper',38,10)]:
            circle(n,x,y,4)
        self.add_polyline('outer-route',(10,34),(10,10),(34,10))
        self.add_polyline('upper-route',(38,14),(38,26),(30,26))
        self.add_polyline('lower-route',(26,30),(26,38),(14,38))
        for a,b in [('outer-route','lower'),('outer-route','upper'),('upper-route','upper'),('upper-route','middle'),('lower-route','middle'),('lower-route','lower')]:
            self.relate('connect',a,b)
