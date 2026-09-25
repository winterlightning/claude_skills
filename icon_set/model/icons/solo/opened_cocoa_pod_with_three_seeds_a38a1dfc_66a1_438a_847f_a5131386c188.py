'opened-cocoa-pod-with-three-seeds. Plan: Pointed cocoa husk surrounding a vertical seed series. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: No useful Lucide match; mirrored pod silhouette. Reduction: Removed nested shell and stem detail; three seed circles reduced to dots inside the pointed pod.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a38a1dfc-66a1-438a-847f-a5131386c188'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/cocoa_a38a1dfc-66a1-438a-847f-a5131386c188.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'opened-cocoa-pod-with-three-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cocoa', 'cacao', 'pod', 'seeds', 'fruit', 'husk', 'food')

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
        path('pod',(24,4),[('C',(40,24),(32,10),(40,16)),('C',(24,44),(40,32),(32,40)),('C',(8,24),(16,40),(8,32)),('C',(24,4),(8,16),(16,10))],True)
        for y in (16,24,32):self.add_dot(f'seed-{y}',(24,y))
