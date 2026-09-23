from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4a5d4a34-afe6-4020-b1fa-c429eb47cc78'
SOURCE_PATH = 'icon_set/work/todo-references/spellbook_4a5d4a34-afe6-4020-b1fa-c429eb47cc78.svg'
AUTHOR = 'gpt-6'
# Plan: Open spellbook with a star on its left page and a lower cover edge.
# References: book-open: mirrored page contours with a central gutter.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'spellbook'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('spellbook',)

    def build(self):
        self.add_bezier('top-left',(6,10),((6,6),(20,4),(24,12)))
        self.add_bezier('top-right',(24,12),((28,4),(42,6),(42,10)))
        self.add_polyline('outer',(42,10),(42,42),(6,42),(6,10))
        self.add_line('spine',(24,12),(24,39))
        self.add_bezier('pages',(6,37),((14,37),(19,35),(24,39)),((29,35),(34,37),(42,37)))
        for a,b in [('top-left','top-right'),('top-left','outer'),('top-right','outer'),('spine','top-left'),('spine','top-right'),('spine','pages'),('pages','outer')]:self.relate('connect',a,b)
        self.add_polyline('star',(15,17),(17,22),(22,22),(18,25),(19,30),(15,27),(11,30),(12,25),(8,22),(13,22),closed=True)

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
