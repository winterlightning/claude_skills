"""Peace hand with diverging raised fingers, folded thumb and open wrist. VRECT_XL centerlines 8,4–40,44. Lucide hand-metal informs rounded finger caps; V distinguishes peace from horns; omit tiny palm marks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f2b86052-f36b-478c-97db-5c1032939b7f'
SOURCE_PATH = 'pictographic-primitives/social/mood peace_f2b86052-f36b-478c-97db-5c1032939b7f.svg'
AUTHOR = 'gpt-6'

class PeaceSignHand(Solo48):
    icon_id = 'peace-sign-hand'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('hand', 'peace', 'victory', 'finger', 'gesture', 'palm')

    def build(self):
        self.add_line('wrist-left',(16,44),(16,40))
        self.add_arc('palm-left',(16,40),(8,32),radius_x=8)
        self.add_line('palm-side',(8,32),(8,26))
        self.add_line('thumb-top',(8,26),(12,26))
        self.add_line('index-outer',(12,26),(8,8))
        self.add_arc('index-tip',(8,8),(16,8),radius_x=4)
        self.add_line('index-inner',(16,8),(24,26))
        self.add_line('middle-inner',(24,26),(32,8))
        self.add_arc('middle-tip',(32,8),(40,8),radius_x=4)
        self.add_line('middle-outer',(40,8),(36,26))
        self.add_arc('folded-fingers',(36,26),(40,30),radius_x=4)
        self.add_line('palm-right',(40,30),(40,34))
        self.add_arc('palm-right-round',(40,34),(32,42),radius_x=8)
        self.add_line('wrist-right',(32,42),(32,44))
        self.add_contour('outline','wrist-left','palm-left','palm-side','thumb-top','index-outer','index-tip','index-inner','middle-inner','middle-tip','middle-outer','folded-fingers','palm-right','palm-right-round','wrist-right')
        self.add_line('thumb',(12,26),(25,26))
        self.add_arc('thumb-hook',(25,26),(25,34),radius_x=4)
        self.add_contour('thumb-fold','thumb','thumb-hook')
        self.relate('connect','outline','thumb-fold')
