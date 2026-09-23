from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f8998b5a-15d8-45ce-9679-4cac7ab954c3'
SOURCE_PATH = 'icon_set/work/todo-references/snorer_f8998b5a-15d8-45ce-9679-4cac7ab954c3.svg'
AUTHOR = 'gpt-6'
# Plan: Sleeping person in bed with two hand-authored Z marks overhead.
# References: bed: simple bedding silhouette; human_ref/user.svg and full_body_ref.png: circular head and smooth shoulder construction.
# Reduction: Omitted minor pillow crease; retained pillow, blanket and both Zs.

class AuthoredIcon(Solo48):
    icon_id = 'snorer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('snorer',)

    def build(self):
        self.circle('head',16,25,6)
        self.add_bezier('torso',(16,39),((18,39),(21,41),(24,42)))
        self.mark_human_figure('sleeper',head='head',torso='torso',torso_junction='start')
        self.add_polyline('pillow',(15,34),(6,34),(6,42),(24,42));self.relate('connect','pillow','torso')
        self.add_bezier('blanket-top',(24,42),((26,31),(26,30),(31,30)),((36,30),(42,28),(42,35)))
        self.add_polyline('blanket-base',(42,35),(42,42),(24,42));self.relate('connect','blanket-top','blanket-base');self.relate('connect','blanket-top','torso')
        for n,x,y in [('small',23,15),('large',33,6)]:self.add_polyline(n,(x,y),(x+6,y),(x,y+6),(x+6,y+6))

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
