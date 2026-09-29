"""wearable smart watch.
Plan: Reconstructed the closed perspective strap, front display edges, and two short horizontal display marks.
Construction: watch: distinguish strap from watch face with coherent contours.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '1cd0692c-3506-4df2-80d7-66be18de3019'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-fitness-band-with-two-display-marks/20260928T180129Z-thuan-mac/reference/wearable smart watch_1cd0692c-3506-4df2-80d7-66be18de3019.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'closed-fitness-band-with-two-display-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('wearable', 'smart', 'watch')

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

        self.circle('band',24,24,18)
        self.add_bezier('front-edge',(29,6),((17,12),(17,36),(29,42)))
        self.add_bezier('inner-edge',(25,10),((37,19),(37,29),(25,38)))
        self.add_line('display-top',(8,16),(21,16));self.add_line('display-bottom',(8,32),(21,32))
        self.add_line('mark1',(12,22),(15,22));self.add_line('mark2',(12,27),(15,27))
