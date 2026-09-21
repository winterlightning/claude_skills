"""Rounded Shade Table Lamp
Plan: Domed shade above centered stem and low rounded base.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide lamp: shade, stem and base share central axis.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b722a90c-05e3-4b1d-89b2-b457b197c35e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nightlight_b722a90c-05e3-4b1d-89b2-b457b197c35e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-shade-table-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('lamp', 'table', 'shade', 'light', 'base', 'furniture')

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
        path('shade',(8,26),[('L',(12,12)),('C',(24,4),(14,6),(18,4)),('C',(36,12),(30,4),(34,6)),('L',(40,26)),('L',(8,26))],True)
        self.add_line('stem-left',(20,26),(20,36))
        self.add_line('stem-right',(28,26),(28,36))
        rect('base',12,36,24,8,2)
        for part in ('stem-left','stem-right'):
            self.relate('connect','shade',part);self.relate('connect',part,'base')
