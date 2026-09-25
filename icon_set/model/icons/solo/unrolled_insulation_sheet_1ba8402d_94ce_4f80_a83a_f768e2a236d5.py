"""Unrolled Insulation Sheet.

Symbol plan: One upright roll with a circular end and a rectangular unfurled sheet. Remove fine insulation hatching.
HRECT_L centerline extremes (4,8)-(44,40); envelope follows the subject's proportions.
Construction reference: No useful exact Lucide match; circular roll end and open sheet outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1ba8402d-94ce-4f80-a83a-f768e2a236d5'
SOURCE_PATH = 'pictographic-primitives/construction/material isolation_1ba8402d-94ce-4f80-a83a-f768e2a236d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unrolled-insulation-sheet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('unrolled', 'insulation', 'sheet')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('roll-top',(4,16),(20,16),8)
        line('roll-right',(20,16),(20,32))
        arc('roll-bottom-r',(20,32),(12,40),8)
        arc('roll-bottom-l',(12,40),(4,32),8)
        line('roll-left',(4,32),(4,16))
        join('roll','roll-top','roll-right','roll-bottom-r','roll-bottom-l','roll-left',closed=True)
        arc('end-top',(4,32),(20,32),8)
        connect('roll','end-top')
        path('sheet',(20,16),(44,16),(44,40),(12,40))
        connect('sheet','roll')
