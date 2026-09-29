"""Circular open halo fitted inside the canvas, detached head with exact4px ink gap above shoulders, bent raised arm and long robe with diagonal drape.
Reference comparison: The rejected holy figure became a raised arm over a triangular pedestal and lost the diagonal robe drape. The source shows a detached round head, open halo and flowing robe.
Construction references: human_ref/user.svg and full_body_ref.png: circular head and coherent human construction; supplied source defines halo and drape.
Omissions: Robe base remains open as in the reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'feefe9f2-9440-4f6a-b297-44a74f3dc1f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robed-figure-with-halo/20260929T051531Z-thuan-mac/reference/feast of the ascension_feefe9f2-9440-4f6a-b297-44a74f3dc1f9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'robed-figure-with-halo'
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
        # Circular halo: endpoints are antipodal on r17 about (26,20), keeping every stroke inside the48px canvas.
        self.add_arc('halo',(11,12),(41,28),radius_x=17,radius_y=17,sweep=True)
        self.circle('head',27,17,5)
        self.path('robe-and-arm',(19,44),('L',(22,34)),('L',(13,34)),('A',(9,30),4,4,True),('L',(9,22)),('A',(15,22),3,3,True),('L',(15,30)),('L',(33,30)),('L',(40,44)))
        self.add_line('robe-fold',(20,41),(33,30));self.relate('connect','robe-and-arm','robe-fold')
        # Head bottom22 to nearest horizontal shoulder at30:8 centerline /4 painted gap.

Drawing.exception = {'reason': 'Halo, arm and robe preserve compact natural spacing and an asymmetric envelope. User authorized visual exception; exact4px detached head gap and48px canvas are maintained.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'b56b4d9c22c17717ccdf25e2cabe8da91289e2738b9407ba89a7a969c0f2b439'}
