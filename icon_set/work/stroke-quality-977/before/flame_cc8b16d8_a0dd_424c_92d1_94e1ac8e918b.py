"""flame-fire: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc8b16d8-a0dd-424c-92d1-94e1ac8e918b'
SOURCE_PATH = 'pictographic-primitives/fire/flame_cc8b16d8-a0dd-424c-92d1-94e1ac8e918b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class FlameFire(Solo48):
    icon_id = 'flame-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('flame', 'fire')

    def build(self):
        # VRECT_L (8,4)-(40,44); retain two flame tips, omit the cramped inner flame.
        # Construction reference: Lucide flame: a few flowing curves with intentional pointed tips
        self.add_bezier('left',(24,44),((16,44),(8,38),(8,30)),((8,18),(24,16),(20,4)))
        self.add_bezier('crest',(20,4),((29,10),(32,16),(30,24)))
        self.add_bezier('notch',(30,24),((34,23),(36,20),(36,18)))
        self.add_bezier('right',(36,18),((39,22),(40,26),(40,30)),((40,38),(32,44),(24,44)))
        self.add_contour('outline','left','crest','notch','right',closed=True)
