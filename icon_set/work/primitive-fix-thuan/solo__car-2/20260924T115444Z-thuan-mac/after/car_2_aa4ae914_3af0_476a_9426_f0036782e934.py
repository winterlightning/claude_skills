"""Restore a wide divided window and smoothly rounded roof shoulders above two separate wheels.
Construction: Lucide car: rounded shoulder transitions and full wheels; source window division retained.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aa4ae914-3af0-476a-9426-f0036782e934'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-2/20260924T115444Z-thuan-mac/reference/car 2_aa4ae914-3af0-476a-9426-f0036782e934.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-2'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('car', '2')
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

        path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,25)),('A',(8,21),4,4,True),('L',(16,12)),('C',(20,10),(17,10),(18,10)),('L',(24,10)),('L',(28,10)),('C',(32,12),(30,10),(31,11)),('L',(40,21)),('A',(44,25),4,4,True),('L',(44,30)),('A',(41,33),3,3,True)])
        poly('window-base',(8,21),(24,21),(40,21));join('window-base','body')
        line('pillar',(24,10),(24,21));join('pillar','body');join('pillar','window-base')

        for x in (12,36):circle(f'wheel-{x}',x,33,5)
        line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
        join('body','wheel-12');join('body','wheel-36')
