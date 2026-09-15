"""Pointed Beard with Curled Moustache.

Plan: SQUARE centerlines (6,6)-(42,42); paired curled moustache lobes above a coherent pointed beard, mirrored around x24.
Construction references: Supplied pointed-beard source; human_ref/user.svg informed facial-hair placement; no useful exact Lucide match.
Reduction: Removed fine inner divisions; preserved the curled tips and pointed chin.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9af73eee-e38d-550a-8356-879d828c0fbf'
SOURCE_PATH = 'pictographic-primitives/beauty/beard style mustache_9af73eee-e38d-550a-8356-879d828c0fbf.svg'
SOURCE_ICON_IDS = ('9af73eee-e38d-550a-8356-879d828c0fbf',)
SOURCE_PATHS = ('pictographic-primitives/beauty/beard style mustache_9af73eee-e38d-550a-8356-879d828c0fbf.svg',)
AUTHOR = 'gpt-6'


class PointedBeardWithCurledMoustache(Solo48):
    icon_id = 'pointed-beard-with-curled-moustache'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('pointed', 'beard', 'with', 'curled', 'moustache')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        axis=24
        path("moustache",(6,6),[("C",(axis,8),(6,18),(14,8)),("C",(42,6),(34,8),(42,18)),("L",(42,16)),("C",(axis,16),(42,26),(28,26)),("C",(6,16),(20,26),(6,26)),("L",(6,6))],True)
        path("beard",(6,16),[("C",(axis,42),(6,32),(12,34)),("C",(42,16),(36,34),(42,32))])
        self.relate("connect","moustache","beard")
