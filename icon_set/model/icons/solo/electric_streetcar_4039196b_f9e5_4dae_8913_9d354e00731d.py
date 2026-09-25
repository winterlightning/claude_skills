"""A side-view electric streetcar with two window panes, equal wheels and a roof trolley pole. Extrema 4,8,44,40.
Construction: bus: equal wheels and divided glazing
Reduction: Window frames integrated into the upper body band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4039196b-f9e5-4dae-8913-9d354e00731d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trolley_4039196b-f9e5-4dae-8913-9d354e00731d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='electric-streetcar'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('electric', 'streetcar')
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

        path('body',(4,18),[('A',(8,14),4,4,True),('L',(24,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,24)),('L',(44,32)),('L',(34,32)),('L',(14,32)),('L',(4,32)),('L',(4,24)),('L',(4,18))],True)
        for x in (14,34):circle('wheel-'+str(x),x,36,4);join('wheel-'+str(x),'body')
        poly('window-sill',(4,24),(24,24),(44,24));line('window-divider',(24,14),(24,24));join('window-sill','body');join('window-divider','body');join('window-divider','window-sill')
        line('trolley-pole',(24,14),(34,8));join('trolley-pole','body')
