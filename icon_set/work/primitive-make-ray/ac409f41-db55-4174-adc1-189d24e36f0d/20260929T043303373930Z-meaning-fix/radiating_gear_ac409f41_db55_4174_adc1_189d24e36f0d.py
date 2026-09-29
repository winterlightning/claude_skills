"""Restore six smooth, symmetric gear lobes and eight surrounding short rays. The cog has no central hub, matching the reference.
Reference comparison: The rejected cog used four dots instead of radiating strokes and reduced its lobes to a coarse hexagon. Feedback asks to recover the radiating cog meaning.
Construction references: Lucide settings original and atomic geometry: alternating smooth outer teeth and inner valleys; source controls absence of hub and eight rays.
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
        # Six rounded teeth; both axes mirror exactly around (24,24).
        self.add_bezier('gear',(22,13),
            ((22,10),(26,10),(26,13)),
            ((26,16),(28,17),(31,15)),
            ((34,13),(37,18),(34,20)),
            ((31,22),(31,26),(34,28)),
            ((37,30),(34,35),(31,33)),
            ((28,31),(26,32),(26,35)),
            ((26,38),(22,38),(22,35)),
            ((22,32),(20,31),(17,33)),
            ((14,35),(11,30),(14,28)),
            ((17,26),(17,22),(14,20)),
            ((11,18),(14,13),(17,15)),
            ((20,17),(22,16),(22,13)))
        self.add_contour('gear-outline','gear',closed=True)
        for name,p,q in [('top',(24,3),(24,5)),('bottom',(24,43),(24,45)),('left',(3,24),(6,24)),('right',(42,24),(45,24)),('nw',(7,7),(10,10)),('ne',(38,10),(41,7)),('sw',(7,41),(10,38)),('se',(38,38),(41,41))]:
            self.add_line(name,p,q)

Drawing.exception = {'reason': 'Compact ray-to-cog spacing and radial bounds retain all six teeth and eight rays in48px with uniform4px strokes; user authorized visual exception after native-size review.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '882c9b07da9310b1e85df2590354df1931033ecd407dd9c537167524cdf7695f'}
