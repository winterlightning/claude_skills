"""The listener head is a tiny circle and the headphone cups are missing; the book is shallow and flat-bottomed. Restore a larger face, defined headphone cups and a deeper open book.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide headphones and book-open: round band with end cups and angled pages; shared circular human head.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8f662247-0935-46b5-ba77-cc454f1bafe3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphone-listener-reading-an-open-book/20260929T105027Z-thuan-mac/reference/audio book headphones person_8f662247-0935-46b5-ba77-cc454f1bafe3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headphone-listener-reading-an-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('headphone', 'listener', 'reading', 'an', 'open', 'book')

    def build(self):

        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        arc('band',(8,20),(40,20),16,14)
        line('ear-left',(8,20),(8,24));line('ear-right',(40,20),(40,24));join('band','ear-left');join('band','ear-right')
        circle('head',24,20,6)
        poly('book',(6,32),(24,36),(42,32),(42,40),(24,42),(6,40),closed=True)
        line('spine',(24,36),(24,42));join('spine','book')
