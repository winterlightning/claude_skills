"""Large Four-Point Sparkle with Smaller Companion
Plan: Large concave four-point sparkle with small upper-right companion.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f71e0e6f-51ea-4b94-a470-cc24ee588d43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/sparkle_f71e0e6f-51ea-4b94-a470-cc24ee588d43.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'large-four-point-sparkle-with-smaller-companion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sparkle', 'stars', 'shine', 'twinkle', 'points', 'light')

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
        path('sparkle',(6,30),[('C',(18,18),(14,30),(18,26)),('C',(30,30),(18,26),(22,30)),('C',(18,42),(22,30),(18,34)),('C',(6,30),(18,34),(14,30))],True)
        path('small',(34,6),[('C',(42,14),(37,10),(38,11)),('C',(34,22),(38,17),(37,18)),('C',(26,14),(31,18),(30,17)),('C',(34,6),(30,11),(31,10))],True)
