"""defense-shield-ability: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80420655-2d61-4bd8-9f65-b4a7eb6ab310'
SOURCE_PATH = 'pictographic-primitives/video-games/defense shield ability_80420655-2d61-4bd8-9f65-b4a7eb6ab310.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DefenseShieldAbility(Solo48):
    icon_id = 'defense-shield-ability'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('defense', 'shield', 'ability', 'video-games')

    def build(self):
        # Plan: VRECT_L; mirrored shield shoulders, tangent vertical walls and curved base.
        # Reference: Lucide shield: symmetric protective silhouette.
        self.add_bezier('upper-left',(24,4),((19,7),(14,9),(8,10)))
        self.add_line('left-wall',(8,10),(8,20))
        self.add_bezier('left-base',(8,20),((8,31),(15,40),(24,44)))
        self.add_bezier('right-base',(24,44),((33,40),(40,31),(40,20)))
        self.add_line('right-wall',(40,20),(40,10))
        self.add_bezier('upper-right',(40,10),((34,9),(29,7),(24,4)))
        self.add_contour('outline','upper-left','left-wall','left-base','right-base','right-wall','upper-right',closed=True)
