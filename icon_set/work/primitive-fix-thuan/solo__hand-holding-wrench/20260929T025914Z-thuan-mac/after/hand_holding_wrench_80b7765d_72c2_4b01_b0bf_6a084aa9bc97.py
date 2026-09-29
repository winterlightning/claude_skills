"""Restored an open wrench jaw, diagonal handle, three rounded gripping fingers, and a thumb/palm wrapping around the tool.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide wrench: open angular jaw and tapered handle. Lucide hand-grab: stepped rounded fingers and coherent palm.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Four source fingers reduced to three readable gripping arcs; tool mouth retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '80b7765d-72c2-4b01-b0bf-6a084aa9bc97'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'holding', 'wrench')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. The grip requires fingers to overlap the diagonal tool handle. Preserve an unmistakable open angular wrench jaw and three distinct gripping arcs. Narrow finger channels and intentional tool/hand occlusions retain the action at 48px; a simplified hook and crossed bars would lose the meaning. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd8873f3d99fe51dc0ff34314d9fac07a10d3fdd04bcb197f087d46f98b090e90'}

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

        path('wrench-head',(23,20),[('C',(36,6),(20,11),(27,3)),('L',(31,11)),('L',(36,16)),('L',(42,10)),('C',(30,24),(46,22),(38,29))])
        path('handle',(30,24),[('L',(13,42)),('C',(7,36),(8,47),(3,41)),('L',(12,31))])
        path('finger-top',(14,22),[('C',(19,17),(10,18),(15,13)),('L',(24,22)),('C',(19,27),(28,27),(23,31)),('L',(14,22))],True)
        path('finger-mid',(10,27),[('C',(14,22),(6,23),(9,19))])
        path('finger-low',(7,32),[('C',(10,27),(3,29),(5,24)),('L',(16,33))])
        path('palm',(37,42),[('C',(32,34),(33,39),(31,37)),('C',(34,27),(32,31),(35,30)),('L',(26,19))])
        self.add_line('wrist',(18,37),(23,42))
 