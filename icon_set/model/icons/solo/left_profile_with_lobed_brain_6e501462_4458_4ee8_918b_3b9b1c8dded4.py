"""Anatomical head with brain intrinsic to skull. Broad SQUARE skull leaves room for visible lobes and short descending brain stem. Human_ref informs smooth silhouette; Lucide brain informs lobe junctions.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6e501462-4458-4ee8-918b-3b9b1c8dded4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/neurobiologist_6e501462-4458-4ee8-918b-3b9b1c8dded4.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'left-profile-with-lobed-brain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "primitives-generate"
    aliases = ('Human Head with Brain',)
    keywords = ('left', 'profile', 'with', 'lobed', 'brain')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        def p(x,y): return (48-x,y) if False else (x,y)
        def b(n,start,*ss): curve(n,p(*start),*[tuple(p(*v) for v in s) for s in ss])
        def pl(n,*pts): poly(n,*[p(*v) for v in pts])
        b('skull',(36,42),((32,35),(42,32),(42,23)),((42,13),(35,6),(26,6)),((16,6),(10,12),(10,21)))
        pl('face',(10,21),(6,28),(8,28),(8,36),(22,36),(22,42));join('skull','face')
        b('brain',(22,27),((18,27),(18,21),(21,20)),((20,14),(25,13),(27,17)),((31,14),(33,20),(31,23)),((33,27),(31,30),(28,29)),((27,25),(24,27),(22,27)))
