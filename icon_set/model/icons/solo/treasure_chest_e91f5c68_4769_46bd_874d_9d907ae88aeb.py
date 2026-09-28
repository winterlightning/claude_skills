"""A domed treasure chest with reinforcing bands and a central latch.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide gift (rounded box and bands); no local treasure-chest match informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e91f5c68-4769-46bd-874d-9d907ae88aeb'
SOURCE_PATH='pictographic-primitives/rewards/treasure chest_e91f5c68-4769-46bd-874d-9d907ae88aeb.svg'
AUTHOR='gpt-6'
class TreasureChest(Solo48):
    icon_id='treasure-chest'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('reward','celebration','treasure-chest')
    def build(self) -> None:
        self.add_arc('lid-left',(4,20),(16,8),radius_x=12)
        self.add_line('lid-top',(16,8),(32,8))
        self.add_arc('lid-right',(32,8),(44,20),radius_x=12)
        self.add_line('wall-right-top',(44,20),(44,22))
        self.add_line('wall-right',(44,22),(44,36))
        self.add_arc('corner-right',(44,36),(40,40),radius_x=4)
        self.add_line('bottom-right',(40,40),(32,40))
        self.add_line('bottom',(32,40),(16,40))
        self.add_line('bottom-left',(16,40),(8,40))
        self.add_arc('corner-left',(8,40),(4,36),radius_x=4)
        self.add_line('wall-left',(4,36),(4,22))
        self.add_line('wall-left-top',(4,22),(4,20))
        self.add_contour('chest','lid-left','lid-top','lid-right','wall-right-top','wall-right','corner-right','bottom-right','bottom','bottom-left','corner-left','wall-left','wall-left-top',closed=True)
        self.add_polyline('seam',(4,22),(16,22),(24,22),(32,22),(44,22))
        self.add_polyline('band-left',(16,8),(16,22),(16,40))
        self.add_polyline('band-right',(32,8),(32,22),(32,40))
        self.add_line('latch',(24,22),(24,30))
        for name in ['seam','band-left','band-right']:
            self.relate('connect','chest',name)
        self.relate('connect','seam','band-left')
        self.relate('connect','seam','band-right')
        self.relate('connect','seam','latch')
