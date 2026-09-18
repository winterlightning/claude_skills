"""06-male-and-female-restroom-sign--4366c5ae-436d-4c86-a02e-a01fcc4972ae
Plan: Two equal standing figures at x=10 and x=38, with a central divider. Head radius 4 at y=12; upper torso starts at y=24. Centerline extremes (4,8)-(44,40).
Construction: Human full_body_ref.png: equal circular heads, simple tunics and limbs.
Reduction: Tunic outlines reduced to the shared human stick-figure vocabulary to keep two figures and their divider readable; no gender distinctions invented.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4366c5ae-436d-4c86-a02e-a01fcc4972ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toilet sign 2_4366c5ae-436d-4c86-a02e-a01fcc4972ae.svg'
AUTHOR = 'gpt-6'

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
    category = "objects"
    aliases = ()
    keywords = ('restroom', 'pair')

    def build(self):
        # Human reference: full_body_ref.png. Head bottom 16, neck 24: exact ink gap 4.
        for i,x in enumerate((10,38)):
            _circle(self,f'head-{i}',x,12,4)
            self.add_line(f'torso-{i}',(x,24),(x,32))
            self.add_polyline(f'arms-{i}',(x-6,24),(x,24),(x+6,24))
            self.add_polyline(f'legs-{i}',(x-4,40),(x,32),(x+4,40))
            self.relate('connect',f'torso-{i}',f'arms-{i}');self.relate('connect',f'torso-{i}',f'legs-{i}')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
        self.add_line('divider',(24,8),(24,40))
