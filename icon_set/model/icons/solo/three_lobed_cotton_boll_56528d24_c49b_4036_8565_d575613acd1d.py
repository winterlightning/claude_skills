"""Three Lobed Cotton Boll
Plan: Three rounded cotton lobes with a branching stem
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; repeated lobes.
Reduction: Remove small boll divisions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56528d24-c49b-4036-8565-d575613acd1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cotton_56528d24-c49b-4036-8565-d575613acd1d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-lobed-cotton-boll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cotton', 'boll', 'stem', 'plant', 'fiber', 'crop', 'agriculture')

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
        path('boll',(16,32),[('C',(8,22),(10,32),(8,28)),('C',(16,12),(8,16),(10,12)),('A',(32,12),8,8,True),('C',(40,22),(38,12),(40,16)),('C',(32,32),(40,28),(38,32))])
        path('stem',(16,32),[('L',(24,38)),('L',(32,32))]);self.add_line('trunk',(24,38),(24,44));self.relate('connect','stem','boll');self.relate('connect','stem','trunk')
