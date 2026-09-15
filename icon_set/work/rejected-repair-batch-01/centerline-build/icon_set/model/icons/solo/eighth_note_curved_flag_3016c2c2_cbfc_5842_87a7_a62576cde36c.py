"""Round note head, tall stem and a single long bowed flag. Extremes (8,4)-(40,44). Lucide music shared head/stem junction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3016c2c2-cbfc-5842-87a7-a62576cde36c'
SOURCE_PATH='pictographic-primitives/music/music on off_3016c2c2-cbfc-5842-87a7-a62576cde36c.svg'
AUTHOR='gpt-6'

class EighthNoteCurvedFlag(Solo48):
    icon_id='eighth-note-curved-flag'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('note', 'eighth-note', 'quaver', 'music', 'sound', 'audio', 'notation')

    def build(self):
        cx,cy,rx,ry=16,36,8,8
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'head-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('head',*[f'head-{n}' for n in range(4)],closed=True)
        self.add_line('stem',(24,36),(24,4))
        self.add_bezier('flag',(24,4),((32,4),(40,16),(40,24)))
        self.relate('connect','head','stem')
        self.relate('connect','stem','flag')
