"""Elliptical cymbal with cardinal attachment nodes, centered post and tripod. Omit the small bell. Centerline extremes (8,4)-(40,44); Lucide drum ellipse construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fc924f0e-a62f-5872-91e8-42b85cfe5cbb'
SOURCE_PATH='pictographic-primitives/music/modern music cymbal_fc924f0e-a62f-5872-91e8-42b85cfe5cbb.svg'
AUTHOR='gpt-6'

class CymbalOnStand(Solo48):
    icon_id='cymbal-on-stand'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('cymbal', 'drum-kit', 'percussion', 'stand', 'instrument', 'band', 'music')

    def build(self):
        cx,cy,rx,ry=24,14,16,6
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'cymbal-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('cymbal',*[f'cymbal-{n}' for n in range(4)],closed=True)
        axis=24
        self.add_line('top-post',(axis,4),(axis,8))
        self.add_line('stand',(axis,20),(axis,34))
        self.add_line('center-foot',(axis,34),(axis,44))
        self.add_polyline('tripod',(12,44),(axis,34),(36,44))
        for part in ('top-post','stand'):
            self.relate('connect',part,'cymbal')
        for part in ('center-foot','tripod'):
            self.relate('connect',part,'stand')
        self.relate('connect','center-foot','tripod')
