"""Fresh reference repair. Construction reference: Lucide book.
Keyshape VRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '49781b64-ccc2-5e53-93f8-360efdda93fc'
SOURCE_PATH = 'pictographic-primitives/content/book close_49781b64-ccc2-5e53-93f8-360efdda93fc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'closed-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('book', 'close')

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):

        # Plain closed cover, rounded spine and page turn; no invented bookmark.
        self.path('cover',(8,38),('L',(8,10)),('A',(14,4),6,6,True),('L',(38,4)),('A',(40,6),2,2,True),('L',(40,32)),('L',(40,42)),('A',(38,44),2,2,True),('L',(14,44)),('A',(8,38),6,6,True),closed=True)
        self.path('pages',(8,38),('A',(14,32),6,6,True),('L',(40,32)))
        self.relate('connect','cover','pages')

    icon_id = 'book-close-49781b64'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
