'soccer-ball-with-polygon-panels. Plan: Circular envelope containing pentagon and five radial panel seams. Keyshape: CIRCLE, exact SOLO48 bounds. Construction: No useful exact Lucide match; geometric panel junctions. Reduction: Reduce peripheral tessellation to five broad panels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9712b15-7e45-436f-be7e-f7e183485e03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/soccer_e9712b15-7e45-436f-be7e-f7e183485e03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soccer-ball-with-polygon-panels'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('soccer', 'football', 'ball', 'pentagon', 'panel', 'sport')

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
        circle('ball',24,24,20)
        points=[(24,13),(34,20),(30,32),(18,32),(14,20)]
        self.add_polyline('panel',*points,closed=True)
        for j,(p,q) in enumerate(zip(points,[(24,4),(44,24),(36,40),(12,40),(4,24)])):
         self.add_line(f'seam-{j}',p,q);self.relate('connect','panel',f'seam-{j}');self.relate('connect','ball',f'seam-{j}')
