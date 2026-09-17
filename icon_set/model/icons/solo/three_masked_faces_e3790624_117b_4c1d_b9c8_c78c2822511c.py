"""Group of Masked Criminals.

Symbol plan: Three equal circular faces in triangular layout with one mask bar per face. Radius=7, centers (24,15),(11,33),(37,33). Visible (2,6)-(46,42). Omit mouths and mask contour detail.
Construction references: human_ref/user.svg: circular face construction; Lucide venetian-mask: eye-band silhouette.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3790624-117b-4c1d-b9c8-c78c2822511c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/organized crime_e3790624-117b-4c1d-b9c8-c78c2822511c.svg'
AUTHOR = 'gpt-6'


class ThreeMaskedFaces(Solo48):
    icon_id = 'three-masked-faces'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('three', 'masked', 'faces')

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

        for j,(x,y) in enumerate(((24,15),(11,33),(37,33))):
         circle(f'face-{j}',x,y,7)
         path(f'mask-{j}',(x-7,y), [((x,y),4,3,False),((x+7,y),4,3,False)])
         self.relate('connect',f'face-{j}',f'mask-{j}')
