"""Perfume Bottle with Squeeze Bulb
Plan: Squat atomizer bottle with stepped neck and right-hand squeeze bulb.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bb96c3e-3ae8-4bb5-ab21-636b28bdfaac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/perfume_4bb96c3e-3ae8-4bb5-ab21-636b28bdfaac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'perfume-bottle-squeeze-bulb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('perfume', 'bottle', 'atomizer', 'bulb', 'fragrance', 'container')

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
        rect('bottle',6,22,26,20,4);self.add_polyline('neck',(14,22),(14,14),(24,14),(24,22));self.add_polyline('stopper',(15,14),(15,6),(23,6),(23,14))
        self.relate('connect','bottle','neck');self.relate('connect','neck','stopper')
        self.add_polyline('hose',(23,6),(30,6),(34,10));self.relate('connect','hose','stopper')
        circle('bulb',38,10,4);self.relate('connect','bulb','hose')
