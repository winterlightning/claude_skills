"""Shield enclosing a monitor; extremes (5,2)-(43,46). Lucide shield symmetry and monitor-down stand. Bezel divider omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db0cac9f-1efd-4347-be80-52b232e59a07'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/computer shield_db0cac9f-1efd-4347-be80-52b232e59a07.svg'
AUTHOR = 'astra-chatgpt'

class MonitorInSecurityShield(Solo48):
    icon_id = 'monitor-in-security-shield'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('security', 'shield', 'monitor', 'computer', 'protection', 'antivirus', 'safe', 'device')

    def build(self) -> None:
        self.add_line('shield-top-1', (5, 22), (5, 6))
        self.add_line('shield-top-2', (5, 6), (24, 2))
        self.add_line('shield-top-3', (24, 2), (43, 6))
        self.add_line('shield-top-4', (43, 6), (43, 22))
        self.add_arc('shield-right', (43, 22), (24, 46), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('shield-left', (24, 46), (5, 22), radius_x=25, radius_y=25, sweep=True)
        self.add_contour('shield', 'shield-top-1', 'shield-top-2', 'shield-top-3', 'shield-top-4', 'shield-right', 'shield-left', closed=True)
        self.add_line('screen-t', (16, 13), (32, 13))
        self.add_arc('screen-ne', (32, 13), (34, 15), radius_x=2, radius_y=2, sweep=True)
        self.add_line('screen-r', (34, 15), (34, 24))
        self.add_arc('screen-se', (34, 24), (32, 26), radius_x=2, radius_y=2, sweep=True)
        self.add_line('screen-b', (32, 26), (16, 26))
        self.add_arc('screen-sw', (16, 26), (14, 24), radius_x=2, radius_y=2, sweep=True)
        self.add_line('screen-l', (14, 24), (14, 15))
        self.add_arc('screen-nw', (14, 15), (16, 13), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('screen', 'screen-t', 'screen-ne', 'screen-r', 'screen-se', 'screen-b', 'screen-sw', 'screen-l', 'screen-nw', closed=True)
        self.add_line('neck', (24, 26), (24, 33))
        self.add_line('foot', (19, 33), (29, 33))
        self.relate('connect', 'screen', 'neck')
        self.relate('connect', 'neck', 'foot')
