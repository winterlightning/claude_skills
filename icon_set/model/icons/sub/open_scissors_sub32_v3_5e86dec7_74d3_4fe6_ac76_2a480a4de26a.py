# Variant of open-scissors-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of open-scissors.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e86dec7-74d3-4fe6-ac76-2a480a4de26a'
SOURCE_PATH = 'pictographic-primitives/tools/scissors_5e86dec7-74d3-4fe6-ac76-2a480a4de26a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e86dec7-74d3-4fe6-ac76-2a480a4de26a', 'pictographic-primitives/tools/scissors_5e86dec7-74d3-4fe6-ac76-2a480a4de26a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/open-scissors',)
SOLO_SOURCE_ICON_IDS = ('open-scissors',)
REFERENCE_EXPORT_SHA256 = 'fb3b9dee71b9ea3e73d7bb8e8fff14bd73408fbe4bd42eb5bb47b8fe6dfa63aa'

class DrawingVariant3(Sub32):
    icon_id = 'open-scissors-sub32-v3'
    variant_of = 'open-scissors-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/tools'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Scissors with recognizable tapered blades, circular finger loops, and a shared central pivot.
        self.add_arc('left-loop-upper',(2,25),(12,25),radius_x=5,radius_y=5,sweep=True)
        self.add_arc('left-loop-lower',(12,25),(2,25),radius_x=5,radius_y=5,sweep=True)
        self.add_contour('left-loop','left-loop-upper','left-loop-lower',closed=True)
        self.add_arc('right-loop-upper',(20,25),(30,25),radius_x=5,radius_y=5,sweep=True)
        self.add_arc('right-loop-lower',(30,25),(20,25),radius_x=5,radius_y=5,sweep=True)
        self.add_contour('right-loop','right-loop-upper','right-loop-lower',closed=True)
        self.add_polyline('left-blade',(26,2),(16,14),(10,21))
        self.add_polyline('right-blade',(6,2),(16,14),(22,21))
        self.relate('connect','left-blade','right-blade');self.relate('connect','left-blade','left-loop');self.relate('connect','right-blade','right-loop')
