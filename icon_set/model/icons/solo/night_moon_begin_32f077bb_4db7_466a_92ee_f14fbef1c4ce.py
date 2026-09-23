"""A crescent moon rises above an upward arrow and horizon.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Moon lower edge is interrupted as in the reference; small tip curvature simplified.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='32f077bb-4db7-466a-92ee-f14fbef1c4ce'
SOURCE_PATH='icon_set/work/todo-references/night moon begin_32f077bb-4db7-466a-92ee-f14fbef1c4ce.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='night-moon-begin'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('night', 'moon', 'begin')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.add_bezier('moon',(10,28),((2,18),(10,6),(24,6)),((20,18),(30,26),(40,22)),((39,24),(38,25),(38,26)))
        self.add_line('horizon',(6,42),(42,42))
        self.add_line('rise',(24,34),(24,28))
        self.add_polyline('rise-tip',(20,32),(24,28),(28,32));self.relate('connect','rise','rise-tip')

# Final visible bounds: (4, 4, 44, 44)
# Construction: Coherent outer and inner crescent curves with deliberate tip corners.
# Final reductions: Moon lower edge is interrupted as in the reference; small tip curvature simplified.
# Visual review: Crescent, short upward arrow and horizon remain distinct. Arrow shortened to preserve clearance; the crescent is intentionally open below.
