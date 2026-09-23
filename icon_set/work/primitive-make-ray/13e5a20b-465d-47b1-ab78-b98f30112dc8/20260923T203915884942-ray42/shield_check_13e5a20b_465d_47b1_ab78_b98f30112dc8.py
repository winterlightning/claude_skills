from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '13e5a20b-465d-47b1-ab78-b98f30112dc8'
SOURCE_PATH = 'icon_set/work/todo-references/shield check_13e5a20b-465d-47b1-ab78-b98f30112dc8.svg'
AUTHOR = 'gpt-6'
# Plan: Crested shield enclosing a check mark.
# Construction references: shield-check: broad clear shield and a simple joined check.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shield-check'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shield', 'check')

    def build(self):
        self.shield()
        self.add_polyline('check',(18,25),(23,30),(31,21))

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

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
