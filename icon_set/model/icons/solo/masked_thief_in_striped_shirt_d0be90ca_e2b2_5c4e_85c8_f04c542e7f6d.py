"""Masked Thief Character.

Symbol plan: Frontal circular masked head; symmetric striped shirt with one horizontal division. Head bottom20, shoulders28: exact detached ink gap4. Visible (6,2)-(42,46). Omit tiny eye slits and neckline.
Construction references: human_ref/user.svg: circular head and broad smooth shoulders; Lucide venetian-mask inspected previously for eye-band construction.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0be90ca-e2b2-5c4e-85c8-f04c542e7f6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/crime man thief_d0be90ca-e2b2-5c4e-85c8-f04c542e7f6d.svg'
AUTHOR = 'gpt-6'


class MaskedThiefInStripedShirt(Solo48):
    icon_id = 'masked-thief-in-striped-shirt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('masked', 'thief', 'in', 'striped', 'shirt')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        axis=24
        circle('head',axis,12,8)
        self.add_line('mask',(16,12),(32,12))
        self.relate('connect','head','mask')
        path('shirt',(8,36),[((24,28),16,8,True),((40,36),16,8,True),(40,44),(8,44),(8,36)],True)
        self.add_line('stripe',(8,36),(40,36))
        self.relate('connect','shirt','stripe')
