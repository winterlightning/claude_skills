"""Rotationally symmetric eight-tooth gear surrounded by eight short radial strokes. Shared quarter-pattern controls tooth equality and spacing.
Reference comparison: The rejected cog used four dots instead of radiating strokes and lost its tooth rhythm. Feedback asks to recover the radiating cog meaning.
Construction references: Lucide settings: repeating toothed silhouette; supplied reference controls surrounding radiance.
Omissions: Tooth count regularized to eight for a balanced native-size gear; source has no central hub.
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
        # Each quarter is rotated about (24,24); one shared tooth definition prevents asymmetry.
        quarter=[(21,12),(27,12),(28,16),(32,16),(32,20),(36,21)]
        points=[]
        for turn in range(4):
            for x,y in quarter:
                dx,dy=x-24,y-24
                for _ in range(turn): dx,dy=-dy,dx
                p=(24+dx,24+dy)
                if not points or p!=points[-1]:points.append(p)
        self.add_polyline('gear',*points,closed=True)
        for name,p,q in [('top',(24,3),(24,6)),('bottom',(24,42),(24,45)),('left',(3,24),(6,24)),('right',(42,24),(45,24)),('nw',(7,7),(10,10)),('ne',(38,10),(41,7)),('sw',(7,41),(10,38)),('se',(38,38),(41,41))]:
            self.add_line(name,p,q)

Drawing.exception = {'reason': 'Eight rays and cog require compact gaps and a radial envelope slightly larger than SQUARE. All strokes remain4px inside48px; user authorized native-size visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '87d3c405ff0a47df33c1287bae6d8056a2f25461ea9e1f862b3d0d3f42122290'}
