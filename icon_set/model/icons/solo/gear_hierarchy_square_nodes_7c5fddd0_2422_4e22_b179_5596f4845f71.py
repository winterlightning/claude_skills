"""A six-lobed gear branches to three square nodes. The central ring and dot are omitted to preserve room for the square leaves. Lucide network informs the equal nodes and shared bus. Bilateral symmetry.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7c5fddd0-2422-4e22-b179-5596f4845f71'
SOURCE_PATH='pictographic-primitives/programing/obs works_7c5fddd0-2422-4e22-b179-5596f4845f71.svg'
AUTHOR = 'gpt-6'

class GearHierarchySquareNodes(Solo48):
    icon_id='gear-hierarchy-square-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('gear', 'hierarchy', 'tree', 'settings', 'operations', 'nodes', 'workflow', 'structure')

    def build(self):
        # Plan: Keep the gear and all three equal square child nodes; arrange the children around two sides to give the branches room instead of compressing a horizontal bus.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('gear',(14,6),(17,9),(22,10),(20,14),(22,18),(17,19),(14,22),(11,19),(6,18),(8,14),(6,10),(11,9),closed=True)
        poly('upper-node',(34,6),(42,6),(42,14),(34,14),(34,10),closed=True)
        poly('left-node',(6,34),(10,34),(14,34),(14,42),(6,42),closed=True)
        poly('right-node',(34,34),(38,34),(42,34),(42,42),(34,42),closed=True)
        line('upper-link',(22,10),(34,10));line('left-link',(14,22),(10,34));line('right-link',(14,22),(34,42))
        for link,node in [('upper-link','upper-node'),('left-link','left-node'),('right-link','right-node')]:join(link,'gear');join(link,node)
        join('left-link','right-link')
