"""Curving Pinworm
Plan: Continuous thick worm ribbon with alternating bends and rounded ends.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12ed033b-94af-439b-9775-23fdba88d590'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pinworm_12ed033b-94af-439b-9775-23fdba88d590.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curving-pinworm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pinworm', 'worm', 'parasite', 'animal', 'curve', 'biology')

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
        path('worm',(10,6),[('C',(18,18),(15,8),(19,12)),('C',(16,29),(17,23),(13,29)),('C',(23,24),(18,29),(20,26)),('C',(34,22),(27,18),(32,20)),('C',(42,32),(40,24),(42,27)),('C',(39,42),(42,37),(39,39)),('L',(31,42)),('C',(34,32),(31,38),(35,35)),('C',(28,32),(33,29),(30,29)),('C',(16,38),(24,36),(21,38)),('C',(6,27),(8,38),(6,33)),('C',(9,18),(6,23),(10,21)),('C',(6,10),(9,15),(6,14)),('A',(10,6),4,4,True)],True)
