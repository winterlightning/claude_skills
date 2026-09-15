"""A ringing dome bell with a hanging clapper and three rays. VRECT_L extremes (8,4)-(40,44). Lucide bell-ring informs the coherent dome and sound marks. Retain the source straight base, attached half-round clapper and three upper rays; stretch the clapper slightly to fit the keyshape."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf00e394-2d68-4d1e-aa93-205988e1f2bc'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with starburst_cf00e394-2d68-4d1e-aa93-205988e1f2bc.svg'
AUTHOR = 'gpt-6'


class AlarmBellRinging(Solo48):
    icon_id = 'alarm-bell-ringing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('alarm', 'bell', 'ringing', 'alert', 'notification', 'siren', 'warning', 'sound')

    def build(self) -> None:
        self.add_arc('dome',(8,34),(40,34),radius_x=16)
        self.add_polyline('base',(40,34),(32,34),(16,34),(8,34))
        self.relate('connect','dome','base')
        self.add_arc('clapper',(16,34),(32,34),radius_x=8,radius_y=10,sweep=False)
        self.relate('connect','base','clapper')
        self.add_line('ray-top',(24,4),(24,8))
        self.add_line('ray-left',(8,8),(12,12))
        self.add_line('ray-right',(36,12),(40,8))
