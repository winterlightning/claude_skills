"""An upright charging battery with a top terminal and zigzag bolt. VRECT_L extremes (8,6)-(40,42). Lucide battery-charging informs the open zigzag symbol; preserve the upright body and terminal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'


class BatteryChargingVertical(Solo48):
    icon_id = 'battery-charging-vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('battery', 'charging', 'power', 'energy', 'charge', 'electric', 'level', 'device')

    def build(self) -> None:
        self.add_line('body-top',(12,12),(18,12))
        self.add_line('body-top-mid',(18,12),(30,12))
        self.add_line('body-top-end',(30,12),(36,12))
        self.add_arc('body-tr',(36,12),(40,16),radius_x=4)
        self.add_line('body-right',(40,16),(40,40))
        self.add_arc('body-br',(40,40),(36,42),radius_x=4)
        self.add_line('body-bottom',(36,42),(12,42))
        self.add_arc('body-bl',(12,42),(8,40),radius_x=4)
        self.add_line('body-left',(8,40),(8,16))
        self.add_arc('body-tl',(8,16),(12,12),radius_x=4)
        self.add_contour('body',*('body-'+p for p in ['top','top-mid','top-end','tr','right','br','bottom','bl','left','tl']),closed=True)
        self.add_polyline('terminal',(18,12),(18,6),(30,6),(30,12))
        self.relate('connect','body','terminal')
        self.add_polyline('bolt',(26,21),(17,28),(31,28),(22,35))
