from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '405a762c-b2c7-43c2-8ccd-42ddd4967863'
SOURCE_PATH = 'icon_set/work/todo-references/square person confined_405a762c-b2c7-43c2-8ccd-42ddd4967863.svg'
AUTHOR = 'gpt-6'
# Plan: Square enclosure containing a frontal person with a closed torso and two arm seams.
# References: human_ref/user.svg and full_body_ref.png: circular head, broad smooth shoulders and exact detached gap.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-person-confined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'person', 'confined')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.circle('head',24,17,3)
        self.add_bezier('torso',(24,28),((18,28),(15,29),(15,32)))
        self.add_bezier('right-shoulder',(24,28),((30,28),(33,29),(33,32)))
        self.add_polyline('body-base',(15,32),(15,35),(33,35),(33,32))
        self.relate('connect','torso','right-shoulder');self.relate('connect','torso','body-base');self.relate('connect','right-shoulder','body-base')
        for n,x in [('left',20),('right',28)]:self.add_line(n+'-arm',(x,32),(x,35));self.relate('connect',n+'-arm','body-base')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
