'A broad upright triangle is divided into three horizontal tiers by two straight lines. The lowest section is widest, while the upper section narrows to a sharp point.\nPlan: Triangular food pyramid with three horizontal tiers. Split the outer sides at actual divider endpoints.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fe450a0-7b8a-4b59-ae18-c45d80fa1596'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/calories food pyramid_1fe450a0-7b8a-4b59-ae18-c45d80fa1596.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tier-outline-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'tier', 'outline', 'pyramid')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        poly('triangle',(24,6),(30,18),(36,30),(42,42),(6,42),(12,30),(18,18),(24,6))
        for y,l,r in [(18,18,30),(30,12,36)]:line(f'tier-{y}',(l,y),(r,y));join('triangle',f'tier-{y}')
