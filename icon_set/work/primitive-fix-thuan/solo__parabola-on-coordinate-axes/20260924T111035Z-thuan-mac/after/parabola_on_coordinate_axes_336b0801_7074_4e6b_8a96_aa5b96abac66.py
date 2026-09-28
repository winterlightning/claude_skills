"""Restore a symmetric parabola with steeper sides and evenly angled axis arrow. Split true intersections.
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '336b0801-7074-4e6b-8a96-aa5b96abac66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__parabola-on-coordinate-axes/20260924T111035Z-thuan-mac/reference/science axis_336b0801-7074-4e6b-8a96-aa5b96abac66.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'parabola-on-coordinate-axes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('parabola', 'on', 'coordinate', 'axes')
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

        poly('vertical',(24,6),(24,24),(24,36),(24,42))
        poly('horizontal',(6,36),(24,36),(42,36));join('vertical','horizontal')
        path('curve',(6,8),[('C',(24,24),(12,20),(18,24)),('C',(42,8),(30,24),(36,20))])
        join('curve','vertical')
        poly('arrow',(36,30),(42,36),(36,42));join('arrow','horizontal')
