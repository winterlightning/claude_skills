# Variant of fresh-carrot-batch-011-12-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of fresh-carrot-batch-011-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6175b21e-96a2-4503-a4cc-6b0bc36376c0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fresh-carrot-batch-011-12',)
SOLO_SOURCE_ICON_IDS = ('fresh-carrot-batch-011-12',)
REFERENCE_EXPORT_SHA256 = '2c67db710f6202338a4b821064cf730bdb737e4968f7733871534d4273898c79'

class DrawingVariant3(Sub32):
    icon_id = 'fresh-carrot-batch-011-12-sub32-v3'
    variant_of = 'fresh-carrot-batch-011-12-sub32-v2'
    variant_label = 'Restore omitted source details'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two leaves, a tapered root, and two short surface marks.
        self.add_bezier('leaf-left-out',(16,12),((6,12),(6,8),(6,2)))
        self.add_bezier('leaf-left-in',(6,2),((12,2),(16,6),(16,12)))
        self.add_contour('leaf-left','leaf-left-out','leaf-left-in',closed=True)
        self.add_bezier('leaf-right-out',(16,12),((26,12),(26,8),(26,2)))
        self.add_bezier('leaf-right-in',(26,2),((20,2),(16,6),(16,12)))
        self.add_contour('leaf-right','leaf-right-out','leaf-right-in',closed=True)
        self.relate('connect','leaf-left','leaf-right')
        self.add_bezier('root-top-right',(16,12),((22,12),(24,14),(24,18)))
        self.add_line('root-bottom-right',(24,18),(16,30))
        self.add_line('root-bottom-left',(16,30),(8,18))
        self.add_bezier('root-top-left',(8,18),((8,14),(10,12),(16,12)))
        self.add_contour('root','root-top-right','root-bottom-right','root-bottom-left','root-top-left',closed=True)
        self.relate('connect','root','leaf-left');self.relate('connect','root','leaf-right')
        self.add_line('mark-top',(8,18),(12,18));self.relate('connect','mark-top','root')
        self.add_line('mark-low',(22,21),(19,21));self.relate('connect','mark-low','root')
