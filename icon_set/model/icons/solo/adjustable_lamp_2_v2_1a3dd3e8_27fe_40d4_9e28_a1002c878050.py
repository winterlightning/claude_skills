"""adjustable-lamp-2: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a3dd3e8-27fe-40d4-9e28-a1002c878050'
SOURCE_PATH = 'icons-json/_uncategorized_01/adjustable lamp 2_1a3dd3e8-27fe-40d4-9e28-a1002c878050.json'
AUTHOR = 'gpt-6'

class AdjustableLamp2Variant2(Solo48):
    icon_id = 'adjustable-lamp-2-v2'
    variant_of = 'adjustable-lamp-2'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('adjustable', 'lamp', '_uncategorized_01', 'solo-ai-first50')

    def build(self):
        # Plan: Symmetric shade and upright base beneath a smooth semicircular upper arc. Removed the tiny conversion kink at the shade.
        # Reference: Lucide original/lamp.svg and atomic-debug/lamp.svg.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
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
        path('upper',(8,20), [('A',(40,20),16,16,True)])
        poly('shade',(19,20),(29,20),(33,33),(24,33),(15,33),closed=True)
        line('stand',(24,33),(24,44))
        poly('base',(17,44),(24,44),(31,44))
        join('stand','shade');join('stand','base')

