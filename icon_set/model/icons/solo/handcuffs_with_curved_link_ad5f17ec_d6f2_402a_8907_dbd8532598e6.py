"""Pair of Handcuffs.

Symbol plan: Diagonal equal cuffs, joined by a curved loose link. Visible (4,4)-(44,44). Omit concentric rims, joint hatches and lock blocks.
Construction references: Lucide spline: curved linkage ending on circular objects.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad5f17ec-d6f2-402a-8907-dbd8532598e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg'
AUTHOR = 'gpt-6'


class HandcuffsWithCurvedLink(Solo48):
    icon_id = 'handcuffs-with-curved-link'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('handcuffs', 'with', 'curved', 'link')

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

        circle('cuff-left',14,34,8)
        circle('cuff-right',34,14,8)
        path('link',(14,26),[(14,14),((26,14),6,6,True)])
        self.relate('connect','link','cuff-left')
        self.relate('connect','link','cuff-right')
