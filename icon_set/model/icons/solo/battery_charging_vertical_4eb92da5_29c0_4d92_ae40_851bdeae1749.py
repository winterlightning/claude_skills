'Charging battery: spacious terminal and a clear lightning stroke inside a balanced body.'
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
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('body-0', (12, 14), (36, 14))
        self.add_arc('body-1', (36, 14), (40, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('body-2', (40, 18), (40, 40))
        self.add_arc('body-3', (40, 40), (36, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('body-4', (36, 44), (12, 44))
        self.add_arc('body-5', (12, 44), (8, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('body-6', (8, 40), (8, 18))
        self.add_arc('body-7', (8, 18), (12, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('terminal-1', (16, 14), (16, 4))
        self.add_line('terminal-2', (16, 4), (32, 4))
        self.add_line('terminal-3', (32, 4), (32, 14))
        self.add_line('charge-1', (26, 23), (18, 30))
        self.add_line('charge-2', (18, 30), (29, 30))
        self.add_line('charge-3', (29, 30), (22, 35))
        self.add_contour('body', *('body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7'), closed=True)
        self.add_contour('terminal', *('terminal-1', 'terminal-2', 'terminal-3'), closed=False)
        self.add_contour('charge', *('charge-1', 'charge-2', 'charge-3'), closed=False)
        self.relate('connect', *('terminal', 'body'))
