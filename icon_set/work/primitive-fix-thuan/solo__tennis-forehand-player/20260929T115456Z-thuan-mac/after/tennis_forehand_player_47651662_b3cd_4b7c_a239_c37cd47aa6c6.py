"""Tennis player: rejected head floats off a sloping torso and the racket is too small. Enlarge head/racket, align neck tangent, preserve forehand stance. Rebuilt with a larger head, oval racket and curved torso.
Symbol plan: human_ref/full_body_ref.png: circular head radius5, lower edge16 to neck24 gives exact4 ink gap; tangent follows head.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47651662-b3cd-4b7c-a239-c37cd47aa6c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tennis-forehand-player/20260929T115456Z-thuan-mac/reference/tennis forehand_47651662-b3cd-4b7c-a239-c37cd47aa6c6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'tennis-forehand-player'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tennis', 'forehand', 'player')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        circle('head',20,11,5)
        line('torso',(20,24),(20,26))
        path('lower-torso',(20,26),[('C',(18,33),(20,29),(19,31))]);join('torso','lower-torso')
        poly('back-arm',(20,24),(12,26),(8,31));join('back-arm','torso')
        poly('racket-arm',(20,24),(28,30),(34,30));join('racket-arm','torso');join('racket-arm','back-arm')
        poly('legs',(6,42),(14,38),(18,33),(26,38),(26,42));join('legs','lower-torso')
        path('racket',(32,20),[('A',(42,20),5,7,True),('A',(32,20),5,7,True)],True)
        line('shaft',(37,27),(34,30));join('shaft','racket');join('shaft','racket-arm')
        self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
