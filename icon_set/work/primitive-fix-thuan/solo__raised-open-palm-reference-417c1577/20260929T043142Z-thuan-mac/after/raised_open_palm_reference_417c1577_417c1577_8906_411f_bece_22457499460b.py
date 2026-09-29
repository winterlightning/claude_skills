"""Restored four graduated fingers, a separate thumb fold, a tall palm and an open wrist.
Plan and comparison: The wrist and thumb anatomy were shortened or lost, so the raised hand reads as a mitten or wave.
Construction reference: hand: graduated finger caps and shared finger seams; supplied hand reference owns wrist proportions
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='417c1577-8906-411f-bece-22457499460b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raised-open-palm-reference-417c1577/20260929T043142Z-thuan-mac/reference/labor hands_417c1577-8906-411f-bece-22457499460b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='raised-open-palm-reference-417c1577'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Four finger caps share 6-unit pitch; palm keeps an open wrist and thumb crease.
        self.path('silhouette',(15,44),[
            ('L',(15,40)),('L',(8,30)),('A',(7,26),7,7,True),('L',(7,22)),
            ('A',(13,22),3,3,True),('L',(13,10)),('A',(19,10),3,3,True),
            ('L',(19,7)),('A',(25,7),3,3,True),('L',(25,9)),
            ('A',(31,9),3,3,True),('L',(31,13)),('A',(37,13),3,3,True),
            ('L',(37,29)),('A',(33,40),17,17,True),('L',(33,44))])
        for n,(x,y) in enumerate(((19,10),(25,9),(31,13))):
            p=f'finger-seam-{n}'; self.add_line(p,(x,y),(x,21)); self.relate('connect',p,'silhouette')
        self.path('thumb-crease',(13,22),[('L',(13,27)),('A',(22,34),9,9,True)])
        self.relate('connect','thumb-crease','silhouette')

Drawing.exception = {'reason': 'Four graduated fingers and the thumb require 2px internal finger spaces. Keeping the complete hand and open wrist is more recognizable than deleting a finger or shortening the palm. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'df0d0f43155f0bec979d53a13642f1e744e9eac08e9aee3cc760bfbab5571555'}
