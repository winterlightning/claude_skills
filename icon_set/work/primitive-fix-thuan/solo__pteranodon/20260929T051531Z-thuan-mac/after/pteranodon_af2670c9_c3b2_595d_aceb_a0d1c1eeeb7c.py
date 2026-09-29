"""Restore the long pointed beak, curved cranial crest, large swept wing, flowing belly and two small trailing legs; retain the source directional asymmetry.
Reference comparison: The rejected pteranodon was a symmetric bat-shaped star. The source is an asymmetric side view with a long left-facing beak, backward crest and a swept right wing.
Construction references: No useful local Lucide pterosaur match. Source silhouette controls construction; smooth curves preserve wing and neck flow.
Omissions: Tiny eye and wing rib lines omitted, matching the sparse source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pteranodon/20260929T051531Z-thuan-mac/reference/dinosaur pteranodon_af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pteranodon'
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
        # Side-profile pterosaur, intentionally asymmetric: long beak left, crest above neck, raised wing right.
        self.path('flying-pterosaur',(4,32),('L',(18,24)),('L',(14,18)),('L',(4,16)),('C',(26,7),(11,9),(18,9)),('C',(26,25),(19,13),(22,21)),('C',(44,5),(27,17),(37,10)),('C',(40,32),(37,19),(37,24)),('C',(28,36),(35,31),(35,38)),('C',(4,32),(18,32),(15,32)),closed=True)
        self.add_line('rear-leg',(38,33),(42,39));self.add_line('front-leg',(32,36),(36,43))
        self.relate('connect','flying-pterosaur','rear-leg');self.relate('connect','flying-pterosaur','front-leg')

Drawing.exception = {'reason': 'Natural pterosaur proportions need an asymmetric near-full square envelope and sharp beak/wing tips. User-authorized visual exception preserves identity with4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'e7ca2c394eb90086d7abe47fcad2b831f985136394a93c395d995b3ee3cbe8f9'}
