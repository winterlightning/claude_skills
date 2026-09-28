"""Hands Holding Share Symbol.

Plan: mirrored open cupped hands; share nodes excluded. VRECT_L extremes8,4,40,44.
Human full_body_ref.png and Lucide hand inform minimal round-ended anatomy.
Each hand is one continuous open contour; no narrow doubled finger outlines.
Reference: pictographic-primitives/school-learning/e learning share_faabe7b6-2ce7-47c5-a31b-881b93ad2845.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faabe7b6-2ce7-47c5-a31b-881b93ad2845'
SOURCE_PATH = 'pictographic-primitives/school-learning/e learning share_faabe7b6-2ce7-47c5-a31b-881b93ad2845.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cupped-hands-share-component'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/school-learning'
    aliases = ()
    keywords = ('cupped', 'hands', 'share', 'component')

    def build(self):

        def path(name, start, commands, closed=False):
            point, members = start, []
            for index, command in enumerate(commands):
                kind, end, *args = command
                member = f'{name}-{index}'
                if kind == 'L':
                    self.add_line(member, point, end)
                elif kind == 'A':
                    self.add_arc(member, point, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                else:
                    self.add_bezier(member, point, (args[0], args[1], end))
                point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, radius):
            path(name, (x-radius,y), [('A',(x+radius,y),radius,radius,True),
                 ('A',(x-radius,y),radius,radius,True)], True)
        def box(name, l, t, r, b, radius=4):
            path(name,(l+radius,t),[('L',(r-radius,t)),('A',(r,t+radius),radius,radius,True),
                ('L',(r,b-radius)),('A',(r-radius,b),radius,radius,True),('L',(l+radius,b)),
                ('A',(l,b-radius),radius,radius,True),('L',(l,t+radius)),
                ('A',(l+radius,t),radius,radius,True)],True)

        for j,sign in enumerate((-1,1)):
            def pt(x,y): return (24+sign*x,y)
            path(f'hand-{j}',pt(8,44),[('L',pt(8,35)),('L',pt(16,27)),('L',pt(16,4))])
            path(f'thumb-{j}',pt(4,29),[('L',pt(8,13)),('L',pt(16,13))])
            self.relate('connect',f'hand-{j}',f'thumb-{j}')
