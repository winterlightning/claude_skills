"""Briefcase with Central Clasp.

Plan: HRECT centerlines (4,8)-(44,40); rounded rectangular case and radius4 handle share exact attachment nodes. Center clasp and flap use the case midline.
Construction references: Lucide briefcase-business: rounded case, shared handle and flap.
Reduction: Unified equivalent source references; kept the distinguishing blank or clasped front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '0e065604-cef0-4168-88bd-c1578cd53419'
SOURCE_PATH = 'pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg'
SOURCE_ICON_IDS = ('0e065604-cef0-4168-88bd-c1578cd53419', 'c246de89-264c-46cf-bdc1-2edde954a7a7', 'e756308e-0744-49f8-9b09-d1933550ea61')
SOURCE_PATHS = ('pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg', 'pictographic-primitives/business/briefcase_c246de89-264c-46cf-bdc1-2edde954a7a7.svg', 'pictographic-primitives/business/briefcase_e756308e-0744-49f8-9b09-d1933550ea61.svg')
AUTHOR = 'gpt-6'


class BriefcaseWithCentralClasp(Solo48):
    icon_id = 'briefcase-with-central-clasp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('briefcase', 'with', 'central', 'clasp')

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

        path("case",(8,16),[("L",(16,16)),("L",(32,16)),("L",(40,16)),("A",(44,20),4,4,True),("L",(44,26)),("L",(44,36)),("A",(40,40),4,4,True),("L",(8,40)),("A",(4,36),4,4,True),("L",(4,26)),("L",(4,20)),("A",(8,16),4,4,True)],True)
        path("handle",(16,16),[("L",(16,12)),("A",(20,8),4,4,True),("L",(28,8)),("A",(32,12),4,4,True),("L",(32,16))])
        self.relate("connect","case","handle")

        self.add_polyline("flap",(4,26),(24,26),(44,26))
        self.relate("connect","case","flap")
        self.add_line("clasp",(24,26),(24,32))
        self.relate("connect","clasp","flap")
