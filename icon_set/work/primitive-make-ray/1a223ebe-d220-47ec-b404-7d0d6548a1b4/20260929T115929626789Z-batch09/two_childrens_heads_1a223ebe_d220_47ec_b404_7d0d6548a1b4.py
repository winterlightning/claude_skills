"""Children: rejected heads have no hairlines and resemble rings. Restore parted hair and a readable ponytail. Restore parted bangs in both heads and a curled ponytail on the lower child.
Symbol plan: human_ref/user.svg circular head proportions; source offset pair and parted hair.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1a223ebe-d220-47ec-b404-7d0d6548a1b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-childrens-heads/20260929T115456Z-thuan-mac/reference/kids head_1a223ebe-d220-47ec-b404-7d0d6548a1b4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-childrens-heads'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'childrens', 'heads')

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

        circle('upper-head',16,16,10)
        poly('upper-hair',(6,16),(10,16),(16,12),(22,16),(26,16));join('upper-hair','upper-head')
        circle('lower-head',30,32,10)
        poly('lower-hair',(20,32),(24,32),(30,28),(36,32),(40,32));join('lower-hair','lower-head')
        join('upper-head','lower-head')
        path('ponytail',(36,24),[('C',(42,18),(36,16),(40,14))]);join('ponytail','lower-head')
