from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edbc528e-ef07-50da-aefa-8b1cebd26d93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/gradient_edbc528e-ef07-50da-aefa-8b1cebd26d93.svg'
AUTHOR = 'gpt-6'


class GradientAdjustmentBarWithEndMarkers(Solo48):
    icon_id = 'gradient-adjustment-bar-with-end-markers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('gradient', 'bar', 'slider', 'markers', 'stops', 'color', 'adjustment', 'control')

    def build(self) -> None:
        # Four repeated ten-unit sections and two opposing open stop markers.
        self.add_polyline('bar',(4,20),(44,20),(44,28),(4,28),closed=True)
        for x in (14,24,34):
            name=f'divider-{x}'
            self.add_line(name,(x,20),(x,28))
            self.relate('connect',name,'bar')
        self.add_polyline('upper-stop',(34,8),(39,12),(44,8))
        self.add_polyline('lower-stop',(4,40),(9,36),(14,40))
