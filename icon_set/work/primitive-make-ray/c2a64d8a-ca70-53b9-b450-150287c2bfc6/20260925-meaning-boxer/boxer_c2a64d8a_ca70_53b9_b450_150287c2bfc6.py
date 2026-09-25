from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer/20260925T034659Z-thuan-mac/reference/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
AUTHOR = 'gpt-6'
# Plan: Boxer in a wide fighting stance with one punching glove extended; replace generic head between disconnected mitten shapes.
# Construction reference: human_ref/full_body_ref.png round head and coherent limbs; head bottom12 to torso20 gives exact 4-unit ink gap.
# Envelope: VRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'boxer'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('boxer',)
    def build(self):
        self.circle('head',18,8,4)
        self.add_line('torso',(18,20),(18,32))
        self.add_polyline('legs',(10,44),(18,32),(30,44))
        self.add_line('rear-arm',(18,20),(8,28))
        self.add_line('punch-arm',(18,20),(28,24))
        self.add_line('glove-left',(28,24),(28,16))
        self.add_arc('glove-tl',(28,16),(32,12),radius_x=4)
        self.add_line('glove-top',(32,12),(36,12))
        self.add_arc('glove-tr',(36,12),(40,16),radius_x=4)
        self.add_line('glove-right',(40,16),(40,20))
        self.add_arc('glove-br',(40,20),(36,24),radius_x=4)
        self.add_line('glove-bottom',(36,24),(28,24))
        self.add_contour('glove','glove-left','glove-tl','glove-top','glove-tr','glove-right','glove-br','glove-bottom',closed=True)
        self.relate('connect','torso','legs')
        self.relate('connect','torso','rear-arm')
        self.relate('connect','torso','punch-arm')
        self.relate('connect','rear-arm','punch-arm')
        self.relate('connect','punch-arm','glove')
        self.mark_human_figure('boxer',head='head',torso='torso',torso_junction='start')

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
