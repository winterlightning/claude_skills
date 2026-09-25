"""A horizontal-handled hammer strikes a nail below its upright head; impact dashes reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '742f7382-79a3-428c-9817-1a940e466113'
SOURCE_PATH = 'pictographic-primitives/tools/hardware hammer nail hit_742f7382-79a3-428c-9817-1a940e466113.svg'
AUTHOR = 'gpt-6'

class HammerStrikingNail(Solo48):
    icon_id = 'hammer-striking-nail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('hammer', 'nail', 'hit', 'strike', 'impact', 'hardware', 'construction', 'tool')

    def build(self) -> None:
        self.add_polyline('head',(26,24),(26,12),(31,6),(36,12),(36,24),closed=True)
        self.add_polyline('handle',(26,12),(6,12),(6,22),(26,22))
        self.relate('connect','handle','head')
        self.add_line('nail-head',(26,34),(34,34))
        self.add_line('nail-shank',(30,34),(30,42))
        self.relate('connect','nail-head','nail-shank')
        self.add_line('impact-left',(16,32),(18,34))
        self.add_line('impact-right',(42,30),(42,32))
