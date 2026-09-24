"""Restore a flat-topped rounded cabin rather than a semicircle, and separate the circular wheels from the car body.
Construction: Lucide car: paired round wheels and coherent body; source rounded cabin.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-e1ae9ac1/20260924T115444Z-thuan-mac/reference/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-e1ae9ac1'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('car', 'e1ae9ac1')
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

        path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,27)),('A',(12,19),8,8,True),('L',(24,19)),('L',(36,19)),('A',(44,27),8,8,True),('L',(44,30)),('A',(41,33),3,3,True)])
        path('roof',(12,19),[('A',(21,10),9,9,True),('L',(24,10)),('L',(27,10)),('A',(36,19),9,9,True)])
        line('pillar',(24,10),(24,19));join('roof','body');join('pillar','roof');join('pillar','body')

        for x in (12,36):circle(f'wheel-{x}',x,33,5)
        line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
        join('body','wheel-12');join('body','wheel-36')
