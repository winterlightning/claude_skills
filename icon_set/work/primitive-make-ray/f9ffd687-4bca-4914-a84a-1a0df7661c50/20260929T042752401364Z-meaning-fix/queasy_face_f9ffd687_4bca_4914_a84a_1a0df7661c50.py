"""Downcast curved eyelids, a small pursed mouth, open lower-right face outline and a detached organic queasy puff.
Reference comparison: The rejected face had angry eyes and a mouth-like shape fused to its jaw. The source shows closed queasy eyes, pursed mouth and a separate breath puff.
Construction references: Supplied face defines expression; Lucide circular construction informs the head outline.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9ffd687-4bca-4914-a84a-1a0df7661c50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__queasy-face/20260929T042221Z-thuan-mac/reference/sick_f9ffd687-4bca-4914-a84a-1a0df7661c50.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'queasy-face'
    keyshape = Keyshape.CIRCLE
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
        self.path('face',(28,43),('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('L',(44,27)))
        self.add_arc('left-eye',(12,18),(20,18),radius_x=5,radius_y=4,sweep=False)
        self.add_arc('right-eye',(28,18),(36,18),radius_x=5,radius_y=4,sweep=False)
        self.add_arc('mouth',(19,32),(23,29),radius_x=5,radius_y=5,sweep=True)
        self.path('queasy-puff',(29,30),('A',(35,29),4,4,True),('A',(39,32),5,5,False),('A',(44,36),5,5,True),('A',(35,43),9,7,True),('A',(28,36),8,8,True),('A',(29,30),6,6,True),closed=True)

Drawing.exception = {'reason': 'Expressive mouth and puff require local spacing below 4px and an open circular envelope; all marks stay in canvas and use 4px stroke. User authorized expression-preserving exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '885dd95e95335d0006231c62f6b6b539cde62aa761b145cd90ca6673d89a7cbb'}
