"""Support Agent with Boom Microphone — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a796c493-db7e-58ce-9455-493c17f8705a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/headphones customer support_a796c493-db7e-58ce-9455-493c17f8705a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'support-agent-with-boom-microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('support', 'agent', 'with', 'boom', 'microphone')

    def build(self):
        # Plan: concentric circular face, broad arch, paired ear returns.
        # Human user.svg supplies circular face and broad shoulder proportions.
        # Lucide headset informs headband and microphone lead construction.
        # VRECT_L centerline extrema (8,4)-(40,44). Tiny facial marks omitted.
        self.add_arc('headband',(8,20),(40,20),radius_x=16)
        self.add_arc('crown',(16,24),(32,24),radius_x=8)
        self.add_arc('face',(32,24),(16,24),radius_x=8)
        self.add_contour('head','crown','face',closed=True)
        for side,sign in [('left',-1),('right',1)]:
            self.add_polyline('ear-'+side,(24+sign*16,20),(24+sign*16,24),(24+sign*8,24))
            self.relate('connect','ear-'+side,'headband')
            self.relate('connect','ear-'+side,'head')
        # Head-only portrait: no detached torso. Lower boom is the identity cue.
        self.add_line('boom-side',(40,24),(40,36))
        self.add_arc('boom-corner',(40,36),(32,44),radius_x=8)
        self.add_line('microphone',(32,44),(24,44))
        self.add_contour('boom','boom-side','boom-corner','microphone')
        self.relate('connect','boom','ear-right')

