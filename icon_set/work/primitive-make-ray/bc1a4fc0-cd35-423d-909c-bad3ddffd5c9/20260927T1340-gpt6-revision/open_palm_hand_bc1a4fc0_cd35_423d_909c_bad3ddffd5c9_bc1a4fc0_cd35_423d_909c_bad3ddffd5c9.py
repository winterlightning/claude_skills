"""Open Palm Hand.

Plan: Four round fingertips, shared finger radius4 and step8; left thumb and rounded palm. Bounds (4,8)-(44,40).
Construction: Lucide hand original and atomic-debug: rounded tips, continuous palm and separate finger creases. Human-reference simple rounded limb vocabulary.
Reduction: Shortened finger creases and widened fingers to the SOLO48 spacing budget. Identical reference subjects use the same construction under separate source UUIDs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bc1a4fc0-cd35-423d-909c-bad3ddffd5c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9/20260927T133654Z-thuan-mac-1/reference/hand_bc1a4fc0-cd35-423d-909c-bad3ddffd5c9.svg'
AUTHOR = "gpt-6"


class IconOpenPalmHand(Solo48):
    icon_id = 'open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("holidays", "other", "primitives-generate")
    aliases = ()
    keywords = ('open', 'palm', 'hand')

    def build(self):
        # A taller palm and sculpted side thumb replace the squat mitten.
        self.add_line('index-left',(16,28),(16,10))
        self.add_arc('index-tip',(16,10),(24,10),radius_x=4,radius_y=6)
        self.add_line('index-middle-valley',(24,10),(24,8))
        self.add_arc('middle-tip',(24,8),(32,8),radius_x=4)
        self.add_line('middle-ring-valley',(32,8),(32,12))
        self.add_arc('ring-tip',(32,12),(40,12),radius_x=4)
        self.add_line('ring-right',(40,12),(40,30))
        self.add_bezier('palm-right',(40,30),((40,38),(35,44),(28,44)))
        self.add_line('palm-bottom',(28,44),(22,44))
        self.add_bezier('thumb-outside',(22,44),((14,42),(8,36),(8,30)))
        self.add_bezier('thumb',(8,30),((8,23),(12,21),(16,28)))
        self.add_contour('outline','index-left','index-tip','index-middle-valley',
                         'middle-tip','middle-ring-valley','ring-tip','ring-right',
                         'palm-right','palm-bottom','thumb-outside','thumb',
                         closed=True)
