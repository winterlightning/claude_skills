"""Chef Hat and Mustache."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61b954c0-9ee8-4b2b-b3e2-f4636524a669'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear hat moustache_61b954c0-9ee8-4b2b-b3e2-f4636524a669.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chef-hat-with-mustache'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'hat', 'mustache', 'cook', 'toque', 'kitchen', 'portrait')

    def build(self):
        # Plan: Three-lobed chef hat over symmetric curled mustache. Lucide chef-hat and human_ref/user.svg inspected; no head or torso, head gap inapplicable. Pleats omitted and mustache reduced to stroke. Envelope (6,6)-(42,42).
        self.add_bezier('crown',(12,18),((8,18),(6,16),(6,13)),((6,9),(11,6),(16,10)),((18,6),(20,6),(24,6)),((28,6),(30,6),(32,10)),((37,6),(42,9),(42,13)),((42,16),(40,18),(36,18)))
        self.add_polyline('band',(36,18),(36,26),(12,26),(12,18))
        self.add_line('seam',(12,18),(36,18))
        for a,b in (('crown','band'),('crown','seam'),('band','seam')):self.relate('connect',a,b)
        self.add_bezier('mustache',(8,36),((8,40),(12,42),(16,42)),((20,42),(22,36),(24,36)),((26,36),(28,42),(32,42)),((36,42),(40,40),(40,36)))
