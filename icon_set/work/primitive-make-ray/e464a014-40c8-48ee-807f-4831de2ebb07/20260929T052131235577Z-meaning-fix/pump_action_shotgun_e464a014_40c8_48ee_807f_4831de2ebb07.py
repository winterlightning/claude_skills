"""Restore long diagonal shotgun proportions, compact rounded butt, rounded fore-end pump and small trigger guard.
Reference comparison: The rejected shotgun looked like an angular pistol with a large box below it. The original has a long barrel, curved pump grip and a separate small trigger guard.
Construction references: Lucide sword: clean diagonal construction; supplied shotgun reference owns barrel and stock proportions.
Omissions: Mechanical fasteners omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e464a014-40c8-48ee-807f-4831de2ebb07'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pump-action-shotgun/20260929T051531Z-thuan-mac/reference/shotgun_e464a014-40c8-48ee-807f-4831de2ebb07.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pump-action-shotgun'
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
        # One diagonal shotgun body with a short butt, a separate rounded pump and a small trigger guard.
        self.path('stock-and-barrel',(8,44),('L',(5,35)),('C',(9,28),(3,32),(5,30)),('L',(38,6)),('L',(43,11)),('L',(18,31)),('L',(12,36)),('L',(14,41)),('A',(8,44),4,4,True),closed=True)
        self.path('pump',(23,27),('A',(29,30),5,5,False),('L',(37,24)),('A',(39,17),5,5,False))
        self.path('trigger-guard',(13,35),('L',(18,33)),('A',(16,29),4,4,False))
        self.relate('connect','stock-and-barrel','pump');self.relate('connect','stock-and-barrel','trigger-guard')

Drawing.exception = {'reason': 'The long barrel band, pump attachment and compact trigger opening retain natural narrow gaps under the authorized visual exception; this is a48px pictogram with4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '8caa5d05b4313b5bb2810e5b93e4bbb9ae8fcdf1a48e175946123dfa576d03d8'}
