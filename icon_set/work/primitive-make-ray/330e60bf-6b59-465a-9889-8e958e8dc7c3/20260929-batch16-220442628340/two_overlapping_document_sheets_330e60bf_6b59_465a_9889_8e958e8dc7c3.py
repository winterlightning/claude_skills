"""The rejected clone icon is a pair of angular octagons. Restore rounded sheet corners and a single clipped upper-right corner on the front sheet.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide copy: rounded rear sheet partially occluded by a complete front sheet.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='330e60bf-6b59-465a-9889-8e958e8dc7c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-overlapping-document-sheets/20260929T145934Z-thuan-mac/reference/clone_330e60bf-6b59-465a-9889-8e958e8dc7c3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-overlapping-document-sheets'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'overlapping', 'document', 'sheets')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('front',(12,14),[('L',(26,14)),('A',(30,16),5,5,True),('L',(32,18)),('A',(34,22),5,5,True),('L',(34,36)),('A',(28,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,20)),('A',(12,14),6,6,True)],True)
        path('rear',(14,14),[('L',(14,12)),('A',(20,6),6,6,True),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,28)),('A',(36,34),6,6,True),('L',(34,34))]);join('rear','front')
