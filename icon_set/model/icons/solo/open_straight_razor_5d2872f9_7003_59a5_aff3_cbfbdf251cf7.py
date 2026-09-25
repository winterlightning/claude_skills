"""Open Straight Razor.

Plan: SQUARE centerlines (6,6)-(42,42); broad diagonal blade, shared hinge/tang node and a smooth sweeping handle. Intentional opening angle follows the source.
Construction references: Lucide pocket-knife: blade/handle articulation and shared pivot; source supplies the open straight-razor silhouette.
Reduction: Simplified the outlined handle to one rounded curved stroke; omitted the tiny pivot marking.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5d2872f9-7003-59a5-aff3-cbfbdf251cf7'
SOURCE_PATH = 'pictographic-primitives/beauty/beard style razor_5d2872f9-7003-59a5-aff3-cbfbdf251cf7.svg'
SOURCE_ICON_IDS = ('5d2872f9-7003-59a5-aff3-cbfbdf251cf7',)
SOURCE_PATHS = ('pictographic-primitives/beauty/beard style razor_5d2872f9-7003-59a5-aff3-cbfbdf251cf7.svg',)
AUTHOR = 'gpt-6'


class OpenStraightRazor(Solo48):
    icon_id = 'open-straight-razor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('open', 'straight', 'razor')

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

        self.add_polyline("blade",(6,14),(14,6),(30,22),(26,26),(22,30),closed=True)
        path("handle",(6,42),[("C",(34,34),(18,42),(26,40)),("C",(42,30),(38,32),(40,31))])
        self.add_line("tang",(26,26),(34,34))
        self.relate("connect","blade","tang")
        self.relate("connect","handle","tang")
