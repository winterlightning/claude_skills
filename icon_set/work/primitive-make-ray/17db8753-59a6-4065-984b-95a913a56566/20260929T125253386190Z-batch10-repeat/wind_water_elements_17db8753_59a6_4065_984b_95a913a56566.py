"""The rejected water drops were triangular wedges. Restore two rounded teardrops and the upper-right curled wind stroke.
Symbol plan: Lucide wind original and atoms inform the curling run; original rounded droplets retained.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '17db8753-59a6-4065-984b-95a913a56566'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wind-water-elements/20260929T124732Z-thuan-mac/reference/elements_17db8753-59a6-4065-984b-95a913a56566.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wind-water-elements'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wind', 'water', 'elements')

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

        path('drop-a',(12,8),[('C',(4,20),(8,14),(4,16)),('A',(20,20),8,6,False),('C',(12,8),(20,16),(16,12))],True)
        path('drop-b',(32,24),[('C',(24,34),(28,28),(24,31)),('A',(40,34),8,6,False),('C',(32,24),(40,31),(36,28))],True)
        path('wind',(28,16),[('L',(38,16)),('A',(44,10),6,6,False),('C',(40,8),(44,8),(42,8))])
