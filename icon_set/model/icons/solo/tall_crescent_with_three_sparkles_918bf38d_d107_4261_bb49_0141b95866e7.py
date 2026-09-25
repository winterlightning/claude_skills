"""Tall Crescent with Three Sparkles
Plan: Tall crescent and three separated sparkle crosses
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide moon.
Reduction: Sparkles reduced to open crosses; preserve tall layout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '918bf38d-d107-4261-bb49-0141b95866e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy moon_918bf38d-d107-4261-bb49-0141b95866e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-crescent-with-three-sparkles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('moon', 'crescent', 'stars', 'sparkles', 'night', 'sky', 'astronomy')

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
        path('moon',(24,4),[('C',(8,24),(14,4),(8,12)),('C',(24,44),(8,36),(14,44)),('C',(24,4),(13,36),(13,12))],True)
        for i,y in enumerate((8,24,40)):
            self.add_line(f'v{i}',(36,y-4),(36,y+4));self.add_line(f'h{i}',(32,y),(40,y));self.relate('connect',f'v{i}',f'h{i}')
