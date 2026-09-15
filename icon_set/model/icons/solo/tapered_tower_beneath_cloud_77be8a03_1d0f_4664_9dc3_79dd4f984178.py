"""Tapered Tower beneath Cloud.

Symbol plan: Tapered tower and separate cloud; one broad facade band. Omit crowded outer fins.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide cloud: rounded connected lobes; building-2: sparse facade articulation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '77be8a03-1d0f-4664-9dc3-79dd4f984178'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture high cloud building_77be8a03-1d0f-4664-9dc3-79dd4f984178.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-tower-beneath-cloud'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('tapered', 'tower', 'beneath', 'cloud')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('tower',(8,44),(10,34),(16,4),(22,34),(24,44),(8,44),closed=True)
        line('floor',(10,34),(22,34));connect('tower','floor')
        arc('cloud-top',(30,9),(40,9),5)
        arc('cloud-right',(40,9),(34,15),6)
        line('cloud-base',(34,15),(30,15))
        arc('cloud-left',(30,15),(30,9),3)
        join('cloud','cloud-top','cloud-right','cloud-base','cloud-left',closed=True)
