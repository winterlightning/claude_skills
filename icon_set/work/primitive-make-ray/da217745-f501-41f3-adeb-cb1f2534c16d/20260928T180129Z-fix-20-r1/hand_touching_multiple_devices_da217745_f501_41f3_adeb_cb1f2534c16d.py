"""responsive design hand.
Plan: Restored a tall tablet, separate phone, central screen corners and an upright tapping index finger.
Construction: hand-grab: rounded upright finger; watch: device enclosure separation.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'da217745-f501-41f3-adeb-cb1f2534c16d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-touching-multiple-devices/20260928T180129Z-thuan-mac/reference/responsive design hand_da217745-f501-41f3-adeb-cb1f2534c16d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-touching-multiple-devices'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('responsive', 'design', 'hand')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_bezier('tablet',(15,39),((10,39),(6,40),(6,35)),((6,27),(6,15),(6,10)),((6,6),(8,6),(12,6)),((16,6),(21,6),(24,6)),((27,6),(27,8),(27,11)),((27,14),(27,16),(27,19)))
        self.add_line('tablet-top',(6,13),(27,13))
        self.rect('phone',34,6,10,17,2)
        self.add_line('phone-bottom',(34,18),(44,18));self.relate('connect','phone','phone-bottom')
        self.add_polyline('screen',(17,36),(17,24),(25,24))
        self.add_bezier('touch',(26,42),((23,39),(20,36),(21,34)),((23,31),(26,36),(28,37)),((28,32),(28,29),(28,28)),((28,24),(34,24),(34,28)),((34,31),(34,33),(34,33)),((37,34),(42,35),(42,37)),((42,39),(41,41),(41,42)))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve three responsive-device cues and a clear upright tapping index finger. Small phone interior and intentional overlapping hand/screen arrangement need closer spacing.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '7492b6de812a0fc8482555fad0ef13419f9046b7a19844ad19b3bf95ad1ec257'}
