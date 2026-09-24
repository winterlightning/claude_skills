from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4236f26b-6e26-4a4e-b565-3dda332eac7d'
SOURCE_PATH = 'icon_set/work/todo-references/south east_4236f26b-6e26-4a4e-b565-3dda332eac7d.svg'
AUTHOR = 'gpt-6'
# Plan: Compass dial with four ticks and a pointer above the label SE.
# References: compass: circular dial and geometric pointer; letters authored as strokes.
# Reduction: No parts omitted; pointer direction follows the supplied reference.

class AuthoredIcon(Solo48):
    icon_id = 'south-east'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('south', 'east')

    def build(self):
        self.circle('dial',24,20,16)
        for n,a,b in [('north',(24,4),(24,7)),('south',(24,33),(24,36)),('west',(8,20),(11,20)),('east',(37,20),(40,20))]:
            self.add_line(n,a,b);self.relate('connect',n,'dial')
        self.add_polyline('pointer',(19,20),(29,14),(25,26),(23,22),closed=True)
        self.add_bezier('s',(20,39),((11,35),(11,42),(17,41)),((23,40),(22,46),(13,43)))
        self.add_polyline("e",(34,38),(26,38),(26,44),(34,44));self.add_line("e-bar",(26,41),(32,41));self.relate("connect","e","e-bar")

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
