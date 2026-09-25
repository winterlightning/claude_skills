"""Moved the handle dome and base inward; preserved the tapered bag and split the handle at its true attachment.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: shopping-bag: coherent handle and rounded lower corners.
"""
# Independent repair of shopping-bag-with-loop-handle; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e058f399-32d7-55f0-a75e-23168e8b2b79'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/bag handle_e058f399-32d7-55f0-a75e-23168e8b2b79.svg'
AUTHOR = 'gpt-6'

class ShoppingBagWithLoopHandle(Solo48):
    icon_id = 'shopping-bag-with-loop-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('bag', 'shopping bag', 'paper bag', 'carrier', 'handle', 'retail', 'shopping', 'gift bag')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self):
        # Plan: Preserve the tapered shopping bag using coherent curved sides tangent to the rounded base; the dome handle ends exactly at the rim.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('body',(12,16), [('L',(14,16)),('L',(34,16)),('L',(36,16)),('C',(40,40),(36,24),(40,32)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('C',(12,16),(8,32),(12,24))],True)
        path('handle',(14,16), [('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16))]);join('body','handle')
