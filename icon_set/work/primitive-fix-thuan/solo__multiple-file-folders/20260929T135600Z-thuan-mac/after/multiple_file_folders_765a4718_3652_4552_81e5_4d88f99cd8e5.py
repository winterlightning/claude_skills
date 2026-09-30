"""The rejected folders had clipped polygon corners and an incomplete rear folder. Restore rounded overlapping folders with offset tabs.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide folders: rounded tabbed enclosures and a partial rear outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='765a4718-3652-4552-81e5-4d88f99cd8e5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__multiple-file-folders/20260929T135600Z-thuan-mac/reference/folders_765a4718-3652-4552-81e5-4d88f99cd8e5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='multiple-file-folders'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('multiple', 'file', 'folders')
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

        path('rear',(16,34),[('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(17,6)),('L',(23,12)),('L',(30,12)),('A',(34,16),4,4,True),('L',(34,22))])
        path('front',(20,16),[('L',(23,16)),('L',(29,22)),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(20,42)),('A',(16,38),4,4,True),('L',(16,20)),('A',(20,16),4,4,True)],True)
        join('rear','front')
