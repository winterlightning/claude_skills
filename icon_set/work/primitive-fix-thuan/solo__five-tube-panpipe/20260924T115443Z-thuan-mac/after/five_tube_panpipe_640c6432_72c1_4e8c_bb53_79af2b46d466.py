"""Five equal-width panpipes descend in four-unit steps below a broad binding. Extrema 4,8,44,40.
Construction: No useful Lucide panpipe match; equal tube parameters and rounded ends
Reduction: No tubes omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='640c6432-72c1-4e8c-bb53-79af2b46d466'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__five-tube-panpipe/20260924T115443Z-thuan-mac/reference/panpipe_640c6432-72c1-4e8c-bb53-79af2b46d466.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='five-tube-panpipe'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('five', 'tube', 'panpipe')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('binding',(4,16),[('L',(4,11)),('A',(7,8),3,3,True),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,16)),('L',(36,16)),('L',(28,16)),('L',(20,16)),('L',(12,16)),('L',(4,16))],True)
        steps=[('L',(4,36))]
        for i in range(5):
            x=4+i*8;y=36-i*4
            steps.append(('A',(x+8,y),4,4,False))
            steps.append(('L',(x+8,y-4 if i<4 else 16)))
        path('pipes',(4,16),steps);join('pipes','binding')
        for i in range(1,5):
            x=4+i*8;bottom=36-i*4
            line('wall-'+str(i),(x,16),(x,bottom));join('wall-'+str(i),'binding');join('wall-'+str(i),'pipes')
