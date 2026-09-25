"""Wrist Wearing Smart Band.

Plan: One forearm and closed hand; a broad vertical tracker joins both wrist edges. Thumb is a single smooth lobe. Bounds (4,8)-(44,40).
Construction references: human_ref/full_body_ref.png limb vocabulary; Lucide hand-fist and watch for rounded hand and band.
Simplification: Tiny face slash and individual finger seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2125ec54-c0c7-4602-bab6-2abca03de2b6'
SOURCE_PATH = 'pictographic-primitives/combination/technology device smart band_2125ec54-c0c7-4602-bab6-2abca03de2b6.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


class WristWearingSmartBand(Solo48):
    icon_id = 'wrist-wearing-smart-band'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'combination'
    categories = ('combination', 'primitives')
    aliases = ()
    keywords = ('wrist', 'wearing', 'smart', 'band')

    def build(self):
        self.add_line('arm-top',(4,12),(12,12))
        self.add_line('arm-bottom',(4,32),(12,32))
        path(self, 'tracker', (12,12), ('A',(16,8),4,4,True), ('L',(20,8)), ('A',(24,12),4,4,True), ('L',(24,32)), ('A',(20,36),4,4,True), ('L',(16,36)), ('A',(12,32),4,4,True), ('L',(12,12)),closed=True)
        path(self, 'hand', (24,12), ('L',(38,12)), ('A',(44,18),6,6,True), ('L',(44,30)), ('A',(40,34),4,4,True), ('L',(34,34)))
        path(self, 'thumb', (24,32), ('B',(34,40),(26,32),(27,40)), ('B',(40,34),(38,40),(40,38)))
        self.relate('connect','arm-top','tracker')
        self.relate('connect','arm-bottom','tracker')
        self.relate('connect','tracker','hand')
        self.relate('connect','tracker','thumb')
        self.relate('connect','hand','thumb')
