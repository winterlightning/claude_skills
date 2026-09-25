"""shield-ee28756e: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee28756e-a560-4166-b776-2aebcbfcabaa'
SOURCE_PATH = 'pictographic-primitives/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ShieldEe28756e(Solo48):
    icon_id = 'shield-ee28756e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        # Plan: VRECT_L; smooth crowned top, mirrored lower bowl.
        # Reference: Lucide shield: matched sides and coherent curves.
        self.add_bezier('upper-left',(24,4),((19,4),(14,6),(8,8)))
        self.add_line('left-wall',(8,8),(8,20))
        self.add_bezier('left-base',(8,20),((8,31),(15,40),(24,44)))
        self.add_bezier('right-base',(24,44),((33,40),(40,31),(40,20)))
        self.add_line('right-wall',(40,20),(40,8))
        self.add_bezier('upper-right',(40,8),((34,6),(29,4),(24,4)))
        self.add_contour('outline','upper-left','left-wall','left-base','right-base','right-wall','upper-right',closed=True)
