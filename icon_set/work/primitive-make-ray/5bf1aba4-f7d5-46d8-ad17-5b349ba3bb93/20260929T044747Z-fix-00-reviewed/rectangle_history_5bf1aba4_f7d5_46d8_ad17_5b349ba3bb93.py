"""The rejected page has square corners and loses the lower caption rule. Restore a rounded clipped-corner page, readable clock and baseline."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rectangle-history/20260929T044747Z-thuan-mac/reference/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg'
AUTHOR='gpt-6'
PLAN='The rejected page has square corners and loses the lower caption rule. Restore a rounded clipped-corner page, readable clock and baseline.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rectangle-history'
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
        self.path('page',(12,4),[('L',(32,4)),('L',(40,12)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.circle('clock',24,21,9)
        self.add_polyline('hands',(24,17),(24,21),(28,21))
        self.add_line('caption',(16,36),(32,36))

Drawing.exception = {'reason': 'Keep clock hands visibly detached inside the round dial and retain the page caption. Local dial/hand and caption clearances are compact but remain open at 48 px.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '9ac1e25158e1b54127b6aef12772e4f54e849bb9bc5eb64ff5c6727962c4f45d'}
