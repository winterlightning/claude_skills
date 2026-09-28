"""Restore tall tapered chess body below the three-point royal crown and larger finial.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: Lucide crown: balanced repeated tips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '53c44ebc-ebc2-48c3-855c-0ea9b3a726e3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chess-queen/20260925T070532Z-thuan-mac/reference/chess queen_53c44ebc-ebc2-48c3-855c-0ea9b3a726e3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Retain the circular royal finial and stepped three-point crown above a tall chess-piece body. Small local crown openings remain clear in native light and dark previews.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '3d209011cc13de6307333a51d593e6414f952df34c8f47933e6b543fb331fdb9'}
    icon_id = 'chess-queen'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('chess', 'queen')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('finial',24,8,4)
        path('piece',(12,36),[('L',(16,22)),('L',(12,19)),('L',(12,13)),('L',(19,17)),('L',(24,12)),('L',(29,17)),('L',(36,13)),('L',(36,19)),('L',(32,22)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True)],True)
        join('finial','piece')
        line('base-seam',(12,36),(36,36));join('piece','base-seam')
