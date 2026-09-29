"""circle fork knife.
Plan: Restored a three-tine fork and a separate curved knife inside the circular dining symbol.
Construction: utensils: three parallel tines, rounded bowl, long stems.
Keyshape: CIRCLE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fork-and-knife-dining-symbol-solo/20260928T180129Z-thuan-mac/reference/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'fork-and-knife-dining-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('circle', 'fork', 'knife')

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

        self.circle('ring',24,24,20)
        self.add_bezier('fork',(13,15),((13,15),(13,23),(13,23)),((13,28),(23,28),(23,23)),((23,23),(23,15),(23,15)))
        self.add_line('stem',(18,15),(18,34))
        self.add_line('knife-back',(31,15),(31,34))
        self.add_bezier('blade',(31,15),((36,17),(37,22),(36,26)))
        self.add_line('blade-base',(36,26),(31,26))
        self.relate('connect','fork','stem');self.relate('connect','blade','knife-back');self.relate('connect','blade','blade-base');self.relate('connect','blade-base','knife-back')

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Retain three fork tines, a curved knife blade and the surrounding dining circle. Reduced utensil spacing is clear in both themes at native size.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'f0ba1c5a3b801a9af2748235185d13e78137b32a3d904687d9dfcae59bc09bd1'}
