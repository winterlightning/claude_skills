"""Playroom house with a doorway and a round-headed pawn toy.
Plan: SQUARE fits the roof, doorway and foreground toy.
Reduction: Roof made shallower; right wall occluded by toy; stacked toy body simplified to a broad triangular base beneath its circular knob.
Construction: house: coherent roof/wall and doorway construction. Toy identified from the supplied source, not treated as a human figure. Intentional foreground occlusion.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6ecc684-688c-443b-ae9b-74c5652fb4fa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/playroom_c6ecc684-688c-443b-ae9b-74c5652fb4fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'playroom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('playroom',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        # Foreground pawn toy has a round knob, short connector and a broad base.
        self.add_polyline('house',(42,16),(24,6),(6,16),(6,42),(14,42),(22,42),(30,42))
        self.add_polyline('door',(14,42),(14,29),(22,29),(22,42));self.relate('connect','door','house')
        self.circle('toy-knob',36,26,3)
        self.add_line('toy-neck',(36,29),(36,32));self.relate('connect','toy-neck','toy-knob')
        self.add_polyline('toy-base',(36,32),(42,42),(30,42),closed=True)
        self.relate('connect','toy-neck','toy-base');self.relate('connect','toy-base','house')

    def circle(self, name, cx, cy, r):
        points = [(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members = []
        for i, (a,b) in enumerate(zip(points, points[1:])):
            member = f"{name}-{i}"
            self.add_arc(member, a, b, radius_x=r)
            members.append(member)
        self.add_contour(name, *members, closed=True)

    def rounded(self, name, left, top, right, bottom, r):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r),(left+r,top)]
        members = []
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member = f"{name}-{i}"
            if i % 2: self.add_arc(member,a,b,radius_x=r)
            else: self.add_line(member,a,b)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def plug(self, cx=24, top=21, bottom=32):
        # Shared bowl width and mirrored prongs; cable joins bottom apex.
        r=8
        self.add_polyline('plug-top',(cx-r,top),(cx-4,top),(cx+4,top),(cx+r,top))
        self.add_line('plug-right',(cx+r,top),(cx+r,bottom-r))
        self.add_arc('plug-right-curve',(cx+r,bottom-r),(cx,bottom),radius_x=r)
        self.add_arc('plug-left-curve',(cx,bottom),(cx-r,bottom-r),radius_x=r)
        self.add_line('plug-left',(cx-r,bottom-r),(cx-r,top))
        self.add_contour('plug-bowl','plug-right','plug-right-curve','plug-left-curve','plug-left')
        self.relate('connect','plug-top','plug-bowl')
        for i,x in enumerate((cx-4,cx+4)):
            self.add_line(f'prong-{i}',(x,top-8),(x,top))
            self.relate('connect',f'prong-{i}','plug-top')
