"""Front-Facing Bulldozer.

Plan: HRECT centerlines (4,8)-(44,40); symmetrical rounded cab, tapered body and broad flared blade; paired semicircular wheels peek beneath the blade.
Construction references: Lucide tractor: cab/body hierarchy and circular wheels; supplied source controls the front blade.
Reduction: Omitted the small grille mark to preserve clearance between cab and blade.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '82b77389-0a3b-46fa-9b1e-a4828377cd31'
SOURCE_PATH = 'pictographic-primitives/construction/cleaner_82b77389-0a3b-46fa-9b1e-a4828377cd31.svg'
SOURCE_ICON_IDS = ('82b77389-0a3b-46fa-9b1e-a4828377cd31',)
SOURCE_PATHS = ('pictographic-primitives/construction/cleaner_82b77389-0a3b-46fa-9b1e-a4828377cd31.svg',)
AUTHOR = 'gpt-6'


class FrontFacingBulldozer(Solo48):
    icon_id = 'front-facing-bulldozer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('front-facing', 'bulldozer')

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

        path("cab",(16,16),[("L",(16,12)),("A",(20,8),4,4,True),("L",(28,8)),("A",(32,12),4,4,True),("L",(32,16))])
        self.add_polyline("body",(10,26),(12,16),(16,16),(32,16),(36,16),(38,26))
        self.relate("connect","cab","body")
        self.add_polyline("blade",(4,34),(6,26),(10,26),(38,26),(42,26),(44,34),(40,34),(28,34),(20,34),(8,34),closed=True)
        self.relate("connect","body","blade")
        for x in (14,34):
            self.add_arc(f"wheel-{x}",(x+6,34),(x-6,34),radius_x=6)
            self.relate("connect",f"wheel-{x}","blade")
