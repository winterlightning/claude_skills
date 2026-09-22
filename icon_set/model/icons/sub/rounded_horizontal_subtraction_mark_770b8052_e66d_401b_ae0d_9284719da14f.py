"""Outlined rounded subtraction bar. Shared radius6 capsule ends; preserve open interior. HRECT_S is broadest compact legal capsule.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '770b8052-e66d-401b-ae0d-9284719da14f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/minimize_770b8052-e66d-401b-ae0d-9284719da14f.svg'
AUTHOR = "gpt-6"
class Drawing(Sub32):
    icon_id = 'rounded-horizontal-subtraction-mark'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = "Uncategorized"
    aliases = ('Rounded Horizontal Minus Sign',)
    keywords = ('rounded', 'horizontal', 'subtraction', 'mark')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        line('top',(8,10),(24,10))
        self.add_arc('end-right',(24,10),(24,22),radius_x=6)
        line('bottom',(24,22),(8,22))
        self.add_arc('end-left',(8,22),(8,10),radius_x=6)
        self.add_contour('minus','top','end-right','bottom','end-left',closed=True)
