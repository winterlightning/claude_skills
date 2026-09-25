"""Tall open-book silhouette with gently curving matched page edges and no interior strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b5768591-30d0-458a-8f42-f8fa19890c4e'
SOURCE_PATH='pictographic-primitives/content/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.svg'
AUTHOR='gpt-6'
PLAN='Outer contour reaches (6,6)-(42,42) on centerlines. Paired curves mirror about x24. All inside strokes are removed.'
CONSTRUCTION_REFERENCE='book-open original and atomic-debug: paired page outlines; requested empty interior overrides the usual spine.'
OMISSIONS='Spine and all page-layer/interior strokes removed per reviewer feedback.'

class Drawing(Solo48):
    icon_id='open-book-empty-pages'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases=()
    keywords=('book', 'open')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.path('book',(24,12),[('C',(6,6),(19,6),(12,6)),('L',(6,36)),('C',(24,42),(12,36),(19,36)),('C',(42,36),(29,36),(36,36)),('L',(42,6)),('C',(24,12),(36,6),(29,6))],True)

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '83c6789c93b4096a17dd5a27e63d5e75714507155dc19a7805032986b37d817f', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'b5768591-30d0-458a-8f42-f8fa19890c4e'}
