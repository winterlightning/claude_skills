"""Pair of Handcuffs.

Symbol plan: Diagonal equal cuffs, joined by a curved loose link. Visible (4,4)-(44,44). Omit concentric rims, joint hatches and lock blocks.
Construction references: Lucide spline: curved linkage ending on circular objects.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ad5f17ec-d6f2-402a-8907-dbd8532598e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260927T075459Z-thuan-mac-1/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg'
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
        # The original has a long sweeping strap over the upper left cuff.
        self.add_bezier('link',(14,26),((12,22),(10,20),(10,16)),((10,10),(14,8),(19,8)),((23,8),(25,11),(26,14)))
        self.relate('connect','link','cuff-left')
        self.relate('connect','link','cuff-right')
