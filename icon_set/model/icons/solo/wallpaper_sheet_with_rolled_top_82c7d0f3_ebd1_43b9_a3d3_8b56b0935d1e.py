"""Wallpaper Sheet with Rolled Top.
Plan: A horizontal rolled edge owns two rounded ends and a hanging rectangular sheet. Right end is a full circular curl. Bounds (6,6)-(42,42).
References: Lucide scroll: rolled edge and sheet joined at clear nodes.
Reduction: Fine roll thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '82c7d0f3-ebd1-43b9-a3d3-8b56b0935d1e'
SOURCE_PATH = 'pictographic-primitives/construction/wallpaper_82c7d0f3-ebd1-43b9-a3d3-8b56b0935d1e.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


def symmetric(icon, name, start, left_steps, axis=24):
    """One half owns the whole outline; reflect and reverse its traversal."""
    flip = lambda p: (2*axis-p[0], p[1])
    prior = start
    reverse = []
    for kind, end, *args in left_steps:
        if kind == 'B':
            reverse.append((kind, flip(prior), flip(args[1]), flip(args[0])))
        else:
            reverse.append((kind, flip(prior), *args))
        prior = end
    path(icon, name, start, *left_steps, *reversed(reverse), closed=True)


class WallpaperSheetWithRolledTop(Solo48):
    icon_id = 'wallpaper-sheet-with-rolled-top'
    keyshape = Keyshape.SQUARE
    category = 'construction'
    categories = ('construction', 'primitives')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('wallpaper', 'sheet', 'with', 'rolled', 'top')

    def build(self):
        path(self,'roll',(12,6),('L',(36,6)),('A',(42,12),6,6,True),('A',(36,18),6,6,True),('L',(12,18)),('A',(6,12),6,6,True),('A',(12,6),6,6,True),closed=True)
        path(self,'curl',(36,6),('A',(30,12),6,6,False),('A',(36,18),6,6,False))
        self.add_polyline('sheet',(12,18),(12,42),(42,42),(42,12))
        self.relate('connect','roll','curl')
        self.relate('connect','roll','sheet')
