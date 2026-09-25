"""Four broad bar strokes with staggered top edges and decreasing lengths. The mallet rests horizontally below the bar row. Shared bar series and a radius-5 head with a radial handle. Extremes (6,6)-(42,42). Lucide drum supports the mallet construction; no exact xylophone match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1c2356aa-7b35-4413-8da6-14723a4d3aae'
SOURCE_PATH='pictographic-primitives/music/xylophone_1c2356aa-7b35-4413-8da6-14723a4d3aae.svg'
AUTHOR='gpt-6'

class XylophoneWithMallet(Solo48):
    icon_id='xylophone-with-mallet'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('xylophone', 'glockenspiel', 'mallet', 'percussion', 'instrument', 'bars', 'music')

    def build(self):
        for n,(x,top,bottom) in enumerate(((6,6,26),(18,8,24),(30,10,22),(42,12,20))):
            self.add_line(f'bar-{n}',(x,top),(x,bottom))
        cx,cy,rx,ry=18,37,5,5
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'mallet-head-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('mallet-head',*[f'mallet-head-{n}' for n in range(4)],closed=True)
        self.add_line('mallet-handle',(23,37),(42,37))
        self.relate('connect','mallet-head','mallet-handle')
