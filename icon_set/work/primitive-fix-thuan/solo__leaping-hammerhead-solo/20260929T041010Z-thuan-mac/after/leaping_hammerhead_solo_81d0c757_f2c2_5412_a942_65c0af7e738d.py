"""Rejected angular mark loses the shark body and hammer-shaped head. Restore a broad transverse head, smooth arched body, dorsal fin and forked tail."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='81d0c757-f2c2-5412-a942-65c0af7e738d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__leaping-hammerhead-solo/20260929T041010Z-thuan-mac/reference/shark hammer fish_81d0c757-f2c2-5412-a942-65c0af7e738d.svg'
AUTHOR='gpt-6'
PLAN='Rejected angular mark loses the shark body and hammer-shaped head. Restore a broad transverse head, smooth arched body, dorsal fin and forked tail.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='leaping-hammerhead-solo'
    keyshape=Keyshape.VRECT_L
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
        self.path('shark',(8,22),[('C',(24,4),(8,13),(16,5)),('L',(30,9)),('L',(24,13)),('C',(33,19),(28,15),(31,17)),('L',(40,15)),('L',(37,26)),('C',(35,38),(39,31),(40,35)),('C',(23,44),(32,42),(27,44)),('L',(26,36)),('L',(17,33)),('C',(28,31),(24,35),(28,34)),('C',(20,22),(28,27),(22,29)),('L',(17,17)),('L',(14,26)),('L',(8,22))],True)

Drawing.exception = {'reason': 'The hammer-shaped head, dorsal fin, curved body and forked tail need local tapered openings. These preserve shark identity without adding fine strokes.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '880d9e5f86fa5c0bc1075495feb998630cb33e61c43fd5768a8dce295bdbfd57'}
