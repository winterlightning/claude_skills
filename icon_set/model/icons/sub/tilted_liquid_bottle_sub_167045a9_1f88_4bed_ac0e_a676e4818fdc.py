"""Tilted Bottle with Liquid Drop: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '167045a9-1f88-4bed-ac0e-a676e4818fdc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/bottle drop_167045a9-1f88-4bed-ac0e-a676e4818fdc.svg'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'tilted-liquid-bottle-sub'
    variant_of = 'tilted-bottle-and-drop-sub'
    variant_label = 'Complete liquid boundary restored'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):

        # Complete pouring scene: tilted open bottle, wavy liquid boundary, drop.
        # No useful Lucide match for the liquid contour; retain source asymmetry.
        self.add_bezier('upper-neck',(9,15),((12,13),(8,11),(12,8)))
        self.add_line('upper-side',(12,8),(21,2))
        self.add_bezier('base-round',(21,2),((24,2),(26,4),(28,7)),((30,10),(30,10),(30,12)),((30,13),(29,14),(28,15)))
        self.add_line('lower-side',(28,15),(18,22))
        self.add_bezier('lower-neck',(18,22),((17,22),(16,20),(15,21)))
        self.add_contour('bottle','upper-neck','upper-side','base-round','lower-side','lower-neck')
        self.add_bezier('liquid',(12,8),((24,6),(16,15),(28,15)))
        self.relate('connect','liquid','upper-neck','upper-side')
        self.relate('connect','liquid','lower-side')
        self.add_bezier('drop-left',(6,22),((4,24),(2,26),(2,28)),((2,30),(4,30),(6,30)))
        self.add_bezier('drop-right',(6,30),((8,30),(10,30),(10,28)),((10,26),(8,24),(6,22)))
        self.add_contour('drop','drop-left','drop-right',closed=True)

