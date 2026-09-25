"""Sun with a Small Surface Spot
Plan: Sun disk with one surface spot and eight attached rays. Rays meet at cardinal and 3:4:5 circle points.
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: Lucide sun: balanced rays around one central disk.
Reduction: Reduced nine uneven rays to eight balanced rays; retained surface spot.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a16304c-7690-48e3-b751-e98527720251'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy planet_6a16304c-7690-48e3-b751-e98527720251.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-a-small-surface-spot'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'rays', 'spot', 'star', 'astronomy', 'solar', 'radiant')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        # The repeated ray definition owns exact circle junctions and radius 15.
        nodes=[(24,9),(33,12),(39,24),(36,33),(24,39),(15,36),(9,24),(12,15)]
        tips=[(24,4),(36,8),(44,24),(40,36),(24,44),(12,40),(4,24),(8,12)]
        path('sun',nodes[0],[('A',nodes[(j+1)%8],15,15,True) for j in range(8)],True)
        for j,(node,tip) in enumerate(zip(nodes,tips)):
            self.add_line(f'ray-{j}',node,tip)
            self.relate('connect',f'ray-{j}',f'sun-{j}')
            self.relate('connect',f'ray-{j}',f'sun-{(j-1)%8}')
        self.add_dot('spot',(20,28))
