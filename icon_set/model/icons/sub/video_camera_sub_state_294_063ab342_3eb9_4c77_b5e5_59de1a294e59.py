"""Video Camera: A wide rounded rectangular camera body has a trapezoidal lens hood attached to its right side. The hood widens toward its upright outer edge, and the body stays blank.

Construction: Rounded blank camera body retains a distinct attached right wedge; no lens added.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'
AUTHOR = 'gpt-6'


class VideoCameraSubState294(Sub32):
    icon_id = 'video-camera-sub-state-294'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('video', 'camera', 'wide', 'rounded', 'rectangular', 'body', 'trapezoidal', 'lens')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',2,6,22,26,4)
        self.add_polyline('wedge',(22,12),(30,8),(30,24),(22,20))
        self.relate('connect','body','wedge')
