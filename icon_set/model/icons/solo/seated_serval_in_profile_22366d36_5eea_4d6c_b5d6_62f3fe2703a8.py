"""Seated Serval in Profile
Plan: Seated cat profile with pointed ears, bent hind leg and upright curling tail.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Tail simplified to one upright curve; hind leg opened for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22366d36-5eea-4d6c-b5d6-62f3fe2703a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/serval_22366d36-5eea-4d6c-b5d6-62f3fe2703a8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-serval-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('serval', 'cat', 'animal', 'tail', 'seated', 'profile')

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
        path('cat',(10,6),[('L',(17,12)),('L',(24,6)),('L',(24,21)),('C',(32,36),(30,26),(32,31)),('L',(32,42)),('L',(10,42)),('L',(14,36)),('L',(14,25)),('C',(6,17),(8,25),(6,21)),('L',(10,6))],True)
        path('leg',(24,31),[('C',(24,42),(23,35),(23,39))]);self.relate('connect','cat','leg')
        path('tail',(32,42),[('C',(42,32),(40,42),(42,37)),('L',(42,20))]);self.relate('connect','cat','tail')
