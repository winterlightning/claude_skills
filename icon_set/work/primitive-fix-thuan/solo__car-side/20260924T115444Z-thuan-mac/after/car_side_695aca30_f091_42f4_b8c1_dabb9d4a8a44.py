"""Restore equal circular wheels, soft cabin shoulders and rounded body corners for the side-view car.
Construction: Lucide car: shared wheel radius and smooth shell construction.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-side/20260924T115444Z-thuan-mac/reference/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-side'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('car', 'side')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,27)),('A',(10,21),6,6,True),('L',(38,21)),('A',(44,27),6,6,True),('L',(44,30)),('A',(41,33),3,3,True)])
        path('roof',(10,21),[('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,10)),('L',(38,21))]);join('roof','body')

        for x in (12,36):circle(f'wheel-{x}',x,33,5)
        line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
        join('body','wheel-12');join('body','wheel-36')
