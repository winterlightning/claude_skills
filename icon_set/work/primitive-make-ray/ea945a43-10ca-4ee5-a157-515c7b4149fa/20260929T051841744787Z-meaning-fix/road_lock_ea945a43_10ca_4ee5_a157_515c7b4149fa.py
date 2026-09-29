"""Rounded padlock with a broad shackle, converging road edges and two centered road markings; shared vertical axis keeps road and lock aligned.
Reference comparison: The rejected lock contained an arch-like block instead of a perspective road and omitted both center dashes.
Construction references: Lucide lock: rounded shackle and rectangular body; reference defines perspective road.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ea945a43-10ca-4ee5-a157-515c7b4149fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__road-lock/20260929T051531Z-thuan-mac/reference/road lock_ea945a43-10ca-4ee5-a157-515c7b4149fa.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'road-lock'
    keyshape = Keyshape.VRECT_L
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
        self.path('body',(10,22),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,40)),('A',(38,44),4,4,True),('L',(10,44)),('A',(6,40),4,4,True),('L',(6,26)),('A',(10,22),4,4,True),closed=True)
        self.path('shackle',(14,22),('L',(14,14)),('A',(34,14),10,10,True),('L',(34,22)))
        self.path('road-left',(14,43),('L',(21,28)))
        self.path('road-right',(34,43),('L',(27,28)))
        self.add_line('road-dash-upper',(24,31),(24,32))
        self.add_line('road-dash-lower',(24,38),(24,39))
        self.relate('connect','body','shackle')

Drawing.exception = {'reason': 'Two visible road dashes inside a perspective road require compact interior gaps; the complete symbol is readable at48px with4px strokes under the authorized exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '7ee9906182aaeb406f3bb925a749c83e4cb6eadc82c2c05592516066488eb9f2'}
