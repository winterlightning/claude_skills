"""Shirt with Wavy Stripes.

Plan: VRECT centerlines (8,4)-(40,44); one mirrored short-sleeved garment contour with radius6 neck opening and rounded hem corners. Repeated buttons or wavy stripes use shared spacing.
Construction references: Lucide shirt: curved neck, short sleeves and rounded lower garment corners.
Reduction: Buttons are three stroke-wide round dots instead of tiny outlined circles. Striped version retains two flowing lines and deliberate directional asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7bf3dfa5-3ac7-5f0a-80ef-6a0df922feb1'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design animal skin_7bf3dfa5-3ac7-5f0a-80ef-6a0df922feb1.svg'
SOURCE_ICON_IDS = ('7bf3dfa5-3ac7-5f0a-80ef-6a0df922feb1',)
SOURCE_PATHS = ('pictographic-primitives/clothes/clothes design animal skin_7bf3dfa5-3ac7-5f0a-80ef-6a0df922feb1.svg',)
AUTHOR = 'gpt-6'


class ShirtWithWavyStripes(Solo48):
    icon_id = 'shirt-with-wavy-stripes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('shirt', 'with', 'wavy', 'stripes')

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

        path("shirt",(18,4),[("A",(30,4),6,6,False),("L",(36,6)),("L",(40,14)),("L",(36,20)),("L",(34,18)),("L",(34,20)),("L",(34,32)),("L",(34,42)),("A",(32,44),2,2,True),("L",(16,44)),("A",(14,42),2,2,True),("L",(14,34)),("L",(14,22)),("L",(14,18)),("L",(12,20)),("L",(8,14)),("L",(12,6)),("L",(18,4))],True)

        for i,dy in enumerate((0,12)):
            path(f"stripe-{i}",(14,22+dy),[("C",(34,20+dy),(20,26+dy),(28,16+dy))])
            self.relate("connect",f"stripe-{i}","shirt")
