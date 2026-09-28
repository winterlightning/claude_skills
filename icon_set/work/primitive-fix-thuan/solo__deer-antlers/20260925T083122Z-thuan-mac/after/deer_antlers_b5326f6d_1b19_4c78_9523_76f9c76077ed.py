"""Restore three swept tines on each antler and smooth mirrored beams.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: SQUARE for the subject's natural orientation.
Construction: No useful exact Lucide match; mirrored shared curves follow the supplied antlers.
Reduction: None; three side tines per beam retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5326f6d-1b19-4c78-9523-76f9c76077ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__deer-antlers/20260925T083122Z-thuan-mac/reference/deer antlers_b5326f6d-1b19-4c78-9523-76f9c76077ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deer-antlers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('deer', 'antlers')

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

        axis=24
        for side in (-1,1):
            def pt(x,y):return (axis+side*(x-axis),y)
            name='left' if side==1 else 'right'
            # A single beam definition owns both mirrored instances.
            path(name+'-beam',pt(12,6),[('L',pt(12,14)),('C',pt(15,24),pt(12,18),pt(13,21)),('C',pt(20,36),pt(18,28),pt(20,32)),('L',pt(20,42))])
            for j,(a,b,c,d) in enumerate([((12,14),(6,10),(8,14),(6,13)),((15,24),(6,20),(10,24),(8,23)),((20,36),(10,32),(15,36),(12,35))]):
                path(f'{name}-tine-{j}',pt(*a),[('C',pt(*b),pt(*c),pt(*d))]);join(name+'-beam',f'{name}-tine-{j}')
