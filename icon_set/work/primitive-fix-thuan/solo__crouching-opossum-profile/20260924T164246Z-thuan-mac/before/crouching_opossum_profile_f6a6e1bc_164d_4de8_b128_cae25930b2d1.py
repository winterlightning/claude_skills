"""Crouching Opossum Profile
Plan: Crouching opossum with pointed muzzle, round ear, hunched back and long tail.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Eye and crowded forepaw details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6a6e1bc-164d-4de8-b128-cae25930b2d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/opossum_f6a6e1bc-164d-4de8-b128-cae25930b2d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crouching-opossum-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('opossum', 'animal', 'mammal', 'tail', 'wildlife', 'marsupial')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('opossum',(4,23),[('L',(17,12)),('A',(25,12),4,4,True),('L',(31,12)),('C',(44,26),(39,12),(44,18)),('C',(31,40),(44,36),(40,40)),('L',(18,40))])
        path('lower',(4,23),[('L',(16,25)),('L',(22,32)),('L',(17,32))])
        path('haunch',(34,23),[('C',(31,40),(23,26),(26,34))]);self.relate('connect','opossum','lower');self.relate('connect','opossum','haunch')
