"""A smiling devil face: a round head with two curved horns, dash eyes and a smile.

Plan: SQUARE (6,6)-(42,42). Head: a circle of radius 16 about (24,26) whose lower half is two true quarter arcs and whose upper half is four circle-arc cubics through the horn roots (12,16) and (36,16). Horns: single curved strokes from each root sweeping outward and up to the SQUARE corners (6,6) and (42,6). Eyes: 2-unit vertical dashes at x=20/28, y 21-23. Smile: an r6 arc from (20,32) to (28,32).
Review of the rejected drawing: the head was a box with straight sides and two pointed ears on top, so it read as a cat or fox; the original is a round face with slim curved horns and a smile.
Omissions: none beyond the reduction of the horns to single strokes.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '20533df1-caff-43dd-9667-20cbd37a2bd0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-horned-face/20260928T042731Z-thuan-mac-1/reference/face smile horns_20533df1-caff-43dd-9667-20cbd37a2bd0.svg'
AUTHOR = "claude-fable-5-1"


class SmilingHornedFace(Solo48):
    icon_id = 'smiling-horned-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('devil-face', 'smiling-imp')
    keywords = ('face', 'smile', 'horns', 'devil', 'imp', 'emoji')

    def build(self) -> None:
        cx, cy, r = 24, 26, 16

        def carc(name, p0, p3):
            """Circle-arc cubic about (cx,cy) between two knots, tangents taken from the circle."""
            a0 = math.atan2(p0[1] - cy, p0[0] - cx)
            a1 = math.atan2(p3[1] - cy, p3[0] - cx)
            d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
            k = 4 / 3 * math.tan(abs(d) / 4) * r
            s = 1 if d > 0 else -1
            c1 = (p0[0] - s * k * math.sin(a0), p0[1] + s * k * math.cos(a0))
            c2 = (p3[0] + s * k * math.sin(a1), p3[1] - s * k * math.cos(a1))
            self.add_bezier(name, p0, (c1, c2, p3))

        left, top, right, bottom = (cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)
        root_l, root_r = (12, 16), (36, 16)
        self.add_arc('jaw-left', bottom, left, radius_x=r, sweep=True)
        carc('temple-left', left, root_l)
        carc('crown-left', root_l, top)
        carc('crown-right', top, root_r)
        carc('temple-right', root_r, right)
        self.add_arc('jaw-right', right, bottom, radius_x=r, sweep=True)
        self.add_contour('head', 'jaw-left', 'temple-left', 'crown-left', 'crown-right',
                         'temple-right', 'jaw-right', closed=True)
        self.add_bezier('horn-left', root_l, ((8, 14), (6, 11), (6, 6)))
        self.add_bezier('horn-right', root_r, ((40, 14), (42, 11), (42, 6)))
        self.relate('connect', 'horn-left', 'head')
        self.relate('connect', 'horn-right', 'head')
        self.add_line('eye-left', (20, 21), (20, 23))
        self.add_line('eye-right', (28, 21), (28, 23))
        self.add_arc('smile', (20, 32), (28, 32), radius_x=6, sweep=False)
