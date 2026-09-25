'overlapping-clouds: Replace the rear circular disc with a scalloped cloud silhouette, partially hidden by the foreground cloud. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '543688ea-82f8-4c16-8c6f-17f3acc09590'
SOURCE_PATH = 'pictographic-primitives/weather/weather clouds_543688ea-82f8-4c16-8c6f-17f3acc09590.svg'
AUTHOR = 'gpt-6'

class OverlappingClouds(Solo48):
    icon_id = 'overlapping-clouds'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('cloud', 'overcast', 'sky', 'weather', 'cloudy', 'atmosphere')

    def build(self):
        # Symbol plan: Replace the rear circular disc with a scalloped cloud silhouette, partially hidden by the foreground cloud.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('front',(12,40),[('A',(12,24),8,8,True),('A',(28,24),8,8,True),('A',(36,32),8,8,True),('A',(28,40),8,8,True),('L',(12,40))],True)
        path('rear',(20,16),[('A',(40,16),10,10,True),('C',(44,24),(44,16),(44,20)),('C',(36,32),(44,28),(42,32))])
        join('front','rear')
