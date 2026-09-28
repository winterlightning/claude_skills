"""Bound and Blindfolded Woman.

Symbol plan: Circular blindfolded head; broad detached shoulder/binding outline. Head bottom=26; body top=34, exact 4 ink gap. Visible (4,4)-(44,44). Omit mouth and rope hatching.
Construction references: human_ref/user.svg: circular head and broad shoulders; human_ref/full_body_ref.png: simplified anatomy.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e64fd8f9-3929-4c88-98ad-7278fe105998'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/kidnapping woman_e64fd8f9-3929-4c88-98ad-7278fe105998.svg'
AUTHOR = 'gpt-6'


class BoundBlindfoldedWoman(Solo48):
    icon_id = 'bound-blindfolded-woman'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('bound', 'blindfolded', 'woman')

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
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        axis, head_y, radius = 24, 16, 10
        circle('head',axis,head_y,radius)
        self.add_line('blindfold',(axis-radius,head_y),(axis+radius,head_y))
        self.relate('connect','head','blindfold')
        for side in (-1,1):
         self.add_line(f'hair-{side}',(24+side*10,16),(24+side*18,26))
         self.relate('connect',f'hair-{side}','head')
         self.relate('connect',f'hair-{side}','blindfold')
        path('binding',(6,42), [((16,34),10,8,True),(26,34),(32,34),((42,42),10,8,True),(18,42),(6,42)],True)
        self.add_line('binding-division',(18,42),(26,34))
        self.relate('connect','binding','binding-division')
