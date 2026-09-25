"""Cleaning worker bust beside broom. Human_ref circular head and broad shoulders; exact detached gap 4. HRECT_L supplies space for broom. Cap brim retained; collar omitted.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c89e718-df3d-451b-808f-bb9daab2e5b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/janitor_9c89e718-df3d-451b-808f-bb9daab2e5b2.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'cleaning-worker-with-upright-broom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "primitives-generate"
    aliases = ('Cleaning Worker with Broom',)
    keywords = ('cleaning', 'worker', 'with', 'upright', 'broom')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        circle('head',14,14,6)
        line('cap-brim',(8,14),(20,14))
        line('cap-peak',(20,14),(24,14))
        join('head','cap-brim','cap-peak')
        curve('shoulders',(4,40),((4,32),(8,28),(14,28)),((20,28),(24,32),(24,40)))
        line('broom-shaft',(38,8),(38,30))
        poly('broom-head',(38,30),(42,30),(44,40),(32,40),(34,30),(38,30),closed=True)
        join('broom-shaft','broom-head-1','broom-head-5')
