"""Centered circular head above a closed robe, a diagonal shoulder sash and five balanced radiance strokes. Touching-ink bust construction: head bottom26, robe apex30.
Reference comparison: The rejected monk had an off-center head, only three rays and an open generic bust. The original shows a centered radiant monk with a full robe and diagonal sash.
Construction references: human_ref/user.svg circular head and broad shoulders; source specifies robe, sash and rays.
Omissions: Small robe seam omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ae9da9e6-4132-4219-bed0-72be5d29e447'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__radiant-buddhist-monk/20260929T042221Z-thuan-mac/reference/magha puja_ae9da9e6-4132-4219-bed0-72be5d29e447.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'radiant-buddhist-monk'
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
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.circle('head',24,20,6)
        # Circular jaw bottom26 and shoulders apex30 leave touching 4px ink, as bust contract.
        self.path('robe',(12,44),('L',(12,38)),('A',(24,30),12,8,True),('A',(36,38),12,8,True),('L',(36,44)),('L',(12,44)),closed=True)
        self.add_line('sash',(12,42),(34,33))
        self.relate('connect','head','robe')
        self.add_line('top-ray',(24,3),(24,7))
        self.add_line('left-ray',(6,22),(9,22));self.add_line('right-ray',(39,22),(42,22))
        self.add_line('upper-left-ray',(10,7),(13,10));self.add_line('upper-right-ray',(35,10),(38,7))
        self.human_construction='bust'

Drawing.exception = {'reason': 'Five radiance rays and diagonal robe sash retain compact local gaps and organic bounds. User authorized the native-size visual exception; 4px strokes and circular head are preserved.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'fe408025c5561dca35c52fb107fd9f53f6b43b5be918a791773c01abc29f41cb'}
