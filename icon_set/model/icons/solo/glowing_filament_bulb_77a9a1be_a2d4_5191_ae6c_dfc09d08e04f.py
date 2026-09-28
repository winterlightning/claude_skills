"""A glowing bulb contains a Y filament and three rays. Lucide lightbulb informs the rounded glass and taper. Two side rays are omitted to widen the glass; the socket is integrated with the outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77a9a1be-a2d4-5191-ae6c-dfc09d08e04f'
SOURCE_PATH = 'pictographic-primitives/school-learning/study light idea_77a9a1be-a2d4-5191-ae6c-dfc09d08e04f.svg'
AUTHOR = 'gpt-6'


class GlowingFilamentBulb(Solo48):
    icon_id = 'glowing-filament-bulb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "other", "primitives-generate")
    aliases = ()
    keywords = ('bulb', 'filament', 'light', 'idea', 'lamp', 'glow')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+'-'+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Live centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40.

        self.add_arc('dome-left',(12,28),(24,16),radius_x=12)
        self.add_arc('dome-right',(24,16),(36,28),radius_x=12)
        self.add_arc('taper-right',(36,28),(32,36),radius_x=10)
        self.run('socket',(32,36),(32,42),(24,42),(16,42),(16,36))
        self.add_arc('taper-left',(16,36),(12,28),radius_x=10)
        self.add_contour('bulb','dome-left','dome-right','taper-right','socket-1','socket-2','socket-3','socket-4','taper-left',closed=True)
        self.add_line('filament-stem',(24,42),(24,30))
        self.add_polyline('filament-fork',(21,27),(24,30),(27,27))
        self.relate('connect','bulb','filament-stem')
        self.relate('connect','filament-stem','filament-fork')
        self.add_line('ray-top',(24,6),(24,7))
        self.add_line('ray-ul',(6,11),(8,13))
        self.add_line('ray-ur',(40,13),(42,11))
