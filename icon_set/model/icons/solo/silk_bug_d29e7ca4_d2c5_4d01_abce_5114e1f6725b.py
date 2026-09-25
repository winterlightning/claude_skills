from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd29e7ca4-d2c5-4d01-abce-5114e1f6725b'
SOURCE_PATH = 'pictographic-primitives/animals/silk bug_d29e7ca4-d2c5-4d01-abce-5114e1f6725b.svg'
AUTHOR = 'gpt-6'


class DomedBeetle(Solo48):
    icon_id = 'domed-beetle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'shell', 'antennae', 'legs', 'nature', 'wildlife')

    def build(self):
        # Beetle: a smooth capsule shell with a central seam and symmetric single-stroke appendages.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('shell',14,12,34,40,10)
        l('seam',(24,12),(24,40))
        link('connect','seam','shell')
        for side in (-1,1):
            for j,y in enumerate((22,30,40)):
                # End at the same side of the shell; the bottom leg meets its apex.
                start=(14 if side<0 else 34,y) if j<2 else (24,40)
                end=(8 if side<0 else 40, y-6 if j==0 else (44 if j==2 else y))
                l(f'leg-{side}-{j}',start,end)
                link('connect',f'leg-{side}-{j}','shell')
                if j==2:
                    link('connect',f'leg-{side}-{j}','seam')
            l(f'antenna-{side}',(24,12),(24+side*10,4))
            link('connect',f'antenna-{side}','shell')
            link('connect',f'antenna-{side}','seam')
        link('connect','antenna--1','antenna-1')
        link('connect','leg--1-2','leg-1-2')
