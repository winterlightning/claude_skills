"""Rounded player at left, cable arches to the right earbud. Retain click wheel; omit the display for clearance. Extremes (6,6)-(42,42); Lucide smartphone rounded shell."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e469a0c-329f-4eab-b8ae-f643bfcbda08'
SOURCE_PATH = 'pictographic-primitives/music/ipod_6e469a0c-329f-4eab-b8ae-f643bfcbda08.svg'
AUTHOR = 'gpt-6'

class PortableMusicPlayerWithEarphones(Solo48):
    icon_id = 'portable-music-player-with-earphones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    categories = ("primitives", "music")
    aliases = ()
    keywords = ('ipod', 'music-player', 'earphones', 'portable', 'audio', 'device', 'mp3', 'listening')

    def build(self):
        self.add_line('player-top-a', (10, 16), (18, 16))
        self.add_line('player-top-b', (18, 16), (26, 16))
        self.add_arc('player-tr', (26, 16), (30, 20), radius_x=4)
        self.add_line('player-right', (30, 20), (30, 38))
        self.add_arc('player-br', (30, 38), (26, 42), radius_x=4)
        self.add_line('player-bottom-a', (26, 42), (18, 42))
        self.add_line('player-bottom-b', (18, 42), (10, 42))
        self.add_arc('player-bl', (10, 42), (6, 38), radius_x=4)
        self.add_line('player-left', (6, 38), (6, 20))
        self.add_arc('player-tl', (6, 20), (10, 16), radius_x=4)
        self.add_contour('player', *[f'player-{s}' for s in ('top-a','top-b','tr','right','br','bottom-a','bottom-b','bl','left','tl')], closed=True)
        cx, cy, radius = 18, 30, 3
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'wheel-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('wheel', *[f'wheel-{n}' for n in range(4)], closed=True)
        self.add_line('cable-rise',(18,16),(18,10))
        self.add_arc('cable-corner',(18,10),(22,6),radius_x=4)
        self.add_line('cable-top',(22,6),(34,6))
        self.add_arc('cable-turn',(34,6),(42,14),radius_x=8)
        self.add_line('cable-drop',(42,14),(42,28))
        self.add_contour('cable','cable-rise','cable-corner','cable-top','cable-turn','cable-drop')
        self.add_line('earbud',(42,28),(42,34))
        self.relate('connect','player','cable')
        self.relate('connect','cable','earbud')
