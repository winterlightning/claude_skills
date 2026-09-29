"""Enlarge the head, separate the upright rider and reaching arm, show a hanging bent leg, and open the craft silhouette around that leg.
Construction plan: Head (24,10), r4; neck (24,22) gives exact 4 ink gap. Upright upper torso bends into a seated hip; bow faces left. Hull is interrupted behind the hanging leg. Square intended extremes (6,6)-(42,42).
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected rider has a tiny head and the bent body merges with the hull into a mound; the seated leg is no longer clear.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '959341bb-93a4-4207-a514-99f7bd37b9b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-jet-ski-rider/20260929T084652Z-thuan-mac/reference/sport jet skiing_959341bb-93a4-4207-a514-99f7bd37b9b4.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'seated-jet-ski-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('seated', 'jet', 'ski', 'rider')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.circle('head',24,10,4)
        self.add_line('torso',(24,22),(24,25))
        self.add_bezier('back',(24,25),((24,27),(30,28),(30,30)))
        self.add_polyline('leg',(30,30),(24,30),(27,37))
        self.add_polyline('arm',(24,22),(19,28),(13,28))
        self.add_bezier('bow',(13,28),((10,28),(6,32),(6,34)),((6,36),(8,37),(10,37)))
        self.add_line('front-hull',(10,37),(18,37))
        self.add_line('seat',(30,30),(36,30))
        self.add_bezier('stern',(36,30),((40,30),(42,33),(42,35)),((40,36),(37,36),(34,36)))
        self.add_bezier('water',(6,44),((12,42),(18,42),(24,44)),((30,42),(36,42),(42,44)))
        for a,b in [('torso','back'),('back','leg'),('torso','arm'),('arm','bow'),('bow','front-hull'),('leg','seat'),('seat','stern')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

