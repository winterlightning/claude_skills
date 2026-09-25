"""Paired Three-Stroke Tufts
Plan: Two groups of three grass-like strokes.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Six source strokes retained; spacing enlarged within the horizontal keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aee7722c-dd24-4d55-b610-ee4dcefeb9b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park disneyland_aee7722c-dd24-4d55-b610-ee4dcefeb9b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-three-stroke-tufts'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tufts', 'strokes', 'grass', 'marks', 'pair', 'sprays', 'pattern')

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
        for x in (12,36):
         self.add_line(f'middle-{x}',(x,10),(x,22))
         for s in (-1,1):self.add_line(f'side-{x}-{s}',(x+s*4,30),(x+s*8,38))
