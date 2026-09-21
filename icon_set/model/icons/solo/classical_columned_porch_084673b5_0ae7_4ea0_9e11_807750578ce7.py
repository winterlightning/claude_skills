'classical-columned-porch. Plan: Symmetric triangular roof above two columns and baseline. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide landmark: repeated column spacing. Reduction: Reduce layered platform and entablature to single structural strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '084673b5-0ae7-4ea0-9e11-807750578ce7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/porch_084673b5-0ae7-4ea0-9e11-807750578ce7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'classical-columned-porch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('porch', 'columns', 'roof', 'classical', 'building', 'entrance')

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
        self.add_polyline('roof',(4,20),(24,8),(44,20),(4,20),closed=True)
        for x in (12,36):
         self.add_line(f'column-{x}',(x,20),(x,40));self.relate('connect','roof',f'column-{x}')
        self.add_line('base',(4,40),(44,40))
        for x in (12,36):self.relate('connect','base',f'column-{x}')
