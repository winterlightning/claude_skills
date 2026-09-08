"""Curled centipede; centerline extremes (2,2)-(46,46). Comma body preserved, bristles reduced to six. Asymmetric curl follows supplied source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f8bec42-eede-4182-ae2b-3d6dbe6d13f9'
SOURCE_PATH = 'pictographic-primitives/animals/insect centipede_0f8bec42-eede-4182-ae2b-3d6dbe6d13f9.svg'
AUTHOR = 'gpt-6'


class CurledCentipede(Solo48):
    icon_id = 'curled-centipede'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('centipede', 'grub', 'larva', 'bug', 'legs', 'crawl', 'microbe', 'insect')

    def build(self) -> None:
        # Curled centipede; centerline extremes (2,2)-(46,46). Comma body preserved, bristles reduced to six. Asymmetric curl follows supplied source.
        self.add_arc('crown-a', (12, 10), (24, 12), radius_x=20, radius_y=14, sweep=True)
        self.add_arc('crown-b', (24, 12), (38, 26), radius_x=14, radius_y=14, sweep=True)
        self.add_line('side', (38, 26), (38, 32))
        self.add_arc('base-r', (38, 32), (28, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('base-l', (28, 42), (18, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('inside', (18, 32), (12, 24), radius_x=6, radius_y=8, sweep=False)
        self.add_arc('head', (12, 24), (12, 10), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('body', 'crown-a', 'crown-b', 'side', 'base-r', 'base-l', 'inside', 'head', closed=True)
        self.add_line('top-left', (12, 10), (7, 3))
        self.relate("connect", 'body', 'top-left')
        self.add_line('top-mid', (24, 12), (26, 2))
        self.relate("connect", 'body', 'top-mid')
        self.add_line('top-right', (38, 26), (46, 20))
        self.relate("connect", 'body', 'top-right')
        self.add_line('low-right', (38, 32), (45, 39))
        self.relate("connect", 'body', 'low-right')
        self.add_line('base-leg', (28, 42), (28, 46))
        self.relate("connect", 'body', 'base-leg')
        self.add_line('left-leg', (12, 24), (2, 26))
        self.relate("connect", 'body', 'left-leg')
