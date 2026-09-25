"""Cow Face with Curved Horns and Broad Muzzle
Plan: Broad cow head, paired horns and wide muzzle
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful Lucide match; mirrored face construction.
Reduction: Remove tiny nostrils and eyes to emphasize horns and muzzle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ff5bf8d-72f8-4493-852c-e8fd0c4071c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mambo_8ff5bf8d-72f8-4493-852c-e8fd0c4071c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cow-face-with-curved-horns-and-broad-muzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cow', 'cattle', 'head', 'horns', 'muzzle', 'animal', 'farm')

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
        path('head',(14,30),[('L',(12,20)),('C',(24,14),(12,14),(18,14)),('C',(36,20),(30,14),(36,14)),('L',(34,30))])
        rect('muzzle',10,30,28,12,6);self.relate('connect','head','muzzle')
        for name,a,b,c in [('left',(12,20),(6,14),(6,6)),('right',(36,20),(42,14),(42,6))]:
            path(name,a,[('C',b,(b[0],20),b),('C',c,b,(c[0],10))]);self.relate('connect',name,'head')
