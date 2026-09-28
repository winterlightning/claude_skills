"""Curved Modern Tower.

Symbol plan: Asymmetric sail-shaped tower with circular sweeping facade and one floor tick. Retain curved left face and straight right edge.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide building-2: sparse floor details. Source supplies distinctive curved silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ab5d3316-275a-593a-983a-04ff4dc8fd2d'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture building_ab5d3316-275a-593a-983a-04ff4dc8fd2d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-modern-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('curved', 'modern', 'tower')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('facade',(8,36),(40,4),32)
        line('walls-1',(40,4),(40,44))
        line('walls-2',(40,44),(8,44))
        line('walls-3',(8,44),(8,36))
        join('outline','facade','walls-1','walls-2','walls-3',closed=True)
        for j,(x,y) in enumerate(((8,36),)):
            line('floor-'+str(j),(x,y),(24,y))
            connect('floor-'+str(j),'outline')
