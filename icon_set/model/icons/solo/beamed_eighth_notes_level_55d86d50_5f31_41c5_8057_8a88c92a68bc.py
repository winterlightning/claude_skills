"""Equal circular note heads and exact stem/beam attachments. Two beams for sixteenths; level heads for the eighth-note pair. Extremes (6,6)-(42,42). Lucide music construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='55d86d50-5f31-41c5-8057-8a88c92a68bc'
SOURCE_PATH='pictographic-primitives/music/music_55d86d50-5f31-41c5-8057-8a88c92a68bc.svg'
AUTHOR='gpt-6'

class BeamedEighthNotesLevel(Solo48):
    icon_id='beamed-eighth-notes-level'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("music", "state", "other", "primitives-generate")
    aliases=()
    keywords=('music', 'notes', 'eighth-notes', 'beamed', 'melody', 'song', 'audio')

    def build(self):
        radius=6
        for name,cx,cy,top in (('left',12,36,10),('right',36,36,6)):
            points=((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
            for n in range(4):
                self.add_arc(f'{name}-head-{n}',points[n],points[(n+1)%4],radius_x=radius)
            self.add_contour(f'{name}-head',*[f'{name}-head-{n}' for n in range(4)],closed=True)
            mid=top+9
            self.add_polyline(f'{name}-stem',(cx+radius,cy),(cx+radius,mid),(cx+radius,top))
            self.relate('connect',f'{name}-head',f'{name}-stem')
        self.add_line('beam-top',(18,10),(42,6))
        for name in ('left','right'):
            self.relate('connect','beam-top',f'{name}-stem')
