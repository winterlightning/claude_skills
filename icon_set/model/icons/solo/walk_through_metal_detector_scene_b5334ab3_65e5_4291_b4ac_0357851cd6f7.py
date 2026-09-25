"""VRECT_L centerline bounds (8,4)-(40,44). Rounded detector portal, attached overhead control and centered person. The head ends at y27 and the torso begins at y35, giving exactly 4 units of visible clearance. External beep rays and sleeve notches are omitted to preserve a readable 48-unit scene.

Construction reference: Shared human_ref/full_body_ref.png; round detached heads and simplified bodies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5334ab3-65e5-4291-b4ac-0357851cd6f7'
SOURCE_PATH = 'pictographic-primitives/travel/security officer scanner beep_b5334ab3-65e5-4291-b4ac-0357851cd6f7.svg'
SOURCE_ICON_IDS = ('b5334ab3-65e5-4291-b4ac-0357851cd6f7',)
AUTHOR = 'gpt-6'

def circle(m, name, cx, cy, r):
    # A single circular loop owns its radius and shared antipodal endpoints.
    m.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
    m.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
    m.add_contour(name,name+"-top",name+"-bottom",closed=True)


def rounded(m, name, left, top, right, bottom, r):
    # One rectangle owns all four equal tangent quarter-circle corners.
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
            (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    for i,start in enumerate(points):
        end=points[(i+1)%8]
        if i%2: m.add_arc(f"{name}-{i}",start,end,radius_x=r)
        else: m.add_line(f"{name}-{i}",start,end)
    m.add_contour(name,*(f"{name}-{i}" for i in range(8)),closed=True)


class WalkThroughMetalDetectorScene(Solo48):
    icon_id = 'walk-through-metal-detector-scene'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('walk', 'through', 'metal', 'detector', 'scene')

    def build(self) -> None:
        # VRECT_L centerline bounds (8,4)-(40,44). The overhead control
        # remains; peripheral beep rays are omitted to keep the person clear.
        self.add_line('left-wall',(8,44),(8,18))
        self.add_arc('left-corner',(8,18),(14,12),radius_x=6)
        self.add_line('lintel',(14,12),(34,12))
        self.add_arc('right-corner',(34,12),(40,18),radius_x=6)
        self.add_line('right-wall',(40,18),(40,44))
        self.add_contour('arch','left-wall','left-corner','lintel','right-corner','right-wall')
        self.add_polyline('control',(20,12),(20,4),(28,4),(28,12))
        self.relate('connect','arch','control')
        circle(self,'head',24,24,3)
        # Head bottom28, shoulder centerline36: exact four-unit ink gap.
        self.add_bezier('shoulders',(18,38),((18,35),(20,35),(24,35)),((28,35),(30,35),(30,38)))
        self.add_polyline('torso',(30,38),(28,44),(20,44),(18,38))
        self.add_contour('person','shoulders','torso-1','torso-2','torso-3',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='torso']
