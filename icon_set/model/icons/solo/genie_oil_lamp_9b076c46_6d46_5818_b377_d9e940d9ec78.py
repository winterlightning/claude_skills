"""An oil lamp with a curled handle, lid finial, raised spout and foot. HRECT_L extremes (2,8)-(46,40). Preserve the source side-view asymmetry; omit foot steps."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b076c46-6d46-5818-b377-d9e940d9ec78'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/lamp genie_9b076c46-6d46-5818-b377-d9e940d9ec78.svg'


class GenieOilLamp(Solo48):
    icon_id = 'genie-oil-lamp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('lamp', 'genie', 'oil lamp', 'aladdin', 'wish', 'magic', 'arabian', 'antique')

    def build(self) -> None:
        self.add_line('lid-left',(12,20),(24,20))
        self.add_line('lid-right',(24,20),(32,20))
        self.add_line('spout-top',(32,20),(46,14))
        self.add_arc('spout-underside',(46,14),(24,32),radius_x=30)
        self.add_arc('belly',(24,32),(12,20),radius_x=12)
        self.add_contour('body','lid-left','lid-right','spout-top','spout-underside','belly',closed=True)
        self.add_arc('handle',(12,20),(12,32),radius_x=10,radius_y=6,sweep=False)
        self.add_line('handle-join',(12,32),(20,32))
        self.add_contour('handle-outline','handle','handle-join')
        self.relate('connect','body','handle-outline')
        self.add_line('finial',(24,8),(24,20))
        self.relate('connect','body','finial')
        self.add_line('foot',(24,32),(24,40))
        self.add_line('base',(16,40),(32,40))
        self.relate('connect','foot','base')
        self.relate('connect','body','foot')
