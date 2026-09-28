"""money bags.
Plan: Two money bags: larger front bag with dollar S and scalloped crown, smaller left rear bag. Exact square extremes retained; increase currency-to-tie gap. No useful Lucide exact match; asymmetry follows reference.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='facf19d7-e5b7-4559-806e-6d1d682ef4d0'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='money-bags'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('money', 'bags')
    def build(self):
        self.add_bezier(
            "small-bag-crown", (11, 21),
            ((9, 18), (10, 15), (13, 16)),
            ((15, 14), (16, 18), (17, 17)),
            ((20, 16), (22, 18), (19, 21)),
        )
        self.add_line("small-bag-tie", (11, 21), (19, 21))
        self.add_bezier(
            "small-bag-body", (11, 21),
            ((8, 25), (6, 28), (6, 31)),
            ((6, 35), (10, 37), (15, 37)),
        )
        self.relate("connect", "small-bag-crown", "small-bag-tie")
        self.relate("connect", "small-bag-body", "small-bag-tie")

        self.add_bezier(
            "front-bag-crown", (20, 18),
            ((18, 14), (17, 11), (19, 9)),
            ((21, 7), (22, 10), (24, 9)),
            ((25, 7), (25, 6), (27, 6)),
            ((29, 6), (30, 10), (32, 9)),
            ((35, 8), (36, 11), (34, 14)),
            ((33, 16), (32, 17), (32, 18)),
        )
        self.add_line("front-bag-tie", (20, 18), (32, 18))
        self.add_bezier(
            "front-bag-body", (20, 18),
            ((14, 23), (12, 28), (12, 32)),
            ((12, 38), (18, 42), (26, 42)),
            ((34, 42), (42, 38), (42, 32)),
            ((42, 27), (36, 22), (32, 18)),
        )
        self.relate("connect", "front-bag-crown", "front-bag-tie")
        self.relate("connect", "front-bag-body", "front-bag-tie")

        self.add_line("dollar-upper-stem", (27, 26), (27, 27))
        self.add_bezier(
            "dollar-s", (27, 27),
            ((23, 25), (22, 28), (24, 29)),
            ((26, 30), (31, 29), (31, 32)),
            ((31, 34), (28, 35), (26, 33)),
        )
        self.add_line("dollar-lower-stem", (26, 33), (26, 34))
        self.add_contour("dollar", "dollar-upper-stem", "dollar-s", "dollar-lower-stem")

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
