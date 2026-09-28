"""A head in left-facing profile sneezing, with spray bursting from its open mouth.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the head is one open profile outline: a r11 skull dome about
(31,17) from the forehead (20,17) over the crown to the back (42,17), the
back of the head slanting into the nape and the neck down to the ground; in
front, a pointed nose, a wide-open mouth notch, the chin and jaw, and the
front of the neck. Three droplets fan out to the left of the open mouth,
each at least 8 clear of the nose, the lips and each other.
Revision: the rejected drawing's profile had no nose or open mouth and read
as a letter R beside dashes; the nose, open mouth and fanned spray now read
as a sneeze.
Human reference: `full_body_ref.png` (round skull, simple profile).
Construction reference: no useful Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f2e9b73a-cb3b-4ba3-9a35-136a976c9aec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-facing-person-sneezing/20260926T152509Z-thuan-mac-1/reference/sneeze_f2e9b73a-cb3b-4ba3-9a35-136a976c9aec.svg'
AUTHOR = "claude-opus-5-5"

SKULL, SKULL_R = (31, 17), 11
FACE = [(20, 17), (16, 21), (20, 24), (25, 28), (20, 32), (22, 36), (27, 37), (27, 42)]
BACK = [(42, 17), (38, 30), (37, 42)]
SPRAY = ((6, 23), (12, 30), (6, 37))


class Drawing(Solo48):
    icon_id = 'left-facing-person-sneezing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('sneeze',)
    keywords = ('sneeze', 'cold', 'flu', 'allergy', 'sick', 'illness', 'germs', 'head')

    def build(self):
        sx, sy = SKULL
        top = (sx, sy - SKULL_R)
        members = []
        # neck front up the face to the forehead
        pts = list(reversed(FACE))
        for i in range(len(pts) - 1):
            self.add_line(f'face-{i}', pts[i], pts[i + 1])
            members.append(f'face-{i}')
        self.add_arc('skull-front', FACE[0], top, radius_x=SKULL_R, sweep=True)
        self.add_arc('skull-back', top, BACK[0], radius_x=SKULL_R, sweep=True)
        members += ['skull-front', 'skull-back']
        self.add_line('nape', BACK[0], BACK[1])
        self.add_line('neck-back', BACK[1], BACK[2])
        members += ['nape', 'neck-back']
        self.add_contour('head', *members)
        for i, drop in enumerate(SPRAY):
            self.add_dot(f'spray-{i}', drop)
