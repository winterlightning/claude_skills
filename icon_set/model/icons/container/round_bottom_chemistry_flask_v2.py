"""Widen the round bulb and shorten the neck while retaining the flask silhouette.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class RoundBottomChemistryFlaskVariant2(Container64):
    icon_id = 'round-bottom-chemistry-flask-v2'
    variant_of = 'round-bottom-chemistry-flask'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'vessel',(24,2),[('L',(24,12)),('A',(6,36),18,24,False),('A',(58,36),26,26,False),('A',(40,12),18,24,False),('L',(40,2))])
        line('rim',(20,2),(44,2));join('rim','vessel')
