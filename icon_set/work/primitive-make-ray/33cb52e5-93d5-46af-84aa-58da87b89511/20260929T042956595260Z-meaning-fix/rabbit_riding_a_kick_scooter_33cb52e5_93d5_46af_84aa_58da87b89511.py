"""Restore left-side steering stem and wheel, long swept rabbit ear, distinct snout, rounded haunch, reaching arm and feet on the deck.
Reference comparison: The rejected scooter rabbit was reversed and its ear/body shape read like an abstract human. The reference shows a left-facing scooter with a rabbit behind the handlebar.
Construction references: Lucide bike circular wheels and coherent equipment strokes; source rabbit silhouette defines long ear and head.
Omissions: Tiny eye omitted to keep the head open.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '33cb52e5-93d5-46af-84aa-58da87b89511'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rabbit-riding-a-kick-scooter/20260929T042221Z-thuan-mac/reference/scooter faster rabbit_33cb52e5-93d5-46af-84aa-58da87b89511.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rabbit-riding-a-kick-scooter'
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
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        # Scooter faces left like the original: handle above the front wheel, rabbit behind it.
        self.circle('front-wheel',8,40,4);self.circle('rear-wheel',39,40,4)
        self.add_line('deck',(12,40),(35,40))
        self.path('steering',(8,40),('L',(8,9)),('L',(4,7)))
        # Tall backward-swept ear, snout and haunch are one coherent rabbit silhouette.
        self.add_bezier('ear',(29,18),((20,12),(20,5),(24,5)),((29,5),(32,12),(34,15)))
        self.add_bezier('face',(34,15),((41,16),(44,20),(41,24)),((39,26),(35,26),(34,26)))
        self.add_bezier('back',(34,26),((35,32),(31,35),(29,36)))
        self.add_line('hind-foot',(29,36),(29,40))
        self.add_bezier('chest',(29,18),((28,23),(30,26),(25,26)))
        self.add_line('reaching-arm',(25,26),(8,26))
        self.add_line('front-leg',(25,26),(21,40))
        self.add_contour('rabbit-outline','ear','face','back','hind-foot')
        self.relate('connect','rabbit-outline','chest');self.relate('connect','chest','reaching-arm');self.relate('connect','chest','front-leg');self.relate('connect','front-leg','deck');self.relate('connect','rabbit-outline','deck')

Drawing.exception = {'reason': 'Rabbit and scooter use compact true overlaps and a narrow steering/body gap to keep the complete reference scene. User authorized native-size visual exception with 4px strokes and 48px canvas.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'addd4faf88897275533f6dabe076e6b26e06d272da68a3a3c0077de9356b8a3d'}
