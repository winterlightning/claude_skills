"""Two nested C arcs linked by the curled arrowhead at the upper-right. Preserve asymmetric directional opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014a161f-8fa3-4281-9043-eacf794cfc32'
SOURCE_PATH = 'pictographic-primitives/logos/rdio logo_014a161f-8fa3-4281-9043-eacf794cfc32.svg'
AUTHOR = 'gpt-6'

class RdioLogo(Solo48):
    icon_id = 'rdio-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('rdio', 'music', 'streaming', 'refresh', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Two nested C arcs linked by the curled arrowhead at the upper-right. Preserve asymmetric directional opening.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.

        self.add_arc('outer',(40,36),(40,12),radius_x=20,large_arc=True)
        self.add_polyline('arrow',(40,12),(44,24),(35,24))
        self.add_arc('inner',(35,24),(24,35),radius_x=11,large_arc=True,sweep=False)
        self.relate('connect','outer','arrow')
        self.relate('connect','arrow','inner')

