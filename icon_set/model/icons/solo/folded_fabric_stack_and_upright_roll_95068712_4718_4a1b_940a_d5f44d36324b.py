"""Folded Fabric Stack and Upright Roll.

Symbol plan: Two repeated horizontal folded layers and one upright roll; shared stack endpoints. Reduce three layers to two.
SQUARE centerline extremes (6,6)-(42,42); envelope follows the subject's proportions.
Construction reference: No useful exact Lucide match; capsule-like fabric folds and shared layer construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '95068712-4718-4a1b-940a-d5f44d36324b'
SOURCE_PATH = 'pictographic-primitives/construction/material fabric_95068712-4718-4a1b-940a-d5f44d36324b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folded-fabric-stack-and-upright-roll'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('folded', 'fabric', 'stack', 'and', 'upright', 'roll')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        # Upright roll has a rounded crown and a flat cut end; every fold joins a wall node.
        line('roll-top',(34,6),(38,6))
        arc('roll-tr',(38,6),(42,10),4)
        path('roll-wall',(42,10),(42,42),(30,42),(30,26),(30,10))
        arc('roll-tl',(30,10),(34,6),4)
        connect('roll-top','roll-tr');connect('roll-tr','roll-wall')
        connect('roll-wall','roll-tl');connect('roll-tl','roll-top')
        line('upper',(30,10),(14,10))
        arc('fold-top',(14,10),(14,26),8,s=False)
        line('middle',(14,26),(30,26))
        join('upper-layer','upper','fold-top','middle')
        arc('fold-bottom',(14,26),(14,42),8,s=False)
        line('lower',(14,42),(30,42))
        join('lower-layer','fold-bottom','lower')
        connect('upper-layer','lower-layer')
        connect('upper-layer','roll-wall');connect('upper-layer','roll-tl')
        connect('lower-layer','roll-wall')
