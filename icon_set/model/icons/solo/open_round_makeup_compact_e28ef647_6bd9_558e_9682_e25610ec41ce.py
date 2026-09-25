"""Open Round Makeup Compact.

Symbol plan: Round raised mirror lid and broad oval compact tray sharing hinge. Drop nested tray ring and diagonal cosmetic divider.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: No useful exact Lucide match; full circle plus coherent elliptical tray.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e28ef647-6bd9-558e-9682-e25610ec41ce'
SOURCE_PATH = 'pictographic-primitives/beauty/mirror_e28ef647-6bd9-558e-9682-e25610ec41ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-round-makeup-compact'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('open', 'round', 'makeup', 'compact')

    def build(self) -> None:

        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        cx,cy,r=24,16,12
        pts=[(24,4),(36,16),(24,28),(12,16),(24,4)]
        for j in range(4): arc('lid-'+str(j),pts[j],pts[j+1],r)
        join('lid',*(f'lid-{j}' for j in range(4)),closed=True)
        pts=[(24,28),(40,36),(24,44),(8,36),(24,28)]
        for j in range(4): arc('tray-'+str(j),pts[j],pts[j+1],16,8)
        join('tray',*(f'tray-{j}' for j in range(4)),closed=True)
        connect('lid','tray')
