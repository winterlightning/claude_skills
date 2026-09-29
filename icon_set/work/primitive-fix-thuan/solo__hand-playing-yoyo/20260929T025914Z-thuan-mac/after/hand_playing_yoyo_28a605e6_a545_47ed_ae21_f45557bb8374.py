"""Restored a side-on pinching hand, one clean slanting string, a circular yoyo with axle, and one motion arc.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide hand: continuous fingertip-to-palm flow. Source defines taut string, axle circle and swinging motion.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Two motion arcs reduced to one; axle retained as a small circular hole."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28a605e6-a545-47ed-ae21-f45557bb8374'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-playing-yoyo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'playing', 'yoyo')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the pinching hand, taut slanting string, round yoyo, center axle and motion arc. The string meets the yoyo visually and narrow finger/axle details remain clear. Natural envelope and close hand contour findings are retained. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '39cbd7d79261432b2c264121e3e9a49656a7ee5231870189ded6835f4245cc16'}

    def build(self):

        def curve(name,start,c1,c2,end): self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start;ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L':self.add_line(part,point,end)
                elif kind=='C':curve(part,point,args[0],args[1],end)
                elif kind=='A':self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                ids.append(part);point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,True)],True)

        path('hand-top',(42,6),[('L',(32,6)),('C',(22,6),(27,6),(25,4)),('L',(9,11)),('C',(11,18),(3,13),(5,21)),('L',(21,14)),('C',(29,15),(24,14),(26,16)),('L',(33,14))])
        path('hand-bottom',(16,16),[('L',(19,21)),('L',(29,23)),('C',(35,21),(32,23),(33,22)),('L',(38,19)),('L',(42,19))])
        self.add_line('string',(19,21),(25,32))
        circle('yoyo',32,36,8);circle('axle',32,36,2)
        curve('motion',(13,31),(8,34),(8,40),(13,43))
        self.relate('connect','hand-bottom','string')
 