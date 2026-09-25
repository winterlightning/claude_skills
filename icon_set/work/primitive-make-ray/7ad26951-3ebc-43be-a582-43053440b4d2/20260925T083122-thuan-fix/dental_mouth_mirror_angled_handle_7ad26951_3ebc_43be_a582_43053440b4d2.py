"""Restore a smooth diagonal capsule handle and oval mirror joined by a thin angled neck.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: SQUARE for the subject's natural orientation.
Construction: Lucide search: clean mirror/head and handle junction; original oval retained.
Reduction: Reflective marks omitted as in the source; oval perspective retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7ad26951-3ebc-43be-a582-43053440b4d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dental-mouth-mirror-angled-handle/20260925T083122Z-thuan-mac/reference/dentistry tooth mirror_7ad26951-3ebc-43be-a582-43053440b4d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dental-mouth-mirror-angled-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('dentistry', 'tooth', 'mirror')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('mirror',(6,36),[('C',(14,30),(6,32),(10,30)),('C',(20,32),(17,30),(19,31)),('C',(22,36),(21,33),(22,34)),('C',(14,42),(22,40),(18,42)),('C',(6,36),(10,42),(6,40))],True)
        path('grip',(26,20),[('L',(36,10)),('C',(42,16),(40,6),(46,12)),('L',(32,26)),('C',(26,26),(30,28),(28,28)),('C',(26,20),(24,24),(24,22))],True)
        line('neck',(20,32),(26,26));join('neck','mirror');join('neck','grip')
