# Follow-up review: Lucide flame: broad connected counter; preserve three pointed tongues and both brick courses. HRECT_L centerline extremes (4,8)-(44,40).
# Variant of brick-firewall-v2; parent file remains unchanged.
"""A flame rises from a staggered brick wall. Three masonry courses reduce to two, retaining alternating joints and the flame silhouette. Lucide flame informs the outer curved lobe; deliberate flame asymmetry preserves the tongues.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31873389-9f53-4271-a274-ace8612680cd'
SOURCE_PATH = 'pictographic-primitives/programing/firewall_31873389-9f53-4271-a274-ace8612680cd.svg'
AUTHOR = 'gpt-6'

class BrickFirewall(Solo48):
    icon_id = 'brick-firewall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/programming'
    aliases = ()
    keywords = ('firewall', 'fire', 'flame', 'wall', 'bricks', 'security', 'network', 'protection')

    def build(self):
        # Plan: Wall owns two eight-unit brick courses and staggered joints. One broad smooth flame replaces cramped short tongues; flame silhouette remains asymmetric.

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
        poly('wall',(4,24),(16,24),(32,24),(44,24),(44,32),(44,40),(24,40),(4,40),(4,32),closed=True)
        poly('course',(4,32),(16,32),(24,32),(32,32),(44,32));join('wall','course')
        for x in (16,32):
         line(f'upper-{x}',(x,24),(x,32));join(f'upper-{x}','wall');join(f'upper-{x}','course')
        line('lower',(24,32),(24,40));join('lower','wall');join('lower','course')
        path('flame',(16,24), [('C',(24,8),(8,18),(24,14)),('C',(32,24),(24,15),(42,17))])
        join('wall','flame')
