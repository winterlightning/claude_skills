"""Round tomato body with a pointed five-lobed calyx, upright stem and one curved skin highlight; maintain the source broad natural silhouette.
Reference comparison: The rejected tomato had a simple two-leaf top and no pointed star calyx or skin highlight, so it resembled a generic round fruit.
Construction references: No useful local Lucide tomato match; source establishes star-shaped calyx and round body.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '48f3e52f-9771-4349-89ba-dada134c9d72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-fresh-tomato/20260929T051531Z-thuan-mac/reference/tomato_48f3e52f-9771-4349-89ba-dada134c9d72.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-fresh-tomato'
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
        # Tomato body is broad and round, with a pointed calyx rather than two leaf-like wings.
        self.path('fruit',(13,16),('C',(4,29),(6,19),(4,24)),('C',(24,44),(4,39),(13,44)),('C',(44,29),(35,44),(44,39)),('C',(35,16),(44,24),(42,19)))
        self.path('calyx',(24,13),('C',(10,14),(19,9),(14,10)),('L',(16,16)),('L',(14,22)),('L',(22,19)),('L',(24,26)),('L',(28,19)),('L',(35,22)),('L',(33,16)),('L',(39,14)),('C',(24,13),(34,10),(29,10)),closed=True)
        self.add_line('stem',(24,4),(24,13));self.relate('connect','calyx','stem')
        self.add_arc('highlight',(31,37),(37,30),radius_x=11,radius_y=11,sweep=False)

Drawing.exception = {'reason': 'The calyx has tightly connected pointed leaves and compact fruit junctions. Preserve these identifying details with4px strokes using the authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '0cfb711f53eb01cc515be40db2e80dea6a6fbb496bca949521a663c636b1fb50'}
