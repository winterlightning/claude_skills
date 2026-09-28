"""Elastic compute cloud instances: three identical rounded squares stacked diagonally, each hidden behind the next.

Plan: SQUARE. Three 20x20 rounded squares (r3) offset by 8 on both axes: back (6,6)-(26,26), middle (14,14)-(34,34), front (22,22)-(42,42). The back and middle squares are drawn only where they are not occluded, and their cut ends land on nodes of the square in front (Lucide `copy` construction). Every edge and corner arc is a standalone primitive joined by connect so the exact 8-unit parallel gaps certify.
Review of the rejected drawing: the two back squares were drawn as bare L brackets floating away from the front square, so the stack read as brackets around a box instead of three overlapping instances, and the front square was only 18 wide.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6c211c96-838c-47b8-8fce-5a2678d829d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__elastic-compute-cloud-instances/20260928T042731Z-thuan-mac-1/reference/elastic compute cloud instances_6c211c96-838c-47b8-8fce-5a2678d829d5.svg'
AUTHOR = "claude-fable-5-1"


class ElasticComputeCloudInstances(Solo48):
    icon_id = 'elastic-compute-cloud-instances'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ('ec2-instances', 'stacked-instances')
    keywords = ('elastic', 'compute', 'cloud', 'instances', 'programing', 'servers', 'stack')

    def build(self) -> None:
        R = 3
        prev = None

        def carc(name, s, e, c):
            cross = (s[0]-c[0])*(e[1]-c[1]) - (s[1]-c[1])*(e[0]-c[0])
            self.add_arc(name, s, e, radius_x=R, sweep=cross > 0)

        def chain(name, pts):
            """pts: list of ('L', p) or ('A', p, centre); consecutive standalone members joined by connect."""
            here = pts[0][1]
            ids = []
            for i, step in enumerate(pts[1:]):
                eid = f'{name}-{i}'
                if step[0] == 'L':
                    self.add_line(eid, here, step[1])
                else:
                    carc(eid, here, step[1], step[2])
                if ids:
                    self.relate('connect', ids[-1], eid)
                ids.append(eid)
                here = step[1]
            return ids

        # front square, full outline
        f = chain('front', [('L', (25, 22)), ('L', (34, 22)), ('L', (39, 22)), ('A', (42, 25), (39, 25)),
                            ('L', (42, 39)), ('A', (39, 42), (39, 39)), ('L', (25, 42)), ('A', (22, 39), (25, 39)),
                            ('L', (22, 34)), ('L', (22, 25)), ('A', (25, 22), (25, 25))])
        self.relate('connect', f[-1], f[0])
        # middle square: visible run from the front's left edge round the top-left to the front's top edge
        m = chain('middle', [('L', (22, 34)), ('L', (17, 34)), ('A', (14, 31), (17, 31)), ('L', (14, 26)), ('L', (14, 17)),
                             ('A', (17, 14), (17, 17)), ('L', (26, 14)), ('L', (31, 14)), ('A', (34, 17), (31, 17)), ('L', (34, 22))])
        self.relate('connect', m[0], 'front-8')
        self.relate('connect', m[0], 'front-9')
        self.relate('connect', m[-1], 'front-1')
        self.relate('connect', m[-1], 'front-2')
        # back square: visible run from the middle's left edge round the top-left to the middle's top edge
        b = chain('back', [('L', (14, 26)), ('L', (9, 26)), ('A', (6, 23), (9, 23)), ('L', (6, 9)),
                           ('A', (9, 6), (9, 9)), ('L', (23, 6)), ('A', (26, 9), (23, 9)), ('L', (26, 14))])
        self.relate('connect', b[0], 'middle-3')
        self.relate('connect', b[0], 'middle-4')
        self.relate('connect', b[-1], 'middle-6')
        self.relate('connect', b[-1], 'middle-7')
