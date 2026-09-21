'Monitor in security shield: independent spacing revision.\n\nRebalance shield and monitor for an eight-unit stand and clear lower corners.\nNative solo family, VRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db0cac9f-1efd-4347-be80-52b232e59a07'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/computer shield_db0cac9f-1efd-4347-be80-52b232e59a07.svg'
AUTHOR = 'gpt-6'

class MonitorInSecurityShield(Solo48):
    icon_id = 'monitor-in-security-shield'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('security', 'shield', 'monitor', 'computer', 'protection', 'antivirus', 'safe', 'device')

    def build(self):
        self.add_polyline('shield',(8, 10),(24, 4),(40, 10),(40, 34),(24, 44),(8, 34),closed=True)
        self.add_polyline('screen',(16, 16),(32, 16),(32, 24),(24, 24),(16, 24),closed=True)
        self.add_line('neck',(24, 24),(24, 32))
        self.add_polyline('foot',(20, 32),(24, 32),(28, 32),closed=False)
        self.relate('connect','screen','neck')
        self.relate('connect','neck','foot')
