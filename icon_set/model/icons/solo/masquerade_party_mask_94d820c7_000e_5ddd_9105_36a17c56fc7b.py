"""Masquerade Party Mask.

Plan: Mirrored swept eye mask, two lower lobes and bridge. Bounds (4,8)-(44,40).
Construction: Lucide venetian-mask: paired lower lobes and open curved eye strokes. Source supplies pointed outer corners.
Reduction: Almond cutouts reduced to expressive curved eye strokes to preserve the mask walls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '94d820c7-000e-5ddd-9105-36a17c56fc7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/mardi gras_94d820c7-000e-5ddd-9105-36a17c56fc7b.svg'
AUTHOR = 'gpt-6'


class IconMasqueradePartyMask(Solo48):
    icon_id = 'masquerade-party-mask'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('masquerade', 'party', 'mask')

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
        path('mask',(4,8),[('C',(24,17),(12,12),(18,9)),('C',(44,8),(30,9),(36,12)),('C',(34,40),(44,30),(42,40)),('C',(24,35),(29,40),(26,38)),('C',(14,40),(22,38),(19,40)),('C',(4,8),(6,40),(4,30))],True)
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         path('eye-'+str(side),p(11,24),[('C',p(6,27),p(8,24),p(7,25))])

        # Party source has the same physical mask construction; its source identity remains independent.
