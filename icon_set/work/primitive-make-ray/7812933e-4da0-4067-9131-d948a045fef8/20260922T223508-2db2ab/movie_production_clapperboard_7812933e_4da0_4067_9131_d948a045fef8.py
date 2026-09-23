from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7812933e-4da0-4067-9131-d948a045fef8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/clapboard_7812933e-4da0-4067-9131-d948a045fef8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'movie-production-clapperboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('movie', 'production', 'clapperboard')

    def build(self):
        # Blank film slate under a striped band and raised striped clapper. Shared hinge(8,22); stripe series uses two members on each band, split at attachment points. Square ink(4,4)-(44,44), deliberate upward-right slant.
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
        self.add_polyline('slate',(6,22),(8,22),(18,22),(38,22),(42,22),(42,30),(42,42),(6,42),(6,30),closed=True)
        self.add_polyline('band-bottom',(6,30),(10,30),(30,30),(42,30))
        self.relate('connect','slate','band-bottom')
        self.add_polyline('clapper',(6,14),(18,11),(34,7),(38,6),(40,14),(28,17),(12,21),(8,22),closed=True)
        self.relate('connect','clapper','slate')
        for n,a,b in [('upper-1',(18,11),(12,21)),('upper-2',(34,7),(28,17))]:
            self.add_line(n,a,b);self.relate('connect',n,'clapper')
        for n,a,b in [('lower-1',(18,22),(10,30)),('lower-2',(38,22),(30,30))]:
            self.add_line(n,a,b);self.relate('connect',n,'slate');self.relate('connect',n,'band-bottom')
