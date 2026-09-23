"""Happy person bust with circular head, raised shoulders, and enclosing circle."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import circle
SOURCE_ICON_ID = 'a8d49b9d-bc09-4bb6-a4b0-570e012f07c0'
SOURCE_PATH = 'pictographic-primitives/other/person_a8d49b9d-bc09-4bb6-a4b0-570e012f07c0.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'detached head', 'curved smile shoulders', 'torso')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'happy-person-in-a-circle-v2'
    variant_of = 'happy-person-in-a-circle'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/person'
    aliases = ('happy-user-circle',)
    keywords = ('person', 'user', 'happy', 'circle')

    def build(self):
        circle(self, 'frame', 30, 30, 28)
        circle(self, 'head', 30, 20, 9)
        self.add_bezier('shoulder-left', (14, 34), ((18, 37), (24, 37), (30, 37)))
        self.add_bezier('shoulder-right', (30, 37), ((36, 37), (42, 37), (46, 34)))
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.add_line('torso', (30, 37), (30, 50))
        self.relate('connect', 'shoulders', 'torso')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
