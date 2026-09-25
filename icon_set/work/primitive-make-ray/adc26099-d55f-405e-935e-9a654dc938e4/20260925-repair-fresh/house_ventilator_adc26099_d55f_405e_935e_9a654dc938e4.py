"""Fresh repair. Parent preserved in previous.py.txt. Supplied reference re-inspected.
See findings.md for current omissions and review; inherited comments describe the parent design.
"""
"""A four-bladed ventilation fan is inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None; all four blades and hub retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='adc26099-d55f-405e-935e-9a654dc938e4'
SOURCE_PATH = 'pictographic-primitives/other/house ventilator_adc26099-d55f-405e-935e-9a654dc938e4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-ventilator'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'ventilator')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def house(self):
        # One mirrored envelope, x=24 axis; centerline extremes 6,6,42,42.
        self.add_line('roof-1',(6,14),(24,6))
        self.add_line('roof-2',(24,6),(42,14))
        self.add_line('wall-right',(42,14),(42,40))
        self.add_arc('corner-right',(42,40),(40,42),radius_x=2)
        self.add_line('floor',(40,42),(8,42))
        self.add_arc('corner-left',(8,42),(6,40),radius_x=2)
        self.add_line('wall-left',(6,40),(6,14))
        self.add_contour('house','roof-1','roof-2','wall-right','corner-right','floor','corner-left','wall-left',closed=True)

    def lock_body(self):
        # Shared shackle nodes are vertices in the top rail.
        self.add_polyline('lock-body',(17,26),(19,26),(29,26),(31,26),(31,34),(17,34),closed=True)

    def build(self):
        self.house()
        cx,cy=24,25
        for i in range(4):
            def rot(x,y):
                for _ in range(i):x,y=-y,x
                return cx+x,cy+y
            self.add_bezier('blade-'+str(i),rot(0,0),(rot(0,-6),rot(9,-8),rot(8,0)))
        self.relate('connect',*[f'blade-{i}' for i in range(4)])

