"""Widen both rectangular straps equally from 16 to 24 units, keeping the dial centered. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__analogue-wristwatch/20260926T064521Z-thuan-mac/reference/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'claude-opus-5-5'

class AnalogueWristwatch(Solo48):
    icon_id = 'analogue-wristwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self) -> None:
        """Revision per review: the dial is a circle (r13 about (21, 24), was an oval) and each
        strap is open: a horizontal divider line resting on the dial (tangent at its top or
        bottom point, split there) with two parallel sides x 13 and 29 running from the divider
        out to the canvas edge, with no closing end. Hands at 3 o'clock stay 9 inside the dial;
        a crown runs from the dial's right (34, 24) to (40, 24), so the dial sits left of centre."""
        cx, cy, r = 21, 24, 13
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ('dial-nw', 'dial-ne', 'dial-se', 'dial-sw')
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour('dial', *names, closed=True)
        for name, y, edge in (('upper', cy - r, 4), ('lower', cy + r, 44)):
            self.add_polyline(f'{name}-strap', (cx - 8, edge), (cx - 8, y), (cx, y), (cx + 8, y), (cx + 8, edge))
            self.relate('connect', f'{name}-strap', 'dial')
        self.add_polyline('hands', (cx, cy - 4), (cx, cy), (cx + 4, cy))
        self.add_line('crown', (cx + r, cy), (40, cy))
        self.relate('connect', 'crown', 'dial')
