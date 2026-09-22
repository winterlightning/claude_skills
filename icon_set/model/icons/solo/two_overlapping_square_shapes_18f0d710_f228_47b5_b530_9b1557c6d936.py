"""Two Overlapping Square Shapes. Two equal 24-unit square frames offset on the diagonal; the rear contour is interrupted by foreground occlusion. Lucide copy contributes rounded continuous contours. Square envelope (6,6)-(42,42)."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '18f0d710-f228-47b5-b530-9b1557c6d936'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder trim_18f0d710-f228-47b5-b530-9b1557c6d936.svg'
AUTHOR = "gpt-6"
# Saved editorial brief requests this shared design instead of a near duplicate.
SOURCE_REFERENCES = (('237056af-13be-4d06-9e11-1ea0aaf3cfc3', 'pictographic-primitives/design/picture double_237056af-13be-4d06-9e11-1ea0aaf3cfc3.svg'),)
class Drawing(Solo48):
    icon_id = 'two-overlapping-square-shapes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    aliases = ('Two Overlapping Square Shapes',)
    keywords = ('two', 'overlapping', 'square', 'shapes')
    def build(self):
        x,y,w,h,r = 18,18,24,24,4
        self.add_line("front-top",(x+r,y),(x+w-r,y))
        self.add_arc("front-tr",(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line("front-right",(x+w,y+r),(x+w,y+h-r))
        self.add_arc("front-br",(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line("front-bottom",(x+w-r,y+h),(x+r,y+h))
        self.add_arc("front-bl",(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line("front-left",(x,y+h-r),(x,y+r))
        self.add_arc("front-tl",(x,y+r),(x+r,y),radius_x=r)
        self.add_contour("front", *["front-"+s for s in ("top","tr","right","br","bottom","bl","left","tl")],closed=True)
        self.add_arc('rear-tr',(30,9),(27,6),radius_x=3,sweep=False)
        self.add_line('rear-top',(27,6),(9,6))
        self.add_arc('rear-tl',(9,6),(6,9),radius_x=3,sweep=False)
        self.add_line('rear-left',(6,9),(6,27))
        self.add_arc('rear-bl',(6,27),(9,30),radius_x=3,sweep=False)
        self.add_contour('rear','rear-tr','rear-top','rear-tl','rear-left','rear-bl')
