"""A T-handle wrench with long shaft and hollow square socket; small socket collar omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35c4b52a-9f65-4349-911e-2b5d6589d1ec'
SOURCE_PATH = 'pictographic-primitives/tools/tools gasket_35c4b52a-9f65-4349-911e-2b5d6589d1ec.svg'
AUTHOR = 'gpt-6'

class THandleSocketWrench(Solo48):
    icon_id = 't-handle-socket-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('t-handle', 'socket wrench', 'wrench', 'key', 'gasket', 'spanner', 'hardware', 'tool')

    def build(self) -> None:

        def box(n,x,y,w,h,r=0):
            if not r:
                self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                a,b=pts[j],pts[(j+1)%8]
                if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
                else:self.add_line(n+str(j),a,b)
            self.add_contour(n,*[n+str(j) for j in range(8)],closed=True)

        box('bar',6,6,36,8,4)
        self.add_line('shaft',(24,14),(24,30))
        self.relate('connect','shaft','bar')
        box('socket',18,30,12,12,2)
        self.relate('connect','shaft','socket')
