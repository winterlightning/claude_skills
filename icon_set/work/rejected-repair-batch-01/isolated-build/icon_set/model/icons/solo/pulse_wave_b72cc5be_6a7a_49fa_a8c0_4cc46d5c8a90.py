"""Heartbeat line with a small bump, dip, tall peak and deep trough. Lucide activity informs one continuous open stroke; all waveform stages retained.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b72cc5be-6a7a-49fa-a8c0-4cc46d5c8a90'
SOURCE_PATH='pictographic-primitives/symbol/waves 1_b72cc5be-6a7a-49fa-a8c0-4cc46d5c8a90.svg'
AUTHOR='gpt-6'

class PulseWave(Solo48):
    icon_id='pulse-wave'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('pulse', 'heartbeat', 'wave', 'activity', 'health', 'signal', 'ecg', 'monitor')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('pulse',[(4,24),(10,24),(14,18),(18,30),(26,8),(34,40),(38,24),(44,24)])
