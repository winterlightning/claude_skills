"""Two equal circular heads with a shared radius and 24-unit horizontal step; stems share exact head endpoints and a sloping beam. Centerline extremes (6,6)-(42,42). Lucide music loop/stem topology."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='16a68778-68d4-5f6b-9ce5-e5182435ed96'
SOURCE_PATH='pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'
AUTHOR='gpt-6'

class BeamedEighthNotes(Solo48):
    icon_id='beamed-eighth-notes'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('notes', 'eighth-notes', 'beamed', 'music', 'melody', 'notation', 'song')

    def build(self):
        radius=6
        for name,cx,cy,top in (('left',12,36,12),('right',36,30,6)):
            points=((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
            for n in range(4):
                self.add_arc(f'{name}-head-{n}',points[n],points[(n+1)%4],radius_x=radius)
            self.add_contour(f'{name}-head',*[f'{name}-head-{n}' for n in range(4)],closed=True)
            self.add_line(f'{name}-stem',(cx+radius,cy),(cx+radius,top))
            self.relate('connect',f'{name}-stem',f'{name}-head')
        self.add_line('beam',(18,12),(42,6))
        for name in ('left','right'):
            self.relate('connect','beam',f'{name}-stem')
