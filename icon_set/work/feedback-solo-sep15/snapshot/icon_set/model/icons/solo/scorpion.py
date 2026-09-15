# Review candidate; original preserved.
"""Top-view scorpion with open pincers and a curled stinging tail. Centerline extremes (6,6)-(42,42). Lucide bug informs paired appendages. Tail remains left-curled; segmentation and one leg pair omitted for clear gaps."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '447f79a2-697e-4660-a5cc-b4e957e71821'
SOURCE_PATH = 'pictographic-primitives/animals/insect scorpion_447f79a2-697e-4660-a5cc-b4e957e71821.svg'
AUTHOR = 'gpt-6'

class Scorpion(Solo48):
    icon_id = 'scorpion'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('scorpion', 'sting', 'claws', 'arachnid', 'tail', 'desert', 'venom', 'zodiac')

    def build(self):
        # Scorpion: symmetric claws and legs attached at exact body extrema, plus a smooth curled tail.
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

        r('body',18,20,30,34,6)
        for side in (-1,1):
            l(f'upper-leg-{side}',(24+side*6,26),(24+side*18,24))
            l(f'lower-leg-{side}',(24,34),(24+side*18,34))
            link('connect',f'upper-leg-{side}','body')
            link('connect',f'lower-leg-{side}','body')
            p(f'arm-{side}',(24,20),(24+side*12,14),(24+side*14,6))
            l(f'claw-{side}',(24+side*12,14),(24+side*8,6))
            link('connect',f'arm-{side}',f'claw-{side}')
            link('connect',f'arm-{side}','body')
        link('connect','arm--1','arm-1')
        link('connect','lower-leg--1','lower-leg-1')
        a('tail',(24,34),(6,34),9,8,sweep=True)
        for part in ('body','lower-leg--1','lower-leg-1'):
            link('connect','tail',part)
