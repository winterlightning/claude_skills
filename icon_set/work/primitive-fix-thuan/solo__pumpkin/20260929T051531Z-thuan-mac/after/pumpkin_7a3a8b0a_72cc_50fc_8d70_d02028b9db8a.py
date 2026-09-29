"""Restore three rounded pumpkin lobes, a central vertical rib and a short curved outlined stem; mirror paired side lobes around x24.
Reference comparison: The rejected pumpkin was a squat three-loop knot and its stem was reduced to a hook. The reference has an elongated central rib, broad side lobes and a shaped stem.
Construction references: No useful local Lucide pumpkin match. Supplied reference establishes lobes and stem; shared smooth arc construction.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7a3a8b0a-72cc-50fc-8d70-d02028b9db8a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pumpkin/20260929T051531Z-thuan-mac/reference/pumpkin_7a3a8b0a-72cc-50fc-8d70-d02028b9db8a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pumpkin'
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
        # Broad side lobes and a taller central lobe share the same base, preserving the pumpkin's ribbed form.
        self.path('left-lobe',(18,14),('C',(4,28),(7,10),(4,18)),('C',(18,42),(4,38),(9,44)))
        self.path('right-lobe',(30,14),('C',(44,28),(41,10),(44,18)),('C',(30,42),(44,38),(39,44)))
        self.path('center-lobe',(24,12),('C',(36,28),(33,12),(36,18)),('C',(24,44),(36,39),(31,44)),('C',(12,28),(17,44),(12,39)),('C',(24,12),(12,18),(15,12)),closed=True)
        self.add_line('rib',(24,12),(24,44))
        self.path('stem',(22,12),('L',(22,9)),('A',(28,4),6,6,True),('A',(26,12),12,12,False))
        self.relate('connect','center-lobe','rib')

Drawing.exception = {'reason': 'Natural joined pumpkin ribs and the compact stem retain closer spacing than MIC; complete ribbed silhouette is accepted under the user-authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '731df1391aff314b421d08c148f018243535689844242867d0367dfb8c2d8843'}
