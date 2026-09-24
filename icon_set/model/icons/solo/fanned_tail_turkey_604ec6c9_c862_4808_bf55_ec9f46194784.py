"""A right-facing turkey has a scalloped fan, long neck, pointed beak and two legs. Extrema 4,8,44,40.
Construction: No exact Lucide turkey; circular scallops and continuous bird outline
Reduction: Fine feather dividers and tiny eye omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '604ec6c9-c862-4808-bf55-ec9f46194784'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gobbler_604ec6c9-c862-4808-bf55-ec9f46194784.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='fanned-tail-turkey'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('fanned', 'tail', 'turkey')
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

        path('body',(18,30),[('A',(24,20),6,10,True),('L',(30,20)),('L',(30,12)),('A',(38,12),4,4,True),('L',(44,16)),('L',(38,20)),('L',(38,28)),('A',(30,36),8,8,True),('L',(22,36)),('A',(18,30),4,6,True)],True)
        path('fan',(18,30),[('L',(8,30)),('A',(4,26),4,4,True),('A',(8,22),4,4,True),('A',(4,18),4,4,True),('A',(8,14),4,4,True),('A',(14,8),6,6,True),('A',(20,14),6,6,True),('L',(24,20))]);join('fan','body')
        for x in (22,30):line('leg-'+str(x),(x,36),(x,40));join('leg-'+str(x),'body')
