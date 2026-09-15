"""Trapezoid shell and diagonal pendulum with a small round pivot. Pendulum genuinely crosses the case edge; omit the vertical tempo scale. Centerline extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1679c2d5-89c6-5c60-885b-80f3248fbeca'
SOURCE_PATH='pictographic-primitives/music/music metronome_1679c2d5-89c6-5c60-885b-80f3248fbeca.svg'
AUTHOR='gpt-6'

class Metronome(Solo48):
    icon_id='metronome'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('metronome', 'tempo', 'rhythm', 'beat', 'timing', 'practice', 'music')

    def build(self):
        self.add_polyline('case',(8,44),(18,4),(24,4),(40,44),closed=True)
        cx,cy,rx,ry=24,33,2,2
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'pivot-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('pivot',*[f'pivot-{n}' for n in range(4)],closed=True)
        self.add_line('pendulum',(24,31),(40,15))
        self.relate('connect','pendulum','pivot')
        self.relate('occlude','pendulum','case')
