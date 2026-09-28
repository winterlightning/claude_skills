"""Woman explorer with a brimmed hat, flared hair and backpack sides.

VRECT_L (8,4)-(40,44). A circular jaw sits between flared hair ends;
hat band and backpack outline are omitted, keeping crown, brim and the raised backpack sides.
Human user.svg supplies curved open shoulders; Lucide hat-glasses supplies
the crown-to-brim construction. Axis24 owns the mirrored features.
Jaw radius8 at (24,16), bottom24; shoulders28: zero visible ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2ee8f5f0-6cf6-43a9-8839-ed970895cf00'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar adventure woman_2ee8f5f0-6cf6-43a9-8839-ed970895cf00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-explorer-with-a-brimmed-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ('Woman Adventurer wearing Safari Hat',)
    keywords = ('explorer','hair','hat','backpack','straps','person','adventure')

    def build(self):
        self.add_polyline('hat',(12,16),(16,4),(32,4),(36,16))
        self.add_polyline('brim',(8,16),(12,16),(16,16),(32,16),(36,16),(40,16))
        self.add_arc('jaw',(32,16),(16,16),radius_x=8)
        self.relate('connect','hat','brim')
        self.relate('connect','jaw','brim')
        for side,sgn in [('left',-1),('right',1)]:
            x=lambda d:24+sgn*d
            self.add_bezier('hair-'+side,(x(8),16),((x(9),20),(x(14),25),(x(16),25)))
            self.relate('connect','hair-'+side,'jaw','brim')
        top=24+HEAD_BODY_CENTERLINE_GAP
        self.add_arc('body-top',(8,44),(24,top),radius_x=16)
        self.add_arc('body-right',(24,top),(40,44),radius_x=16)
        self.relate('connect','body-top','body-right')
        self.relate('connect','jaw','body-top')
        self.relate('connect','jaw','body-right')
        for side,x in [('left',8),('right',40)]:
            self.add_line('body-backpack-'+side,(x,36),(x,44))
            self.relate('connect','body-backpack-'+side,('body-top' if side=='left' else 'body-right'))
