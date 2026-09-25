"""Avalanche Beside a Steep Mountain Slope
Plan: Steep mountain with snow contour, two falling masses and diagonal motion.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94b3e7fa-f694-4a00-98df-de4a2dbb212b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avalanche 1_94b3e7fa-f694-4a00-98df-de4a2dbb212b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'avalanche-beside-a-steep-mountain-slope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('avalanche', 'mountain', 'snow', 'slope', 'falling', 'rocks', 'hazard')

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
        path('mountain',(6,16),[('C',(10,6),(6,10),(8,6)),('L',(28,42))])
        path('snow',(6,32),[('C',(20,26),(12,28),(17,28))]);self.relate('connect','snow','mountain')
        circle('large-snowball',36,25,6);circle('small-snowball',37,8,2)
        self.add_line('motion',(24,8),(27,12))
