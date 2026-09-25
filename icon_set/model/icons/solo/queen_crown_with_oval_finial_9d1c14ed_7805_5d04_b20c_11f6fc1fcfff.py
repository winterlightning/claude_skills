"""A curved queen crown with raised central lobe and oval finial above an elliptical rim.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide crown informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d1c14ed-7805-5d04-b20c-11f6fc1fcfff'
SOURCE_PATH='pictographic-primitives/rewards/vip crown queen_9d1c14ed-7805-5d04-b20c-11f6fc1fcfff.svg'
AUTHOR='gpt-6'
class QueenCrownWithOvalFinial(Solo48):
    icon_id='queen-crown-with-oval-finial'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('reward','celebration','queen-crown-with-oval-finial')
    def build(self) -> None:
        self.add_arc('finial-right',(24,4),(24,16),radius_x=4,radius_y=6)
        self.add_arc('finial-left',(24,16),(24,4),radius_x=4,radius_y=6)
        self.add_contour('finial','finial-right','finial-left',closed=True)
        self.add_line('left-side-1',(12,38),(8,20))
        self.add_line('left-side-2',(8,20),(15,26))
        self.add_arc('lobe-left',(15,26),(24,16),radius_x=12)
        self.add_arc('lobe-right',(24,16),(33,26),radius_x=12)
        self.add_line('right-side-1',(33,26),(40,20))
        self.add_line('right-side-2',(40,20),(36,38))
        self.add_contour('crown','left-side-1','left-side-2','lobe-left','lobe-right','right-side-1','right-side-2')
        self.relate('connect','finial','crown')
        self.add_arc('rim-front',(36,38),(12,38),radius_x=12,radius_y=6)
        self.add_arc('rim-back',(12,38),(36,38),radius_x=12,radius_y=6)
        self.add_contour('rim','rim-front','rim-back',closed=True)
        self.relate('connect','crown','rim')
