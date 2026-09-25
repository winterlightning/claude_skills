"""Segmented Open Parachute
Plan: Domed canopy with three panels and four converging suspension lines.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1e40b60-693e-4ff7-9900-031831cda47e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parachute_c1e40b60-693e-4ff7-9900-031831cda47e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-open-parachute'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('parachute', 'canopy', 'lines', 'air', 'flying', 'descent')

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
        path('canopy',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(30,24),(38,21),(34,21)),('C',(18,24),(26,21),(22,21)),('C',(6,24),(14,21),(10,21))],True)
        for x in (18,30):
         name=f'panel-{x}';path(name,(24,6),[('C',(x,24),(x,7),(x,16))]);self.relate('connect','canopy',name)
        for x in (6,18,30,42):
         name=f'line-{x}';self.add_line(name,(x,24),(24,42));self.relate('connect','canopy',name)
        for a in (6,18,30,42):
         for b in (6,18,30,42):
          if a<b:self.relate('connect',f'line-{a}',f'line-{b}')
        self.relate('connect','panel-18','panel-30')
