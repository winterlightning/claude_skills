"""Two list lines beside a single music note: one standalone song-list symbol rather than a status/action modifier. Keep the curled flag as one quarter arc. Extremes (4,8)-(44,40). Lucide music construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='31c6b551-411a-431a-a116-38809640bb62'
SOURCE_PATH='pictographic-primitives/music/playlist songs_31c6b551-411a-431a-a116-38809640bb62.svg'
AUTHOR='gpt-6'

class PlaylistWithMusicNote(Solo48):
    icon_id='playlist-with-music-note'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('playlist', 'songs', 'list', 'note', 'tracks', 'queue', 'music')

    def build(self):
        for n,y in enumerate((12,24)):
            self.add_line(f'list-{n}',(4,y),(16,y))
        cx,cy,rx,ry=30,34,6,6
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'note-head-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('note-head',*[f'note-head-{n}' for n in range(4)],closed=True)
        self.add_line('stem',(36,34),(36,8))
        self.add_arc('flag',(36,8),(44,16),radius_x=8)
        self.relate('connect','stem','note-head')
        self.relate('connect','stem','flag')
