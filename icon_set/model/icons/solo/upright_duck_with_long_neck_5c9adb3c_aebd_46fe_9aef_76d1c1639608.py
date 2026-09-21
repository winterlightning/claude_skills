"""Upright Duck with Long Neck
Plan: Left-facing upright duck with vertical neck, broad low body and two feet.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: coherent neck/breast silhouette.
Reduction: Small eye and wing line omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c9adb3c-aebd-46fe-9aef-76d1c1639608'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bog_5c9adb3c-aebd-46fe-9aef-76d1c1639608.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-duck-with-long-neck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('duck', 'bird', 'waterfowl', 'standing', 'wing', 'beak', 'animal')

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
        path('duck',(6,14),[('L',(12,14)),('A',(24,14),6,8,True),('L',(24,26)),('L',(42,26)),('C',(32,36),(42,34),(38,36)),('L',(22,36)),('C',(12,29),(15,36),(12,34)),('L',(15,21)),('C',(12,14),(12,20),(10,17))]);
        for x in (22,32):self.add_line(f'leg-{x}',(x,36),(x,42));self.relate('connect',f'leg-{x}','duck')
