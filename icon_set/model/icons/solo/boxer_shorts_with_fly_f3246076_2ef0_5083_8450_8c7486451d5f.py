"""Boxer Shorts with Fly.

Plan: Broad boxer shorts with waistband, central fly and a smooth U crotch. Mirrored leg hems share parameters. Bounds (4,8)-(44,40).
Construction references: Lucide shirt: one continuous garment boundary and attached seams.
Simplification: Tiny seam stitching omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3246076-2ef0-5083-8450-8c7486451d5f'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear boxers_f3246076-2ef0-5083-8450-8c7486451d5f.svg'
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


class BoxerShortsWithFly(Solo48):
    icon_id = 'boxer-shorts-with-fly'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('boxer', 'shorts', 'with', 'fly')

    def build(self):
        path(self,'outline',(8,8),('L',(40,8)),('L',(41,16)),('L',(44,40)),('L',(30,40)),('L',(28,34)),('A',(20,34),4,4,False),('L',(18,40)),('L',(4,40)),('L',(7,16)),('L',(8,8)),closed=True)
        self.add_polyline('waistband',(7,16),(24,16),(41,16))
        self.add_line('fly',(24,16),(24,23))
        self.relate('connect','waistband','outline')
        self.relate('connect','waistband','fly')
