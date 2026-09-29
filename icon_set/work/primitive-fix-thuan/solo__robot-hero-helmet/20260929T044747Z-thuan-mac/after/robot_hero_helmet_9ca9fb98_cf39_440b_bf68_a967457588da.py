"""Rejected face is an M-shaped slit without eyes and the crest is a square tab. Restore a rounded helmet crest, ear pods, broad face opening and two eyes."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9ca9fb98-cf39-440b-bf68-a967457588da'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__robot-hero-helmet/20260929T044747Z-thuan-mac/reference/megaman_9ca9fb98-cf39-440b-bf68-a967457588da.svg'
AUTHOR='gpt-6'
PLAN='Rejected face is an M-shaped slit without eyes and the crest is a square tab. Restore a rounded helmet crest, ear pods, broad face opening and two eyes.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='robot-hero-helmet'
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
        self.path('shell-left',(12,35),[('C',(6,23),(8,33),(6,29)),('C',(18,9),(6,14),(12,10))])
        self.path('shell-right',(30,9),[('C',(42,23),(36,10),(42,14)),('C',(36,35),(42,29),(40,33))])
        self.path('face',(24,25),[('C',(12,24),(17,19),(12,19)),('C',(10,33),(10,26),(10,30)),('C',(24,42),(12,39),(18,42)),('C',(38,33),(30,42),(36,39)),('C',(36,24),(38,30),(38,26)),('C',(24,25),(36,19),(31,19))],True)
        self.path('crest',(18,6),[('L',(30,6)),('L',(30,15)),('A',(18,15),6,6,True),('L',(18,6))],True)
        self.path('ear-left',(7,18),[('L',(4,18)),('L',(4,28)),('L',(8,28))]);self.path('ear-right',(41,18),[('L',(44,18)),('L',(44,28)),('L',(40,28))])
        self.add_dot('eye-left',(19,30));self.add_dot('eye-right',(29,30))
        self.relate('connect','shell-left','face','crest','ear-left');self.relate('connect','shell-right','face','crest','ear-right')

Drawing.exception = {'reason': 'Retain helmet crest, ear pods, scalloped face opening and two eyes. Local shell/face contacts and compact eye clearances preserve the recognizable helmeted hero.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '89a9aaf28017f8eee03b7817d5b7032c6345842c57b44a61633dbf9e6aaac1ba'}
