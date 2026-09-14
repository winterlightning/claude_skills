'Sitting baby: round head, broad smooth shoulders and rounded seated legs from the shared human reference; omit facial details too small for this scale.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10921a97-46e3-5bea-b3ba-ce5691a7278c'
SOURCE_PATH = 'pictographic-primitives/babies/baby care body_10921a97-46e3-5bea-b3ba-ce5691a7278c.svg'
AUTHOR = 'gpt-6'

class SittingBaby(Solo48):
    icon_id = 'sitting-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('sitting', 'baby', 'infant', 'nursery')

    def build(self) -> None:
        self.add_arc('head-top', (18,12), (30,12), radius_x=6, radius_y=6)
        self.add_arc('head-bottom', (30,12), (18,12), radius_x=6, radius_y=6)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        # Shared full_body_ref.png: round head bottom18, shoulders top26 => exactly4 units of ink.
        # Round seated legs and broad arms preserve the baby's sitting pose.
        self.add_bezier('shoulder-left',(12,34),((12,29),(18,26),(24,26)))
        self.add_bezier('shoulder-right',(24,26),((30,26),(36,29),(36,34)))
        self.add_bezier('leg-right',(36,34),((40,34),(42,36),(42,38)),((42,41),(39,42),(36,42)))
        self.add_line('seat-right',(36,42),(30,42))
        self.add_bezier('leg-left',(12,34),((8,34),(6,36),(6,38)),((6,41),(9,42),(12,42)))
        self.add_line('seat-left',(12,42),(18,42))
        self.relate('connect','seat-left','leg-left')
        self.relate('connect','leg-left','shoulder-left')
        self.relate('connect','shoulder-left','shoulder-right')
        self.relate('connect','shoulder-right','leg-right')
        self.relate('connect','leg-right','seat-right')
