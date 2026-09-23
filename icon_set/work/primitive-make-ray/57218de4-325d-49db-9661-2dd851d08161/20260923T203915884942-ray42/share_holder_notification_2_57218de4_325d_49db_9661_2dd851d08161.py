from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '57218de4-325d-49db-9661-2dd851d08161'
SOURCE_PATH = 'icon_set/work/todo-references/share holder notification 2_57218de4-325d-49db-9661-2dd851d08161.svg'
AUTHOR = 'gpt-6'
# Plan: Notification bell above three shareholder busts, with shared head radii and exact own head-to-shoulder gaps.
# Construction references: bell: flared contour; human_ref/user.svg and full_body_ref.png: circular heads and smooth shoulders.
# Reduction: Omitted tiny bell top loop; retained bell clapper and all three people.

class AuthoredIcon(Solo48):
    icon_id = 'share-holder-notification-2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('share', 'holder', 'notification', '2')

    def build(self):
        self.add_bezier('bell',(14,18),((19,14),(15,6),(24,6)),((33,6),(29,14),(34,18)))
        self.add_line('bell-base',(34,18),(14,18));self.add_contour('bell-outline','bell','bell-base',closed=True)
        self.add_arc('clapper',(21,18),(27,18),radius_x=3,sweep=False);self.relate('connect','clapper','bell-outline')
        for n,x in [('left',11),('center',24),('right',37)]:
            self.circle(n+'-head',x,26,3)
            self.add_bezier(n+'-torso',(x,37),((x-3,37),(x-5,39),(x-5,42)))
            self.add_bezier(n+'-shoulder',(x,37),((x+3,37),(x+5,39),(x+5,42)))
            self.relate('connect',n+'-torso',n+'-shoulder')
            self.mark_human_figure(n,head=n+'-head',torso=n+'-torso',torso_junction='start')

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
