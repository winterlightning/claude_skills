"""Two Pointed Trees beneath Cloud.

Symbol plan: Two pointed trees of different heights under a small cloud. Keep the smaller rear crown; omit its tiny trunk and the ground line.
SQUARE centerline extremes (6,6)-(42,42); envelope follows the subject's proportions.
Construction reference: Lucide cloud: coherent cloud contour. Source supplies unequal pointed trees.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '53180ae8-932a-42c6-9ffa-67a1bc8e3eb8'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture cloud_53180ae8-932a-42c6-9ffa-67a1bc8e3eb8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-pointed-trees-beneath-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('two', 'pointed', 'trees', 'beneath', 'cloud')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('tree-front',(6,34),(14,6),(22,34),(14,34),(6,34),closed=True)
        # A smaller independent rear crown sits to the right.
        path('tree-back',(30,38),(36,27),(42,38),(30,38),closed=True)
        line('trunk-front',(14,34),(14,42));connect('tree-front','trunk-front')

        arc('cloud-top',(30,12),(42,12),6)
        arc('cloud-right',(42,12),(36,18),6)
        line('cloud-base',(36,18),(30,18))
        arc('cloud-left',(30,18),(30,12),3)
        join('cloud','cloud-top','cloud-right','cloud-base','cloud-left',closed=True)
