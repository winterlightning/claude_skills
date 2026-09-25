"""Rounded Beard with Moustache.

Plan: SQUARE centerlines (6,6)-(42,42); radius-18 round beard below tall sideburns and a mirrored wavy moustache.
Construction references: Supplied rounded-beard source; human_ref/user.svg informed the circular lower-face vocabulary; no useful exact Lucide match.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '0c32c222-4af0-55ad-a91f-8d15af99d088'
SOURCE_PATH = 'pictographic-primitives/beauty/beard style mustache_0c32c222-4af0-55ad-a91f-8d15af99d088.svg'
SOURCE_ICON_IDS = ('0c32c222-4af0-55ad-a91f-8d15af99d088',)
SOURCE_PATHS = ('pictographic-primitives/beauty/beard style mustache_0c32c222-4af0-55ad-a91f-8d15af99d088.svg',)
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'


class RoundedBeardWithMoustache(Solo48):
    icon_id = 'rounded-beard-with-moustache'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('rounded', 'beard', 'with', 'moustache')

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
        path("beard",(6,6),[("L",(6,14)),("L",(6,24)),("A",(42,24),18,18,False),("L",(42,14)),("L",(42,6))])
        path("moustache-top",(6,14),[("C",(axis,14),(10,30),(15,6)),("C",(42,14),(33,6),(38,30))])
        self.relate("connect","beard","moustache-top")
        path("moustache-division",(17,30),[("C",(axis,24),(20,30),(24,26)),("C",(31,30),(24,26),(28,30))])
