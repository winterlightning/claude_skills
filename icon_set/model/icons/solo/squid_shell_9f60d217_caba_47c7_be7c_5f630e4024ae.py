"""Nautilus with an open spiral and hooked tentacle. Bounds (2,2)-(46,46). Lucide snail: progressively shrinking arcs; omit the second small hook."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f60d217-caba-47c7-be7c-5f630e4024ae'
SOURCE_PATH = 'pictographic-primitives/animals/squid shell_9f60d217-caba-47c7-be7c-5f630e4024ae.svg'
AUTHOR = 'gpt-6'


class NautilusShell(Solo48):
    icon_id = 'nautilus-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('nautilus', 'shell', 'spiral', 'sea', 'marine', 'cephalopod', 'coil', 'ocean')

    def build(self) -> None:
        self.add_arc('tentacle-hook', (2,40), (12,40), radius_x=5, radius_y=6, sweep=False)
        self.add_line('tentacle', (12,40), (12,19))
        self.add_arc('shell-top-left', (12,19), (29,2), radius_x=17, sweep=True)
        self.add_arc('shell-top-right', (29,2), (46,19), radius_x=17, sweep=True)
        self.add_arc('shell-bottom-right', (46,19), (29,36), radius_x=17, sweep=True)
        self.add_arc('coil-entry', (29,36), (20,27), radius_x=9, sweep=True)
        self.add_line('coil-left', (20,27), (20,19))
        self.add_arc('coil-top-left', (20,19), (29,10), radius_x=9, sweep=True)
        self.add_arc('coil-top-right', (29,10), (38,19), radius_x=9, sweep=True)
        self.add_arc('coil-bottom', (38,19), (29,28), radius_x=9, sweep=True)
        self.add_contour('shell', 'tentacle-hook','tentacle','shell-top-left','shell-top-right','shell-bottom-right','coil-entry','coil-left','coil-top-left','coil-top-right','coil-bottom')
        self.add_line('aperture', (12,19), (20,19))
        self.relate('connect','shell','aperture')
