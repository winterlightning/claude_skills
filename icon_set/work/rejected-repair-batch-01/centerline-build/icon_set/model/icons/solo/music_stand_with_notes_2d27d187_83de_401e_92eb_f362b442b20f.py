"""Open book and tripod at left, one quarter note at right. Shared book spine and stand axis; reduce floating notes to one. Centerline extremes (6,6)-(42,42). Lucide music note construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2d27d187-83de-401e-92eb-f362b442b20f'
SOURCE_PATH='pictographic-primitives/music/music book note_2d27d187-83de-401e-92eb-f362b442b20f.svg'
AUTHOR='gpt-6'

class MusicStandWithNotes(Solo48):
    icon_id='music-stand-with-notes'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('music-stand', 'sheet-music', 'book', 'notes', 'score', 'practice', 'music')

    def build(self):
        axis=14
        self.add_polyline('book',(axis,10),(6,6),(6,22),(axis,26),(22,22),(22,6),closed=True)
        self.add_line('spine',(axis,10),(axis,26))
        self.add_line('stand',(axis,26),(axis,34))
        self.add_polyline('tripod',(6,42),(axis,34),(22,42))
        self.relate('connect','book','spine')
        self.relate('connect','stand','book')
        self.relate('connect','stand','spine')
        self.relate('connect','stand','tripod')
        cx,cy,rx,ry=36,36,6,6
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'note-head-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('note-head',*[f'note-head-{n}' for n in range(4)],closed=True)
        self.add_line('note-stem',(42,36),(42,12))
        self.relate('connect','note-stem','note-head')
