"""Happy person bust with circular head, raised shoulders, and enclosing circle."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "a8d49b9d-bc09-4bb6-a4b0-570e012f07c0"
SOURCE_PATH = "pictographic-primitives/other/person_a8d49b9d-bc09-4bb6-a4b0-570e012f07c0.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'detached head', 'curved smile shoulders', 'torso')
REPAIR_PLAN = {'concept': 'Happy Person in a Circle', 'core_parts': ('enclosing circle', 'detached head', 'curved smile shoulders', 'torso'), 'flexible_parts': 'head and shoulder proportions', 'ladder': 'Reduced the head and centered the body at the exact 4px human gap'}



class DrawingVariant2(Sub32):
    icon_id = "happy-person-in-a-circle-v2"
    variant_label = 'Reduced the head and centered the body at the exact 4px human gap'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("state", "other", "primitives-generate")
    aliases = ("happy-user-circle",)
    keywords = ("person", "user", "happy", "circle")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        circle(self, "head", 16, 11, 2)
        self.add_line("shoulders", (10, 21), (22, 21))
        self.add_line("torso", (16, 21), (16, 23))
        self.relate("connect", "shoulders", "torso")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
