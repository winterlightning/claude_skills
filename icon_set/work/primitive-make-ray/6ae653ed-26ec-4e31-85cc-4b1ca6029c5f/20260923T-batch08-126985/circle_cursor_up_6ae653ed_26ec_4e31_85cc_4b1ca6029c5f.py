"""circle cursor up. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide circle-arrow-down, round joins and coherent symbol contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6ae653ed-26ec-4e31-85cc-4b1ca6029c5f'
SOURCE_PATH = 'icon_set/work/todo-references/circle cursor up_6ae653ed-26ec-4e31-85cc-4b1ca6029c5f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-cursor-up'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'cursor', 'up')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # Shared dart polygon rotated about the enclosure centre on the integer grid.
        points = [(15,17),(24,22),(33,17),(24,35)]
        for _ in range(2):
            points = [(48-y,x) for x,y in points]
        self.add_polyline('cursor',*points,closed=True)

