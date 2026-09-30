"""Only the current keycap is available as a reference. Its heavy corner rounding reduces the straight key edges. Rebuild it with balanced, tighter rounded corners.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide square-minus: matched quarter-circle corner construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='aaba174c-93d8-53b3-9563-a0a238407f3c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rounded-square-keyboard-key-upload-d2dede8249ae89f0/20260929T141808Z-thuan-mac/reference/rounded-square-keyboard-key-upload-d2dede8249ae89f0_aaba174c-93d8-53b3-9563-a0a238407f3c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='rounded-square-keyboard-key-upload-d2dede8249ae89f0'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('rounded', 'square', 'keyboard', 'key', 'upload', 'd2dede8249ae89f0')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        box('keycap',6,6,42,42,6)
