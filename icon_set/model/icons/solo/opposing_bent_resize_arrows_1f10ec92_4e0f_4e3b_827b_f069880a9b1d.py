from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f10ec92-4e0f-4e3b-827b-f069880a9b1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/resize expand sides_1f10ec92-4e0f-4e3b-827b-f069880a9b1d.svg'
AUTHOR = 'gpt-6'


class OpposingBentResizeArrows(Solo48):
    icon_id = 'opposing-bent-resize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('arrows', 'resize', 'expand', 'bent', 'directions', 'opposing', 'transform', 'layout')

    def build(self) -> None:
        # The source has a shared bent shaft with two heads and an opposite corner.
        self.add_line('shaft-left',(12,42),(12,16))
        self.add_arc('shaft-corner',(12,16),(16,12),radius_x=4)
        self.add_line('shaft-top',(16,12),(42,12))
        self.add_contour('shaft','shaft-left','shaft-corner','shaft-top')
        self.add_polyline('right-head',(34,6),(42,12),(34,18))
        self.add_polyline('down-head',(6,34),(12,42),(18,34))
        for name in ('right-head','down-head'):self.relate('connect',name,'shaft')
        self.add_line('opposite-right',(42,24),(42,38))
        self.add_arc('opposite-bend',(42,38),(38,42),radius_x=4)
        self.add_line('opposite-bottom',(38,42),(24,42))
        self.add_contour('opposite','opposite-right','opposite-bend','opposite-bottom')
