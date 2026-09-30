"""Shaped Armor Breastplate
Plan: Symmetric armor outline has a scooped neck, scooped armholes, tapered waist and flared bottom. Paired chest arcs share the center.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful exact Lucide match; coherent garment outline.
Reduction: Omitted narrow lower trim stripe; retained armor torso and paired breast shaping.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8e53793-05b3-42da-a1ec-4dba6c2ce3f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/breastplate_f8e53793-05b3-42da-a1ec-4dba6c2ce3f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shaped-armor-breastplate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('armor', 'breastplate', 'chest', 'protection', 'vest', 'warrior', 'equipment')

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
        path('armor',(8,4),[('L',(18,4)),('A',(30,4),6,6,False),('L',(40,4)),('C',(40,22),(36,10),(36,15)),('L',(35,35)),('L',(40,44)),('L',(8,44)),('L',(13,35)),('L',(8,22)),('C',(8,4),(12,15),(12,10))],True)
        path('chest',(18,24),[('C',(24,21),(19,29),(23,29)),('C',(30,24),(25,29),(29,29))])
