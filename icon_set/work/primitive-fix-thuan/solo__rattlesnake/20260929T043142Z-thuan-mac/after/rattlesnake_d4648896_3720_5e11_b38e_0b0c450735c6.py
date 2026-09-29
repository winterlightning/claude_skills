"""Restored an S-shaped snake with a separate segmented rattle, a broad head, eyes and a forked tongue.
Plan and comparison: The tail is enclosed like a handle and the broad snake head lacks eyes and a forked tongue.
Construction reference: no useful exact Lucide match; concentric body bends and minimal facial marks
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d4648896-3720-5e11-b38e-0b0c450735c6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rattlesnake/20260929T043142Z-thuan-mac/reference/reptile rattlesnake_d4648896-3720-5e11-b38e-0b0c450735c6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rattlesnake'
    keyshape=Keyshape.SQUARE
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

        # One continuous tubular body ends in a widened head; the rattle is a detached series.
        self.path('snake',(5,26),[('L',(5,33)),('A',(23,33),9,9,False),('L',(23,16)),('A',(31,16),4,4,True),('L',(31,21)),('L',(26,25)),('A',(34,38),15,15,False),('A',(44,25),15,15,False),('L',(39,21)),('L',(39,16)),('A',(17,16),11,11,False),('L',(17,33)),('A',(11,33),3,3,True),('L',(11,26)),('A',(5,26),3,3,False)],True)
        self.add_dot('eye-left',(32,27)); self.add_dot('eye-right',(38,27))
        self.add_polyline('tongue',(35,38),(35,42),(32,45)); self.relate('connect','tongue','snake')
        self.add_line('fork',(35,42),(38,45)); self.relate('connect','fork','tongue')
        for n,y in enumerate((19,13,7)):
            self.add_line(f'rattle-{n}',(6+n,y),(10-n,y)) if n<2 else self.add_dot(f'rattle-{n}',(8,y))

Drawing.exception = {'reason': 'The tubular S-body, head eyes and segmented rattle use local gaps below 4px. The inner body channel remains open and the head, tail and forked tongue remain identifiable. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '3f871499f58a18ad311db6f4cb40f9502862118d25e6a2589d8501aa591ce09e'}
