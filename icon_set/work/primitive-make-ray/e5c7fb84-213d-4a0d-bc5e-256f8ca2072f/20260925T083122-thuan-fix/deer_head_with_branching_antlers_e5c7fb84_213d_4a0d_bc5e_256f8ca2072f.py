"""Restore organic branching antlers and a flowing deer profile with pointed ear and long muzzle.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: VRECT_L for the subject's natural orientation.
Construction: No useful exact Lucide deer match; source profile and smooth shared branch nodes.
Reduction: Omit the eye and one fine antler tine; retain three clear tips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e5c7fb84-213d-4a0d-bc5e-256f8ca2072f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__deer-head-with-branching-antlers/20260925T083122Z-thuan-mac/reference/elk_e5c7fb84-213d-4a0d-bc5e-256f8ca2072f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deer-head-with-branching-antlers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('elk',)

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

        path('head',(10,44),[('L',(18,28)),('C',(8,20),(11,28),(9,24)),('L',(15,20)),('C',(23,24),(19,20),(21,22)),('C',(31,24),(26,21),(28,22)),('C',(40,29),(34,26),(38,28)),('C',(35,35),(40,33),(39,35)),('L',(30,35)),('C',(26,44),(26,35),(26,39))])
        path('antler',(23,24),[('C',(20,13),(23,20),(22,18)),('C',(18,4),(18,12),(18,8))])
        path('left-tine',(20,13),[('C',(8,4),(11,12),(8,9))]);join('left-tine','antler')
        path('right-tine',(23,24),[('C',(28,17),(23,20),(25,18)),('C',(36,4),(35,15),(36,10))]);join('right-tine','antler');join('antler','head');join('right-tine','head')
