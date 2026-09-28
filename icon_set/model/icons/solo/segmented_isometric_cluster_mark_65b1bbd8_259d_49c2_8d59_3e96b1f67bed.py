"""A split peaked upper module floats above a descending segmented lower band. Shared parameters own vertical divisions; x24 is the principal upper axis. Source supplies the segmented silhouette. Lucide box contributes shared face joins; no exact Lucide cluster match.
Plan: exact SQUARE envelope; stroke 4, integer points, shared attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65b1bbd8-259d-49c2-8d59-3e96b1f67bed'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon elastic map module_65b1bbd8-259d-49c2-8d59-3e96b1f67bed.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'segmented-isometric-cluster-mark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = []
    keywords = ['segmented', 'isometric', 'cluster', 'mark']

    def build(self):
        self.add_polyline('roof-left',(24,6),(6,10),(6,20),(24,20))
        self.add_polyline('roof-right',(24,20),(42,20),(42,10),(24,6))
        self.add_line('roof-seam',(24,6),(24,20))
        self.relate('connect','roof-left','roof-right','roof-seam')
        xs=[6,15,24,33,42]
        for i,(a,b) in enumerate(zip(xs,xs[1:])):self.add_line(f'band-top-{i}',(a,28),(b,28))
        self.add_contour('band-top',*[f'band-top-{i}' for i in range(4)])
        for i,(x,y) in enumerate(zip(xs,[34,38,42,40,38])):
            self.add_line(f'division-{i}',(x,28),(x,y))
            for j in (i-1,i):
                if 0<=j<4:self.relate('connect',f'division-{i}',f'band-top-{j}')
        self.add_line('bottom-left',(24,42),(33,40));self.add_line('bottom-right',(33,40),(42,38))
        self.add_contour('bottom','bottom-left','bottom-right')
        self.relate('connect','bottom-left','division-2','division-3')
        self.relate('connect','bottom-right','division-3','division-4')
