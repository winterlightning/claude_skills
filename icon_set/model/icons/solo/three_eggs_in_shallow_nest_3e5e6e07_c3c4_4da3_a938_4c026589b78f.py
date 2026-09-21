'Three upright eggs sit side by side within a shallow bowl-shaped nest. Their pointed tops rise above the curved rim, while their lower portions are hidden inside.\nPlan: Three eggs rise above a shallow bowl nest; silhouettes are occluded at a common rim. Straw texture removed.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e5e6e07-c3c4-4da3-a938-4c026589b78f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brood_3e5e6e07-c3c4-4da3-a938-4c026589b78f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-eggs-in-shallow-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'eggs', 'in', 'shallow', 'nest')

    # Repair: Shared egg apex y=8 gives exact HRECT_L envelope without fractional extrema.
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

        path('nest',(4,28),[('L',(17,28)),('L',(31,28)),('L',(44,28)),('C',(24,40),(42,38),(34,40)),('C',(4,28),(14,40),(6,38))],True)
        for j,(x1,x2,xc) in enumerate([(4,17,10),(17,31,24),(31,44,38)]):
         path(f'egg-{j}',(x1,28),[('C',(xc,8),(x1,18),(xc-4,8)),('C',(x2,28),(xc+4,8),(x2,18))]);join('nest',f'egg-{j}')
        join('egg-0','egg-1');join('egg-1','egg-2')
