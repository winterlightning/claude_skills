"""Picker take (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4f371c6-c5e7-45dd-8d80-8cefea43094a'
SOURCE_PATH = 'pictographic-primitives/design/picker take_b4f371c6-c5e7-45dd-8d80-8cefea43094a.svg'
AUTHOR = 'gpt-6'

class PickerTakeVariant2(Solo48):
    icon_id = 'picker-take-v2'
    variant_of = 'picker-take'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'take', 'design')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        """Remove the repeated bulb base; the continuous rim owns this shared edge."""
        self._path('bulb', (15, 13), [('A', (33, 13), 9, 9, True)])
        self.add_polyline('rim', (8, 13), (15, 13), (33, 13), (40, 13))
        self.relate('connect', 'rim', 'bulb')
        self.add_polyline('nozzle', (15, 13), (15, 21), (24, 25), (33, 21), (33, 13))
        self.relate('connect', 'nozzle', 'rim')
        self.relate('connect', 'nozzle', 'bulb')
        self._path('drop', (24, 34), [('A', (30, 39), 7, 7, True), ('A', (18, 39), 6, 5, True), ('A', (24, 34), 7, 7, True)], True)
