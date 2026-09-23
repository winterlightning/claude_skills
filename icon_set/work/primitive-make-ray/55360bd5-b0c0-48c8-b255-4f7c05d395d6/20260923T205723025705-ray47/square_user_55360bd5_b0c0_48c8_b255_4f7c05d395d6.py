from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '55360bd5-b0c0-48c8-b255-4f7c05d395d6'
SOURCE_PATH = 'icon_set/work/todo-references/square user_55360bd5-b0c0-48c8-b255-4f7c05d395d6.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with a circular user head and a smooth closed shoulder dome.
# References: human_ref/user.svg and full_body_ref.png: circular head, symmetric shoulders and exact detached gap.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-user'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'user')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.circle('head',24,17,3)
        self.add_arc('torso',(24,28),(15,34),radius_x=9,radius_y=6,sweep=False)
        self.add_line('base',(15,34),(33,34))
        self.add_arc('right-shoulder',(33,34),(24,28),radius_x=9,radius_y=6,sweep=False)
        self.add_contour('body','torso','base','right-shoulder',closed=True)
        self.mark_human_figure('user',head='head',torso='torso',torso_junction='start')

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
