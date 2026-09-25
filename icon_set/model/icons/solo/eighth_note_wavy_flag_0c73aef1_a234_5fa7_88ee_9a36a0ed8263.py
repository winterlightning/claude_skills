"""One broad round note head, a vertical stem and a flowing flag extending right. Head/stem share the cardinal contact. Centerline extremes (8,4)-(40,44); Lucide music construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0c73aef1-a234-5fa7-88ee-9a36a0ed8263'
SOURCE_PATH='pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'
AUTHOR='gpt-6'

class EighthNoteWavyFlag(Solo48):
    icon_id='eighth-note-wavy-flag'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('note', 'eighth-note', 'quaver', 'music', 'melody', 'notation', 'sound')

    def build(self):
        cx,cy,rx,ry=16,36,8,8
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'head-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('head',*[f'head-{n}' for n in range(4)],closed=True)
        self.add_line('stem',(24,36),(24,4))
        self.add_bezier('flag',(24,4),((24,12),(40,12),(40,20)),((40,24),(36,26),(36,28)))
        self.relate('connect','head','stem')
        self.relate('connect','flag','stem')
