"""Decorated Gudi Padwa Flag.

Plan: Wavy ceremonial flag on a pole topped by a rounded finial. Reduce tiny foliage and tassels. Lucide flag informs paired wave edges. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b8937f5-ec61-4d22-8b5b-02a296bd4054'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/gudi padwa 1_3b8937f5-ec61-4d22-8b5b-02a296bd4054.svg'
AUTHOR = 'gpt-6'

class DecoratedGudiPadwaFlag(Solo48):
    icon_id = 'decorated-gudi-padwa-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('decorated', 'gudi', 'padwa', 'flag')

    def build(self):
        pts=[(16,4),(24,10),(16,16),(8,10),(16,4)]
        for i in range(4):self.add_arc(f'finial-{i}',pts[i],pts[i+1],radius_x=8,radius_y=6)
        self.add_contour('finial',*[f'finial-{i}' for i in range(4)],closed=True)
        self.add_polyline('pole',(16,16),(16,20),(16,36),(16,44))
        self.add_arc('flag-tl',(16,20),(28,24),radius_x=12,radius_y=4,sweep=False)
        self.add_arc('flag-tr',(28,24),(40,20),radius_x=12,radius_y=4,sweep=False)
        self.add_line('flag-right',(40,20),(40,36))
        self.add_arc('flag-br',(40,36),(28,40),radius_x=12,radius_y=4)
        self.add_arc('flag-bl',(28,40),(16,36),radius_x=12,radius_y=4)
        self.add_contour('flag','flag-tl','flag-tr','flag-right','flag-br','flag-bl')
        self.relate('connect','finial','pole');self.relate('connect','pole','flag')
