"""A circular magnifying glass with a minus and a straight handle. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd05e7aa2-4c1e-43d5-8943-5f63cebcd390'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.svg'
AUTHOR = 'gpt-6'

class ZoomOut(Solo48):
    icon_id = 'zoom-out'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'out', 'interface-essential')

    def build(self) -> None:
        # Circular lens, centered minus, and one uninterrupted handle.
        # Lucide zoom-out informs its circle/line construction.
        # SQUARE centerline extremes: (6, 6)-(42, 42).
        center, radius = 21, 15
        left, right = (center - radius, center), (center + radius, center)
        attachment = (center + 12, center + 9)  # exact 9-12-15 circle point
        self.add_arc('lens-top', left, right, radius_x=radius)
        self.add_arc('lens-join', right, attachment, radius_x=radius)
        self.add_arc('lens-bottom', attachment, left, radius_x=radius)
        self.add_contour('lens', 'lens-top', 'lens-join', 'lens-bottom', closed=True)
        self.add_line('minus', (center - 6, center), (center + 6, center))
        self.add_line('handle', attachment, (42, 42))
        self.relate('connect', 'lens', 'handle')

# Visually reviewed equivalent content reference, explicitly requested for reuse.
SOURCE_REFERENCES = tuple(globals().get("SOURCE_REFERENCES", ())) + (('94d79c2a-5cc5-4d30-a216-d020b553a665', 'icon_set/dist/gallery/combination-originals/94d79c2a-5cc5-4d30-a216-d020b553a665.svg'),)
