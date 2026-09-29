"""Restore a two-leaf stem beside curved pruning jaws with two individually outlined angled grips; deliberately asymmetric natural plant and tool.
Reference comparison: The rejected pruner looked like an R beside a single leaf: its cutting jaws, outlined grips and second leaf were lost.
Construction references: Lucide scissors: pivot-based cutting tool silhouette and separated grips. Supplied pruner defines curved blade and leaf arrangement.
Omissions: Tiny pivot hardware omitted to avoid a dark blob.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a757f97f-925d-4ec4-a7e5-e647c6df42dd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pruning-shears-leafy-stem/20260929T042221Z-thuan-mac/reference/pruner_a757f97f-925d-4ec4-a7e5-e647c6df42dd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pruning-shears-leafy-stem'
    keyshape = Keyshape.HRECT_L
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
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.add_line('stem',(13,24),(13,44))
        self.path('top-leaf',(13,24),('A',(13,4),13,14,True),('A',(13,24),13,14,True),closed=True)
        self.path('side-leaf',(12,31),('A',(4,19),12,12,True),('A',(12,31),12,12,True),closed=True)
        self.relate('connect','stem','top-leaf')
        self.path('blade',(29,24),('L',(34,6)),('A',(34,23),14,14,True),('L',(32,25)))
        self.path('left-grip',(29,24),('L',(23,40)),('A',(28,42),3,3,False),('L',(33,28)))
        self.path('right-grip',(32,25),('A',(37,28),5,5,True),('L',(43,40)),('A',(38,42),3,3,True),('L',(33,31)))
        self.relate('connect','blade','left-grip');self.relate('connect','blade','right-grip')

Drawing.exception = {'reason': 'Narrow outlined grips and leaf tips are essential to distinguish pruning shears. Local spacing and keyshape variance accepted under user authorization after native-size review.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '1d9863c5c120e41b569f8b347cbff1fda47b871b562ed066692a51bbb89ccb04'}
