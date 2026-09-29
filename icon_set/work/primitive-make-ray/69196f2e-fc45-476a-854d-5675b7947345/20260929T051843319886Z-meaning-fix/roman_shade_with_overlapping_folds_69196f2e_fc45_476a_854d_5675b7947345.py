"""Long rounded headrail, two broad overlapping fabric folds with curved left drape, and a fine pull cord with round weight.
Reference comparison: The rejected Roman shade had a disconnected lower strip and an oversized pull weight; overlapping fabric panels were lost.
Construction references: Lucide blinds: suspended pull cord and repeated horizontal structure; original defines overlapping Roman folds.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '69196f2e-fc45-476a-854d-5675b7947345'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__roman-shade-with-overlapping-folds/20260929T051531Z-thuan-mac/reference/roman shade closed_69196f2e-fc45-476a-854d-5675b7947345.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'roman-shade-with-overlapping-folds'
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
        self.path('header',(8,6),('L',(40,6)),('A',(40,14),4,4,True),('L',(8,14)),('A',(8,6),4,4,True),closed=True)
        # Front cloth fold overlays the lower fold. One shared right edge avoids doubled outline.
        self.path('front-fold',(15,14),('C',(13,32),(15,21),(14,27)),('L',(40,32)),('L',(39,14)))
        self.path('lower-fold',(17,32),('L',(14,44)),('L',(41,44)),('L',(40,32)))
        self.add_line('pull-cord',(7,14),(7,33))
        self.circle('pull-weight',7,37,4)
        self.relate('connect','header','front-fold');self.relate('connect','front-fold','lower-fold');self.relate('connect','header','pull-cord');self.relate('connect','pull-cord','pull-weight')

Drawing.exception = {'reason': 'Outlined headrail, compact fold overlap and small pull weight preserve Roman-shade structure in48px; user-authorized spacing and envelope exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'ae29dc643554f6bb69dada70056266a8641550136b36eb35bbac1e7e624d8008'}
