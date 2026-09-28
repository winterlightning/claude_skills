"""06-male-and-female-restroom-sign--4366c5ae-436d-4c86-a02e-a01fcc4972ae
Plan: Two equal standing figures at x=10 and x=38, with a central divider. Head radius 4 at y=12; upper torso starts at y=24. Centerline extremes (4,8)-(44,40).
Construction: Human full_body_ref.png: equal circular heads, simple tunics and limbs.
Reduction: Tunic outlines reduced to the shared human stick-figure vocabulary to keep two figures and their divider readable; no gender distinctions invented.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4366c5ae-436d-4c86-a02e-a01fcc4972ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__restroom-pair-batch-071/20260927T171300Z-thuan-mac-1/reference/toilet sign 2_4366c5ae-436d-4c86-a02e-a01fcc4972ae.svg'
AUTHOR = "gpt-6"

def _path(icon, name, start, steps, closed=False):
    members=[]
    for i, step in enumerate(steps):
        end=step[0]; member=f'{name}-{i}'
        if len(step)==1: icon.add_line(member,start,end)
        else: icon.add_arc(member,start,end,radius_x=step[1],radius_y=step[2],sweep=step[3])
        members.append(member); start=end
    icon.add_contour(name,*members,closed=closed)


def _circle(icon,name,x,y,r):
    _path(icon,name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)


class Batch071Icon06(Solo48):
    icon_id = 'restroom-pair-batch-071'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('restroom', 'pair')

    def build(self):
        # Paired skirt silhouettes from the reference, split by a central guide.
        for i,x in enumerate((10,38)):
            _circle(self,f'head-{i}',x,12,4)
            self.add_polyline(f'dress-{i}',(x-4,24),(x+4,24),(x+6,36),(x-6,36),closed=True)
            self.add_line(f'leg-left-{i}',(x-4,36),(x-4,40))
            self.add_line(f'leg-right-{i}',(x+4,36),(x+4,40))
            self.relate('connect',f'dress-{i}',f'leg-left-{i}',f'leg-right-{i}')
        self.add_line('divider',(24,8),(24,40))
