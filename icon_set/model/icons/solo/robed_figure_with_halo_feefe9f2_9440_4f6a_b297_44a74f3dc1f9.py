"""Robed Figure with Halo.

Plan: Head center(28,19) radius4; open halo and raised arm; neck at(28,31), flared robe. Centerlines (6,6)-(42,42).
Construction: human_ref/full_body_ref.png detached head; source open halo and diagonal robe.
Reduction: Omitted diagonal sash to prevent a pinched triangular opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'feefe9f2-9440-4f6a-b297-44a74f3dc1f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/feast of the ascension_feefe9f2-9440-4f6a-b297-44a74f3dc1f9.svg'
AUTHOR = 'gpt-6'


class IconRobedFigureWithHalo(Solo48):
    icon_id = 'robed-figure-with-halo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('robed', 'figure', 'with', 'halo')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        circle('head',28,19,4)
        path('halo',(14,20),[('A',(28,6),14,14,True),('A',(42,20),14,14,True)])
        path('robe',(24,31),[('L',(28,31)),('L',(32,31)),('L',(40,42)),('L',(16,42)),('L',(24,31))],True)
        self.add_polyline('arm',(24,31),(6,31),(6,21));self.relate('connect','arm','robe')
