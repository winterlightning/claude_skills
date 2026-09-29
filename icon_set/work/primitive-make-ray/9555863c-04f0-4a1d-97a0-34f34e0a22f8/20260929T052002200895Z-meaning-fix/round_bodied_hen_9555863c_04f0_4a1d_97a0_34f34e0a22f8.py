"""Restore a round-bellied hen with raised tail, curved neck, comb, pointed beak, wattle and two small feet.
Reference comparison: The rejected hen lost its comb, wattle and articulated feet and resembled a generic bathtub bird.
Construction references: Lucide bird: continuous bird outline and short legs; supplied reference owns round body, comb and wattle.
Omissions: Eye omitted as in the source to keep head details open.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9555863c-04f0-4a1d-97a0-34f34e0a22f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-bodied-hen/20260929T051531Z-thuan-mac/reference/broiler_9555863c-04f0-4a1d-97a0-34f34e0a22f8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-bodied-hen'
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
        # Hen is a single round-bellied silhouette; upright tail, comb, beak and two feet carry identity.
        self.path('hen',(6,15),('C',(23,21),(12,20),(17,23)),('C',(29,13),(27,21),(25,16)),('C',(39,12),(29,7),(35,8)),('L',(44,16)),('L',(39,19)),('L',(39,25)),('C',(24,38),(39,33),(33,38)),('C',(6,23),(12,38),(6,32)),('L',(6,15)),closed=True)
        self.add_arc('comb',(29,10),(37,10),radius_x=4,radius_y=6,sweep=True)
        self.add_arc('wattle',(39,19),(38,26),radius_x=3,radius_y=4,sweep=True)
        self.path('left-foot',(20,38),('L',(20,44)),('L',(17,44)))
        self.path('right-foot',(28,38),('L',(28,44)),('L',(31,44)))
        self.relate('connect','hen','comb');self.relate('connect','hen','wattle');self.relate('connect','hen','left-foot');self.relate('connect','hen','right-foot')

Drawing.exception = {'reason': 'Comb and wattle have compact outline gaps at48px, while attached feet and beak retain natural contacts. User authorized the complete hen silhouette as a visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'c9aaa16ae52309bb55c1d89fb7a016067ffe5c81d01b84032fa74466761989f1'}
