"""Round the cargo box and cab corners; restore complete wheels with clean shared axle-height attachments.
Construction: Lucide truck: round wheels, cargo/cab height contrast and sloped windshield.
Omissions: Cargo lower stripe omitted for wheel clearance.
Keyshape HRECT_L: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd23c80b5-df62-4255-b184-b83a86285322'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cargo-delivery-truck/20260924T115444Z-thuan-mac/reference/truck cargo_d23c80b5-df62-4255-b184-b83a86285322.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cargo-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('cargo', 'delivery', 'truck')
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

        path('body',(7,35),[('A',(4,32),3,3,True),('L',(4,12)),('A',(8,8),4,4,True),('L',(24,8)),('A',(28,12),4,4,True),('L',(28,17)),('L',(28,26)),('L',(28,35)),('L',(17,35))])
        path('cab',(28,17),[('L',(33,17)),('C',(37,20),(35,17),(36,18)),('L',(40,26)),('A',(44,30),4,4,True),('L',(44,32)),('A',(41,35),3,3,True)])
        line('cab-floor',(28,35),(31,35));line('window',(28,26),(40,26))
        for x in (12,36):circle(f'wheel-{x}',x,35,5)
        join('body','wheel-12');join('cab','wheel-36');join('body','cab');join('window','body');join('window','cab');join('cab-floor','body');join('cab-floor','wheel-36')
