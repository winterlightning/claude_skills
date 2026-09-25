"""One cylindrical shell, one central tension rod, crossed sticks above it. Omit doubled hoops. Extremes (6,6)-(42,42); Lucide drum grouped shell and rods."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0706c6f-5c48-4d64-a145-d56c1fe0de85'
SOURCE_PATH = 'pictographic-primitives/music/drums_d0706c6f-5c48-4d64-a145-d56c1fe0de85.svg'
AUTHOR = 'gpt-6'

class SnareDrumCrossedSticks(Solo48):
    icon_id = 'snare-drum-crossed-sticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ()
    keywords = ('drum', 'snare', 'drumsticks', 'percussion', 'instrument', 'band', 'music', 'rhythm')

    def build(self):
        self.add_line('shell-top-a', (10, 26), (24, 26))
        self.add_line('shell-top-b', (24, 26), (38, 26))
        self.add_arc('shell-tr', (38, 26), (42, 30), radius_x=4)
        self.add_line('shell-right', (42, 30), (42, 38))
        self.add_arc('shell-br', (42, 38), (38, 42), radius_x=4)
        self.add_line('shell-bottom-a', (38, 42), (24, 42))
        self.add_line('shell-bottom-b', (24, 42), (10, 42))
        self.add_arc('shell-bl', (10, 42), (6, 38), radius_x=4)
        self.add_line('shell-left', (6, 38), (6, 30))
        self.add_arc('shell-tl', (6, 30), (10, 26), radius_x=4)
        self.add_contour('shell', *[f'shell-{s}' for s in ('top-a','top-b','tr','right','br','bottom-a','bottom-b','bl','left','tl')], closed=True)
        self.add_line('tension-rod',(24,26),(24,42))
        self.relate('connect','tension-rod','shell')
        self.add_line('stick-left',(8,6),(34,18))
        self.add_line('stick-right',(40,6),(14,18))
        self.relate('occlude','stick-left','stick-right')
