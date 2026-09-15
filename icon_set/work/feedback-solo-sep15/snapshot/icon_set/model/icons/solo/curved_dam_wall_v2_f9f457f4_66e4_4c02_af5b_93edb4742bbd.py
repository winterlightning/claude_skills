"""Straight-bottom dam alternative: replace the curved lower edge with a flat base. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9f457f4-66e4-4c02-af5b-93edb4742bbd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'
AUTHOR = 'gpt-6'

class CurvedDamWallVariant2(Solo48):
    icon_id = 'curved-dam-wall-v2'
    variant_of = 'curved-dam-wall'
    variant_label = 'Wave-bottom dam alternative: add three equal wave sections along the base.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'wall', 'water', 'reservoir', 'barrier', 'spillway', 'infrastructure', 'river')

    def build(self):
        """Symbol plan: Straight-bottom dam alternative: replace the curved lower edge with a flat base. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_line('wall-1', (4, 40), (4, 8))
        self.add_line('wall-2', (4, 8), (14, 8))
        self.add_line('wall-3', (14, 8), (14, 16))
        self.add_line('wall-4', (14, 16), (34, 16))
        self.add_line('wall-5', (34, 16), (34, 8))
        self.add_line('wall-6', (34, 8), (44, 8))
        self.add_line('wall-7', (44, 8), (44, 40))
        self.add_line('water', (44, 40), (4, 40))
        self.add_contour('outline', 'wall-1', 'wall-2', 'wall-3', 'wall-4', 'wall-5', 'wall-6', 'wall-7', 'water', closed=True)
        self.add_line('flow-left', (18, 25), (16, 31))
        self.add_line('flow-right', (32, 25), (30, 31))
