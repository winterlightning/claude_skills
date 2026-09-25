"""Overlapping Triangle and Circle.
Plan: Complete right triangle overlapping a lower-right circle, with two exact shared intersection nodes. Centerline extremes (6,6)-(42,42).
Construction: Lucide shapes: complete circle and recognizable triangular contour.
Reduction: The triangle is reconstructed as a right triangle to preserve both complete outlines without narrow pockets.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '927bb4f8-cc28-47f8-a265-f32d65fd9b37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shape triangle circle_927bb4f8-cc28-47f8-a265-f32d65fd9b37.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/shape triangle circle_927bb4f8-cc28-47f8-a265-f32d65fd9b37.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon,name,cx,cy,r):
    a,b=(cx-r,cy),(cx+r,cy)
    icon.add_arc(name+'-a',a,b,radius_x=r)
    icon.add_arc(name+'-b',b,a,radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def _box(icon,name,l,t,r,b,rad,top_nodes=()):
    xs=[l+rad]+sorted(x for x in top_nodes if l+rad<x<r-rad)+[r-rad]
    _run(icon,name+'-top',*[(x,t) for x in xs])
    icon.add_arc(name+'-tr',(r-rad,t),(r,t+rad),radius_x=rad)
    icon.add_line(name+'-right',(r,t+rad),(r,b-rad))
    icon.add_arc(name+'-br',(r,b-rad),(r-rad,b),radius_x=rad)
    icon.add_line(name+'-bottom',(r-rad,b),(l+rad,b))
    icon.add_arc(name+'-bl',(l+rad,b),(l,b-rad),radius_x=rad)
    icon.add_line(name+'-left',(l,b-rad),(l,t+rad))
    icon.add_arc(name+'-tl',(l,t+rad),(l+rad,t),radius_x=rad)
    icon.add_contour(name,*[name+f'-top-{i}' for i in range(1,len(xs))],*[name+'-'+s for s in ('tr','right','br','bottom','bl','left','tl')],closed=True)

class Drawing(Solo48):
    icon_id = 'outlined-triangle-overlapping-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('overlapping', 'triangle', 'and', 'circle')

    def build(self):
        self.add_polyline('triangle',(32,6),(32,22),(32,32),(22,32),(6,32),closed=True)
        pts=[(32,22),(42,32),(32,42),(22,32),(32,22)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'circle-{i}',a,b,radius_x=10)
        self.add_contour('circle',*[f'circle-{i}' for i in range(4)],closed=True)
        self.relate('connect','circle','triangle')
