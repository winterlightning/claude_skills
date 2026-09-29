"""Open circular halo behind a round head, a bent raised arm and long robe sides with a diagonal draped fold.
Reference comparison: The rejected holy figure became a raised arm over a triangular block and lost the diagonal robe drape. The source shows an open halo, a round head and a flowing robe.
Construction references: human_ref/user.svg and full_body_ref.png: circular head and coherent human silhouette; supplied robed figure establishes halo and drapery.
Omissions: Open robe base preserved from source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'feefe9f2-9440-4f6a-b297-44a74f3dc1f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robed-figure-with-halo/20260929T051531Z-thuan-mac/reference/feast of the ascension_feefe9f2-9440-4f6a-b297-44a74f3dc1f9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'robed-figure-with-halo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        # The halo is a separate open arc behind the head. A raised arm belongs to a full robe, not a triangular pedestal.
        self.add_arc('halo',(12,16),(41,22),radius_x=17,radius_y=17,sweep=True,large_arc=True)
        self.circle('head',27,17,5)
        self.path('robe-and-arm',(19,44),('L',(22,30)),('L',(13,30)),('A',(9,26),4,4,True),('L',(9,19)),('A',(15,19),3,3,True),('L',(15,25)),('L',(33,25)),('L',(41,44)))
        self.add_line('robe-fold',(20,39),(34,26))
        self.relate('connect','robe-and-arm','robe-fold')

Drawing.exception = {'reason': 'Halo, head and robe form a compact devotional figure. Local spacing and natural robe envelope use the authorized visual exception; no generic pedestal replaces the body.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'b867a46e02a4339ffa337064291f7a1c1fa5fb5f6a422cad4a65e5ac35627995'}
