"""Pointed Ear Collie Face
Plan: Mirrored pointed ears and elongated canine muzzle with eyes and nose.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide dog: spare face marks within broad silhouette.
Reduction: Dropped cheek patches and inner ear lines; retained collie-like pointed ears and long muzzle.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4731ca55-af71-4c3b-9bfa-b1c641a0b9a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/border collie_4731ca55-af71-4c3b-9bfa-b1c641a0b9a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-ear-collie-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dog', 'collie', 'face', 'ears', 'canine', 'pet', 'muzzle')

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
        path('head',(8,4),[('L',(19,14)),('L',(29,14)),('L',(40,4)),('L',(40,19)),('C',(34,44),(40,26),(34,32)),('L',(14,44)),('C',(8,19),(14,32),(8,26)),('L',(8,4))],True)
        for name,x in [('left-eye',18),('right-eye',30)]:self.add_dot(name,(x,24))
        self.add_line('nose',(24,33),(24,35))
