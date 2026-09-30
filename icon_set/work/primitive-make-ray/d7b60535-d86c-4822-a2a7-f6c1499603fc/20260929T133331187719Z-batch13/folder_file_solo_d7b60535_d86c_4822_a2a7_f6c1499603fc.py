"""Restore a tall front folder and rounded rear document with a text line.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The folder is a shallow tray and the document has no content marks.
Construction reference: Lucide folder and square: clear folder tab and tangent rounded corners.
Omissions: Second text line omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='d7b60535-d86c-4822-a2a7-f6c1499603fc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__folder-file-solo/20260929T132621Z-thuan-mac/reference/folder file_d7b60535-d86c-4822-a2a7-f6c1499603fc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='folder-file-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('folder', 'file')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                k,end,*a=step; name=f'{n}-{i}'
                if k=='L': self.add_line(name,p,end)
                elif k=='A': self.add_arc(name,p,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='B': self.add_bezier(name,p,(a[0],a[1],end))
                members.append(name);p=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=4):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('file',(14,25),[('L',(14,10)),('A',(18,6),4,4,True),('L',(32,6)),('L',(42,16)),('L',(42,35)),('A',(38,39),4,4,True),('L',(30,39))])
        path('folder',(6,29),[('A',(10,25),4,4,True),('L',(16,25)),('L',(21,29)),('L',(26,29)),('A',(30,33),4,4,True),('L',(30,38)),('A',(26,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,29))],True)
        line('text',(22,17),(31,17));join('file','folder')
