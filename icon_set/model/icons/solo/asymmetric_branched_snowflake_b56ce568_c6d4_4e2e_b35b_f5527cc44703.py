from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b56ce568-c6d4-4e2e-b35b-f5527cc44703'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/temperature snowflake_b56ce568-c6d4-4e2e-b35b-f5527cc44703.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'asymmetric-branched-snowflake'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('temperature snowflake',)
    # Plan: Six crystalline arms with a fork on every arm, shared center and mirrored branch definitions.
    # Construction references: Lucide snowflake: sixfold branching.
    # Omissions: Fine secondary ice twigs omitted.
    def build(self):
        # Six rays, each split at its fork node; all actual endpoint junctions declared.
        center=(24,24)
        rays=[((24,14),(24,6),[(16,6),(32,6)]),((24,34),(24,42),[(16,42),(32,42)]),
              ((14,18),(6,14),[(6,22),(14,10)]),((34,18),(42,14),[(42,22),(34,10)]),
              ((14,30),(6,34),[(6,26),(14,38)]),((34,30),(42,34),[(42,26),(34,38)])]
        roots=[]
        for i,(node,end,twigs) in enumerate(rays):
            root=f'ray-{i}'
            self.add_line(root,center,node);roots.append(root)
            branches=[]
            for j,p in enumerate([end,*twigs]):
                name=f'fork-{i}-{j}';self.add_line(name,node,p);branches.append(name)
            for a in [root,*branches]:
                for b in [root,*branches]:
                    if a<b:self.relate('connect',a,b)
        for a in roots:
            for b in roots:
                if a<b:self.relate('connect',a,b)

    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
