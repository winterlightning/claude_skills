"""A broad round bell joins the outer and inner sweeps of a U-shaped horn, ending in an angled mouthpiece. Extremes (6,6)-(42,42). Coherent tangent curves preserve deliberate asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b551d9d4-0be3-4e13-8d2a-c7ee5ef8c8b6'
SOURCE_PATH='pictographic-primitives/music/trumpet_b551d9d4-0be3-4e13-8d2a-c7ee5ef8c8b6.svg'
AUTHOR='gpt-6'

class CurvedHorn(Solo48):
    icon_id='curved-horn'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('horn', 'shofar', 'wind', 'instrument', 'brass', 'call', 'folk', 'music')

    def build(self):
        cx,cy,rx,ry=14,14,8,8
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'bell-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('bell',*[f'bell-{n}' for n in range(4)],closed=True)
        self.add_bezier('outside',(6,14),((6,32),(12,42),(26,42)),((34,42),(38,32),(42,26)))
        self.add_line('mouthpiece',(42,26),(36,18))
        self.add_bezier('inside',(36,18),((32,28),(26,32),(22,28)),((18,24),(20,20),(22,14)))
        self.add_contour('body','outside','mouthpiece','inside')
        self.relate('connect','body','bell')
