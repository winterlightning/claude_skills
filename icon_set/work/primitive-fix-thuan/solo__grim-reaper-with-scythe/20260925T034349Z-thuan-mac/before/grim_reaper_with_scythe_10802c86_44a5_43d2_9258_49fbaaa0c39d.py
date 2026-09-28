"""Grim Reaper with Scythe.

Plan: Hooded robe left with blank face; separate long scythe connected by holding arm. Bounds (6,6)-(42,42).
Construction: human_ref/full_body_ref.png for economical figure, source hood and scythe; no exact Lucide match.
Reduction: Robe hem simplified; blade sweeps overhead to preserve open hood spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '10802c86-44a5-43d2-9258-49fbaaa0c39d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/grim reaper_10802c86-44a5-43d2-9258-49fbaaa0c39d.svg'
AUTHOR = 'gpt-6'


class GrimReaperWithScythe(Solo48):
    icon_id = 'grim-reaper-with-scythe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('grim', 'reaper', 'with', 'scythe')

    def build(self) -> None:

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
        path('robe',(6,42),[('L',(6,29)),('A',(30,29),12,12,True),('L',(30,34)),('L',(30,42)),('C',(18,41),(26,42),(22,41)),('C',(6,42),(14,41),(10,42))],True)
        circle('face',18,29,3)
        self.add_polyline('shaft',(42,6),(42,18),(42,34),(42,42))
        path('blade',(42,6),[('L',(6,6)),('C',(42,18),(18,6),(30,9))])
        self.relate('connect','shaft','blade')
        self.add_line('arm',(30,34),(42,34));self.relate('connect','arm','robe');self.relate('connect','arm','shaft')
