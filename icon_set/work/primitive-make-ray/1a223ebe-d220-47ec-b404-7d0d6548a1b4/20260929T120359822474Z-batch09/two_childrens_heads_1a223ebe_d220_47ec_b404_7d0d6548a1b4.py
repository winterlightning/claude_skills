"""Children: rejected heads have no hairlines and resemble rings. Restore parted hair and a readable ponytail. Restore two child hairlines and a curved ponytail; use touching circular faces at shared tangent point.
Symbol plan: human_ref/user.svg: circular jaws; two hairlines restore the children, with original diagonal arrangement.
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

        path('upper-head',(22,24),[('A',(6,16),10,10,True),('A',(16,6),10,10,True),('A',(26,16),10,10,True),('A',(22,24),10,10,True)],True)
        path('lower-head',(22,24),[('A',(34,24),10,10,True),('A',(38,32),10,10,True),('A',(28,42),10,10,True),('A',(18,32),10,10,True),('A',(22,24),10,10,True)],True)
        join('upper-head','lower-head')
        line('upper-hair',(6,16),(26,16));join('upper-hair','upper-head')
        line('lower-hair',(18,32),(38,32));join('lower-hair','lower-head')
        path('ponytail',(34,24),[('C',(42,18),(34,14),(42,12))]);join('ponytail','lower-head')
