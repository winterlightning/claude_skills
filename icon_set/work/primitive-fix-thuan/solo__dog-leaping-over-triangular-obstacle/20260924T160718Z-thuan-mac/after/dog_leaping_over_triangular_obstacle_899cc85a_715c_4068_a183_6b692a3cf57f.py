"""Right-facing leaping dog over triangular hurdle. Lucide dog informs smooth organic contours; original reference supplies airborne side pose. Open spine and legs replace narrow doubled anatomy; retain head, muzzle, tail and triangle.
Keyshape HRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='899cc85a-715c-4068-a183-6b692a3cf57f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dog-leaping-over-triangular-obstacle/20260924T160718Z-thuan-mac/reference/dog race compettion 2_899cc85a-715c-4068-a183-6b692a3cf57f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='dog-leaping-over-triangular-obstacle'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('dog', 'leaping', 'over', 'triangular', 'obstacle')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('back',(4,8),[('C',(14,16),(4,14),(8,16)),('L',(28,16)),('C',(34,8),(32,16),(30,8)),('C',(40,12),(38,8),(37,12)),('L',(44,13)),('L',(44,17))])
        path('hind-leg',(14,16),[('C',(4,26),(12,23),(10,26))])
        path('front-leg',(28,16),[('C',(36,25),(29,21),(30,25)),('L',(44,25))])
        join('back','hind-leg');join('back','front-leg')
        poly('obstacle',(16,40),(24,31),(32,40),closed=True)
