"""Mirrored padded earcups beneath one semicircular headband. Shared radii and mirrored coordinates. Extremes (6,6)-(42,42). Lucide headphones branching topology."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c19c0577-fcb3-4fbf-b5c9-dfcd789bfafc'
SOURCE_PATH='pictographic-primitives/music/spatial audio device_c19c0577-fcb3-4fbf-b5c9-dfcd789bfafc.svg'
AUTHOR='gpt-6'

class OverEarHeadphones(Solo48):
    icon_id='over-ear-headphones'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('headphones', 'audio', 'listening', 'headset', 'spatial-audio', 'sound', 'music')

    def build(self):
        axis=24
        for name,mirror in (('left',False),('right',True)):
            p=lambda x,y: (2*axis-x,y) if mirror else (x,y)
            sweep=not mirror
            self.add_line(f'{name}-top',p(6,24),p(12,24))
            self.add_arc(f'{name}-tr',p(12,24),p(16,28),radius_x=4,sweep=sweep)
            self.add_line(f'{name}-inner',p(16,28),p(16,38))
            self.add_arc(f'{name}-br',p(16,38),p(12,42),radius_x=4,sweep=sweep)
            self.add_line(f'{name}-bottom',p(12,42),p(10,42))
            self.add_arc(f'{name}-bl',p(10,42),p(6,38),radius_x=4,sweep=sweep)
            self.add_line(f'{name}-outer',p(6,38),p(6,24))
            self.add_contour(name,*[f'{name}-{suffix}' for suffix in ('top','tr','inner','br','bottom','bl','outer')],closed=True)
        self.add_arc('headband',(6,24),(42,24),radius_x=18)
        self.relate('connect','headband','left')
        self.relate('connect','headband','right')
