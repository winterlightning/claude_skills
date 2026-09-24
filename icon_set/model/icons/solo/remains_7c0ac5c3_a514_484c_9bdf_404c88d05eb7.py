"""A bone beside a leaf.
Plan: HRECT_M keeps the two subjects side by side with legal clearance. Visible ink bounds: (2, 8, 46, 40).
Reduction: Bone made upright and its shaft widened; no subject omitted. Leaf and stem retained.
Construction: Lucide bone: paired end lobes around a straight shaft; leaf: a coherent pointed outline and stem."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c0ac5c3-a514-484c-9bdf-404c88d05eb7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/remains_7c0ac5c3-a514-484c-9bdf-404c88d05eb7.svg'
AUTHOR = 'gpt-6'
PLAN = 'A bone beside a leaf.'
OMISSIONS = 'Bone made upright and its shaft widened; no subject omitted. Leaf and stem retained.'
CONSTRUCTION_REFERENCES = 'Lucide bone: paired end lobes around a straight shaft; leaf: a coherent pointed outline and stem.'
KEYSHAPE_INK_BOUNDS = (2, 8, 46, 40)

class Drawing(Solo48):
    icon_id = 'remains'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('remains',)

    def build(self):
        self.add_line('shaft-left', (8, 18), (8, 30))
        arcs = [('bottom-left', (8, 30), (8, 38)), ('bottom-left-notch', (8, 38), (12, 34)), ('bottom-right-notch', (12, 34), (16, 38)), ('bottom-right', (16, 38), (16, 30))]
        for (name, a, b) in arcs:
            self.add_arc(name, a, b, radius_x=4, sweep=False)
        self.add_line('shaft-right', (16, 30), (16, 18))
        for (name, a, b) in [('top-right', (16, 18), (16, 10)), ('top-right-notch', (16, 10), (12, 14)), ('top-left-notch', (12, 14), (8, 10)), ('top-left', (8, 10), (8, 18))]:
            self.add_arc(name, a, b, radius_x=4, sweep=False)
        self.add_contour('bone', 'shaft-left', *(a[0] for a in arcs), 'shaft-right', 'top-right', 'top-right-notch', 'top-left-notch', 'top-left', closed=True)
        self.add_bezier('leaf', (44, 12), ((44, 24), (43, 31), (36, 33)), ((32, 33), (32, 18), (44, 12)))
        self.add_polyline('vein', (34, 38), (36, 33), (40, 23))
        self.relate('connect', 'leaf', 'vein')
