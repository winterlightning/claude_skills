from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '98f6fd32-ffa9-4713-85d4-721b3399c95c'
SOURCE_PATH = 'icon_set/work/todo-references/sign language thank you_98f6fd32-ffa9-4713-85d4-721b3399c95c.svg'
AUTHOR = 'gpt-6'
# Plan: Open hand with four upright fingers, left thumb and downward motion arrow by the palm.
# Construction references: hand: rounded fingertips and coherent palm; human_ref/user.svg and full_body_ref.png inspected for shared human vocabulary, no detached head in this subject.
# Reduction: Omitted minor palm crease; retained four fingers, thumb and motion arrow.

class AuthoredIcon(Solo48):
    icon_id = 'sign-language-thank-you'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('sign', 'language', 'thank', 'you')

    def build(self):
        self.add_bezier('outline',(25,40),((13,40),(8,37),(7,29)),((4,20),(7,19),(11,27)))
        self.add_line('thumb-web',(11,27),(15,10))
        self.add_arc('index-tip',(15,10),(21,10),radius_x=3)
        self.add_line('index-side',(21,10),(18,25))
        self.add_line('middle-left',(20,16),(22,9))
        self.add_arc('middle-tip',(22,9),(28,9),radius_x=3)
        self.add_line('middle-right',(28,9),(25,25))
        self.add_line('ring-left',(28,13),(30,12))
        self.add_arc('ring-tip',(30,12),(36,14),radius_x=4)
        self.add_line('ring-right',(36,14),(33,27))
        self.add_arc('little-tip',(35,19),(41,21),radius_x=4)
        self.add_line('little-side',(41,21),(39,29))
        self.add_bezier('palm',(25,40),((33,41),(36,35),(36,31)))
        for a,b in [('outline','thumb-web'),('thumb-web','index-tip'),('index-tip','index-side'),('middle-left','middle-tip'),('middle-tip','middle-right'),('ring-left','ring-tip'),('ring-tip','ring-right'),('little-tip','little-side'),('palm','outline')]:self.relate('connect',a,b)
        self.add_bezier('motion',(29,28),((40,28),(42,34),(42,42)))
        self.add_polyline('motion-head',(38,38),(42,42),(46,38));self.relate('connect','motion','motion-head')

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
