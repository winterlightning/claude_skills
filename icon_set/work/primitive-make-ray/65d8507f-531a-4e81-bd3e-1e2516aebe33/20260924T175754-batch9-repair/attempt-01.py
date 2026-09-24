from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '65d8507f-531a-4e81-bd3e-1e2516aebe33'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/route interstate_65d8507f-531a-4e81-bd3e-1e2516aebe33.svg'
AUTHOR = 'gpt-6'
# Plan: Interstate shield with scalloped top, header rule and road center dashes.
# Reference: shield: mirrored protective silhouette with a pointed base.
# Reduction: Two center dashes retained; no text added because source contains none.

class AuthoredIcon(Solo48):
    icon_id = 'route-interstate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('route', 'interstate')

    def build(self):
        # Mirrored scalloped shield; header attaches at explicit side nodes.
        self.add_bezier('left-top',(24,6),((19,8),(14,8),(11,4)))
        self.add_bezier('left-upper',(11,4),((9,9),(8,12),(8,17)))
        self.add_line('left-wall',(8,17),(8,19))
        self.add_bezier('left-lower',(8,19),((8,31),(15,40),(24,44)))
        self.add_bezier('right-lower',(24,44),((33,40),(40,31),(40,19)))
        self.add_line('right-wall',(40,19),(40,17))
        self.add_bezier('right-upper',(40,17),((40,12),(39,9),(37,4)))
        self.add_bezier('right-top',(37,4),((34,8),(29,8),(24,6)))
        self.add_contour('shield','left-top','left-upper','left-wall','left-lower','right-lower','right-wall','right-upper','right-top',closed=True)
        self.add_line('header',(8,17),(40,17));self.relate('connect','header','shield')
        self.add_line('road-mark',(24,26),(24,31))

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
