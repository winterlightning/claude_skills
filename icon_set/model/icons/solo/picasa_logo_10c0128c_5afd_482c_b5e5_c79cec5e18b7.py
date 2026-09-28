"""picasa-logo: Circular shutter — local spacing refinement; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10c0128c-5afd-482c-b5e5-c79cec5e18b7'
SOURCE_PATH = 'pictographic-primitives/logos/picasa logo_10c0128c-5afd-482c-b5e5-c79cec5e18b7.svg'
AUTHOR = 'gpt-6'

class PicasaLogo(Solo48):
    icon_id = 'picasa-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'picasa-logo')

    def build(self):
        # Plan: Kept the original circle and all facet strokes. Moved the lower and right junction inward.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(8,12),20,20,True),('A',(24,4),20,20,True)],True)
        poly('diagonal',(8,12),(24,24),(32,32),(40,36));join('diagonal','rim')
        poly('right',(36,8),(32,32));join('right','rim');join('right','diagonal')
        poly('left',(4,24),(16,24),(24,24));join('left','rim');join('left','diagonal')
        poly('bottom',(12,40),(16,32),(16,24));join('bottom','rim');join('bottom','left')
        line('bar',(16,32),(32,32));join('bar','bottom');join('bar','diagonal');join('bar','right')
