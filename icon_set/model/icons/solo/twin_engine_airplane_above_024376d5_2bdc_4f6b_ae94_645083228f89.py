'twin-engine-airplane-above. Plan: Central fuselage, broad swept wings and two engine pods. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide plane: continuous wing/fuselage outline. Reduction: Reduced engine pods to two attached strokes and simplified the divided tail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '024376d5-2bdc-4f6b-ae94-645083228f89'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plane engines_024376d5-2bdc-4f6b-ae94-645083228f89.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-engine-airplane-above'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('airplane', 'engines', 'wings', 'aviation', 'aircraft', 'travel')

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
        path('plane',(20,18),[('L',(20,10)),('A',(28,10),4,4,True),('L',(28,18)),('L',(42,26)),('L',(42,30)),('L',(38,32)),('L',(28,30)),('L',(28,36)),('L',(34,42)),('L',(24,40)),('L',(14,42)),('L',(20,36)),('L',(20,30)),('L',(10,32)),('L',(6,30)),('L',(6,26)),('L',(20,18))],True)
        for x in (10,38):
         self.add_line(f'engine-{x}',(x,32),(x,38));self.relate('connect','plane',f'engine-{x}')
