"""Six-tooth settings gear with round centre hole. Lucide settings informs alternating convex teeth and concave valleys; vertical and horizontal reflections share dimensions.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='95406251-8b85-440b-813a-359dd10112c9'
SOURCE_PATH='pictographic-primitives/symbol/state setting_95406251-8b85-440b-813a-359dd10112c9.svg'
AUTHOR='gpt-6'

class GearSettings(Solo48):
    icon_id='gear-settings'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('gear', 'settings', 'cog', 'preferences', 'configuration', 'options', 'system', 'tools')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.add_line('top',(20,6),(28,6))
        self.add_arc('tr',(28,6),(30,8),radius_x=2)
        self.add_arc('upper-valley-r',(30,8),(36,12),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('upper-tooth-r',(36,12),(42,20),radius_x=6,radius_y=8)
        self.add_arc('middle-valley-r',(42,20),(42,28),radius_x=4,sweep=False)
        self.add_arc('lower-tooth-r',(42,28),(36,36),radius_x=6,radius_y=8)
        self.add_arc('lower-valley-r',(36,36),(30,40),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('br',(30,40),(28,42),radius_x=2)
        self.add_line('bottom',(28,42),(20,42))
        self.add_arc('bl',(20,42),(18,40),radius_x=2)
        self.add_arc('lower-valley-l',(18,40),(12,36),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('lower-tooth-l',(12,36),(6,28),radius_x=6,radius_y=8)
        self.add_arc('middle-valley-l',(6,28),(6,20),radius_x=4,sweep=False)
        self.add_arc('upper-tooth-l',(6,20),(12,12),radius_x=6,radius_y=8)
        self.add_arc('upper-valley-l',(12,12),(18,8),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('tl',(18,8),(20,6),radius_x=2)
        self.add_contour('gear','top','tr','upper-valley-r','upper-tooth-r','middle-valley-r','lower-tooth-r','lower-valley-r','br','bottom','bl','lower-valley-l','lower-tooth-l','middle-valley-l','upper-tooth-l','upper-valley-l','tl',closed=True)
        self.oval('hub',24,24,5)
