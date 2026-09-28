"""Hand holding two cards with rounded card corners and a continuous thumb.
Plan: Hand holding two cards with rounded card corners and a continuous thumb.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Card face marks and finger creases omitted."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9e452a20-d223-431c-a550-2caad608f489'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-holding-two-game-cards/20260924T162241Z-thuan-mac/reference/card game cards hold_9e452a20-d223-431c-a550-2caad608f489.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-holding-two-game-cards'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hand', 'holding', 'two', 'game', 'cards')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        # Cards and thumb use 8-unit-wide lanes. Curved corners are split from straight edges so exact parallel gaps remain certifiable.
        path('front-top',(16,20),[('L',(16,6)),('A',(18,4),2,2,True),('L',(30,4)),('A',(32,6),2,2,True)])
        line('front-side',(32,6),(32,26));join('front-side','front-top')
        path('front-bottom',(32,26),[('A',(30,28),2,2,True),('L',(24,28))]);join('front-bottom','front-side')
        line('rear-side',(40,12),(40,32))
        path('rear-bottom',(40,32),[('A',(36,36),4,4,True),('L',(32,36))]);join('rear-side','rear-bottom')
        path('hand',(8,20),[('L',(8,28)),('L',(8,36)),('C',(13,44),(8,40),(10,44)),('L',(24,44)),('L',(24,36)),('L',(24,28)),('L',(24,20)),('A',(16,20),4,4,False),('L',(16,28)),('L',(8,28))])
        line('cuff',(8,36),(24,36));join('hand','front-top');join('hand','front-bottom');join('hand','cuff')
