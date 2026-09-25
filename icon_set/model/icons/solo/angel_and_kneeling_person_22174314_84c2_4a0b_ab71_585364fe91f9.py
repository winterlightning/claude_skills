"""Angel and Kneeling Person.

Plan: Standing angel reaches to kneeling person. Shared human references user.svg and full_body_ref.png govern radius-4 heads and exact 8 centerline detached gaps. Wing is a broad triangular feather mass. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22174314-84c2-4a0b-ab71-585364fe91f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/feast of the annunciation_22174314-84c2-4a0b-ab71-585364fe91f9.svg'
AUTHOR = 'gpt-6'

class AngelAndKneelingPerson(Solo48):
    icon_id = 'angel-and-kneeling-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('angel', 'and', 'kneeling', 'person')

    def build(self):
        for name,x,y in [('angel',18,10),('kneeler',38,16)]:
         self.add_arc(name+'-head-r',(x,y-4),(x,y+4),radius_x=4)
         self.add_arc(name+'-head-l',(x,y+4),(x,y-4),radius_x=4)
         self.add_contour(name+'-head',name+'-head-r',name+'-head-l',closed=True)
        self.add_line('angel-torso',(18,22),(18,34))
        self.add_polyline('angel-legs',(14,42),(18,34),(22,42))
        self.add_line('angel-arm',(18,22),(26,26))
        self.add_polyline('wing',(6,22),(18,34),(6,34),closed=True)
        for p in ['angel-legs','angel-arm','wing']:self.relate('connect','angel-torso',p)
        self.add_line('kneeler-torso',(38,28),(38,34))
        self.add_polyline('kneeling-legs',(38,34),(30,34),(30,42),(42,42))
        self.relate('connect','kneeler-torso','kneeling-legs')
        self.mark_human_figure('angel',head='angel-head',torso='angel-torso',torso_junction='start')
        self.mark_human_figure('kneeler',head='kneeler-head',torso='kneeler-torso',torso_junction='start')
