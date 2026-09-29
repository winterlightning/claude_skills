"""Rejected two diagonal rings read as a chain link. Restore two hanging circular cuff housings, inset wrist openings, and a top suspension ring."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='7c088e36-de93-4207-ba03-087b8bb9a1a3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__linked-circular-handcuffs/20260929T041010Z-thuan-mac/reference/fantasy medieval bounty hunter 2_7c088e36-de93-4207-ba03-087b8bb9a1a3.svg'
AUTHOR='gpt-6'
PLAN='Rejected two diagonal rings read as a chain link. Restore two hanging circular cuff housings, inset wrist openings, and a top suspension ring.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Double rings and suspension preserved; tiny housing shoulders simplified.'
class Drawing(Solo48):
    icon_id='linked-circular-handcuffs'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('link',24,10,4)
        for n,x in [('left',14),('right',34)]:
         self.circle(n+'-cuff',x,32,10);self.circle(n+'-opening',x,32,4)
        self.add_line('chain-left',(21,13),(15,22)); self.add_line('chain-right',(27,13),(33,22))
        self.relate('connect','link','chain-left','chain-right');self.relate('connect','chain-left','left-cuff');self.relate('connect','chain-right','right-cuff')

Drawing.exception = {'reason': 'Preserve two double-ring cuffs suspended from a top link. The clear 2 px inter-ring bands and broad paired silhouette are intentional, with separate open wrist holes.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '88770ef081927dba64f23324f2f7b99ccfe7f541206cbb0fad2049671de227a7'}
