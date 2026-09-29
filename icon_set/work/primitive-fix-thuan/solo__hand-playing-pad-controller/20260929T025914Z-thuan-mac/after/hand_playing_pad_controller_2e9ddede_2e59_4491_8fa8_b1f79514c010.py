"""Restored a rounded 2-column pad grid, a raised index finger pressing its right pad, a rounded palm and an open musical note.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide panels-top-left: regular panel grid; hand: raised index and thumb; music-2: circular note head and upright stem.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Dense source pad matrix reduced to 2 columns and 3 rows; paired notes reduced to one open note."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2e9ddede-2e59-4491-8fa8-b1f79514c010'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-playing-pad-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'playing', 'pad', 'controller')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. The pressing hand intentionally overlaps the pad grid. Preserve the visible 2-column grid, raised index and musical note, allowing tight pad cells and note details. The cells and gesture are identifiable at 48px; removing the grid would return the rejected F-shaped fragment. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ca91d7949884a5e0dfd1457eecafb9f97867356d76cdebd0af9196e2b933be40'}

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

        path('controller',(24,10),[('L',(9,10)),('A',(6,13),3,False),('L',(6,34)),('A',(9,37),3,False),('L',(14,37))])
        self.add_line('grid-vertical',(16,10),(16,31))
        self.add_line('grid-upper',(6,20),(24,20))
        self.add_line('grid-lower',(6,29),(16,29))
        self.relate('connect','controller','grid-vertical');self.relate('connect','controller','grid-upper');self.relate('connect','controller','grid-lower')
        self.relate('connect','grid-vertical','grid-upper');self.relate('connect','grid-vertical','grid-lower')
        path('hand',(24,42),[('L',(17,33)),('C',(21,29),(13,29),(17,25)),('L',(27,35)),('L',(27,23)),('C',(33,23),(27,18),(33,18)),('L',(33,31)),('L',(37,31)),('A',(42,36),5,True),('L',(42,42))])
        circle('note',37,13,3)
        self.add_polyline('stem',(40,13),(40,6),(44,8))
        self.relate('connect','note','stem')
 