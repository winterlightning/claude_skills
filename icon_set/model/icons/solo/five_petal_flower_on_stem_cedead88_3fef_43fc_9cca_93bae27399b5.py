"""Five distinct curved petals sit on a central stem with mirrored leaf strokes. Extrema 8,4,40,44.
Construction: flower and flower-2: five coherent lobes and paired foliage
Reduction: Seed ring reduced to a dot; secondary leaf edges omitted for spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cedead88-3fef-43fc-9cca-93bae27399b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jasmine_cedead88-3fef-43fc-9cca-93bae27399b5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='five-petal-flower-on-stem'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('five', 'petal', 'flower', 'on', 'stem')
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

        path('bloom',(24,4),[('C',(30,12),(28,4),(30,8)),('C',(40,16),(36,9),(40,10)),('C',(34,24),(40,21),(38,24)),('C',(32,32),(38,28),(37,32)),('C',(24,28),(28,32),(26,30)),('C',(16,32),(22,30),(20,32)),('C',(14,24),(11,32),(10,28)),('C',(8,16),(10,24),(8,22)),('C',(18,12),(8,10),(12,9)),('C',(24,4),(18,8),(20,4))],True)
        line('stem',(24,28),(24,44));join('stem','bloom')
        self.add_dot('centre',(24,19))

        path('leaves',(8,39),[('C',(24,44),(14,39),(19,42)),('C',(40,39),(29,42),(34,39))]);join('stem','leaves')
