"""Anatomical head with brain intrinsic to skull. Broad SQUARE skull leaves room for visible lobes and short descending brain stem. Human_ref informs smooth silhouette; Lucide brain informs lobe junctions.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0231a044-ecb1-470e-bcc3-8a45ccdc5d4a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'right-profile-with-folded-brain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "Uncategorized"
    aliases = ('Human Head with Brain',)
    keywords = ('right', 'profile', 'with', 'folded', 'brain')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        def p(x,y): return (48-x,y) if True else (x,y)
        def b(n,start,*ss): curve(n,p(*start),*[tuple(p(*v) for v in s) for s in ss])
        def pl(n,*pts): poly(n,*[p(*v) for v in pts])
        b('skull',(36,42),((32,35),(42,32),(42,23)),((42,13),(35,6),(26,6)),((16,6),(10,12),(10,21)))
        pl('face',(10,21),(6,28),(8,28),(8,36),(22,36),(22,42));join('skull','face')
        # Two broad lobes and one open fold retain the brain's folded reading.
        b('brain',(20,26),((18,26),(18,20),(20,19)),((19,14),(26,13),(27,17)),((33,15),(34,23),(30,26)),((27,28),(23,27),(20,26)))
