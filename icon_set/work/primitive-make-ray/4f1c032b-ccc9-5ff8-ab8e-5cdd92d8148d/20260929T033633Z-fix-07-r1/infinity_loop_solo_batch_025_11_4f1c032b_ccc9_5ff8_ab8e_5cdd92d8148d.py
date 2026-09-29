"""hyperloop symbol.
Plan: Restored wide rounded infinity lobes and a smooth diagonal crossing, matching the horizontal source proportions.
Construction: infinity: tangent semicircular ends joined by smooth crossing curves.
Keyshape: HRECT_M; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__infinity-loop-solo-batch-025-11/20260929T033633Z-thuan-mac/reference/hyperloop symbol_4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'infinity-loop-solo-batch-025-11'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hyperloop', 'symbol')

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

        self.add_bezier('cross-down',(14,14),((20,14),(28,34),(34,34)))
        self.add_arc('right-loop',(34,34),(34,14),radius_x=10,sweep=False)
        self.add_bezier('cross-up',(34,14),((28,14),(20,34),(14,34)))
        self.add_arc('left-loop',(14,34),(14,14),radius_x=10,sweep=True)
        self.add_contour('infinity','cross-down','right-loop','cross-up','left-loop',closed=True)

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the original broad horizontal infinity proportions; the otherwise clean geometry is shorter than the predefined horizontal rectangle.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '417b88295f945a74aa22a7ffa37b0ee49ee2689ba2088a6f636b80632521c73f'}
