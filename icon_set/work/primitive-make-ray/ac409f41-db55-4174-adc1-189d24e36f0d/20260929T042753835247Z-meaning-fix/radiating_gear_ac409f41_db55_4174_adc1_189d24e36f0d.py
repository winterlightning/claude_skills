"""A toothed central cog surrounded by eight short radial strokes; preserve the reference absence of a central hub.
Reference comparison: The rejected gear replaced the radial light strokes with four dots and used a coarse hexagonal outline. Feedback asks to recover the radiating cog.
Construction references: Lucide settings: coherent toothed silhouette; supplied reference specifies eight radiating strokes.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ac409f41-db55-4174-adc1-189d24e36f0d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__radiating-gear/20260929T042221Z-thuan-mac/reference/workflow teamwork cog share_ac409f41-db55-4174-adc1-189d24e36f0d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'radiating-gear'
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
        # Symmetric six-tooth cog with alternating rounded lobes and valleys.
        self.path('gear',(21,13),('L',(27,13)),('L',(28,17)),('L',(32,17)),('L',(35,22)),('L',(32,25)),('L',(34,29)),('L',(30,33)),('L',(26,31)),('L',(24,35)),('L',(19,33)),('L',(19,29)),('L',(14,28)),('L',(13,23)),('L',(17,21)),('L',(17,17)),('L',(21,16)),closed=True)
        for name,p,q in [('top',(24,4),(24,7)),('bottom',(24,41),(24,44)),('left',(4,24),(7,24)),('right',(41,24),(44,24)),('nw',(8,8),(11,11)),('ne',(37,11),(40,8)),('sw',(8,40),(11,37)),('se',(37,37),(40,40))]:
            self.add_line(name,p,q)

Drawing.exception = {'reason': 'Eight radial rays require a compact cog-to-ray gap and non-square radial envelope. These remain legible with uniform 4px strokes under the authorized exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'df4090281d45f639bfb2ed1467f90862464d24e2307f16cbb3672f2e89a1b356'}
