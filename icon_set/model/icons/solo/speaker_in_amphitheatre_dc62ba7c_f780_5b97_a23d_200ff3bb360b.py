"""A speaker stands above curved amphitheatre seating."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='dc62ba7c-f780-5b97-a23d-200ff3bb360b'
SOURCE_PATH='pictographic-primitives/office/presentation amphitheater_dc62ba7c-f780-5b97-a23d-200ff3bb360b.svg'
AUTHOR='gpt-6'

class SpeakerInAmphitheatre(Solo48):
    icon_id='speaker-in-amphitheatre'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('speaker', 'amphitheatre', 'presentation', 'person', 'auditorium', 'office')

    def build(self):
        # Plan: A speaker stands above curved amphitheatre seating. Centerline extremes (6,6)-(42,42).
        # Reduction: Simplify torso and seating tiers to broad clear curves.
        # Reference: human_ref/user.svg and full_body_ref.png: round head, broad shoulders, exact detached gap.
        # All contacts below are physical joints sharing exact endpoints.
        endpoints = {}
        def line(name, a, b):
            self.add_line(name, a, b)
            endpoints[name] = (a, b)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
            endpoints[name] = tuple(points)
        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
            endpoints[name] = (a, b)
        def join_contacts():
            names = list(endpoints)
            for i, a in enumerate(names):
                for b in names[i+1:]:
                    if set(endpoints[a]) & set(endpoints[b]):
                        self.relate("connect", a, b)
        def circle(name,cx,cy,r):
            arc(name+'-top',(cx-r,cy),(cx,cy-r),r)
            arc(name+'-right',(cx,cy-r),(cx+r,cy),r)
            arc(name+'-bottom',(cx+r,cy),(cx,cy+r),r)
            arc(name+'-left',(cx,cy+r),(cx-r,cy),r)
            self.add_contour(name,*(name+s for s in ['-top','-right','-bottom','-left']),closed=True)
        # Human refs: user.svg and full_body_ref.png. Head bottom=12, shoulder apex=20: ink gap 4.
        circle('head',24,9,3)
        arc('shoulders',(18,24),(30,24),6,4)
        # Two broad seating tiers widen toward the viewer.
        arc('tier-inner',(10,29),(38,29),14,4,sweep=False)
        arc('tier-outer',(6,37),(42,37),18,5,sweep=False)
        join_contacts()
