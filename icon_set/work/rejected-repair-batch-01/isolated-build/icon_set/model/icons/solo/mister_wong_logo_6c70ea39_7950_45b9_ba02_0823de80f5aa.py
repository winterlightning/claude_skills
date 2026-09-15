"""A character-like figure: a horizontal bar crossed by two posts above a round head, a vertical body line, two diagonal arms, and arched legs below.

Symbol plan: Character glyph with bowl head, crossed posts, stem and arched legs. Extremes (8,4)-(40,44).
Review notes: Full-body human_ref sheet informs round-ended limbs, but the source is a stylized character glyph: its bowl head and connected neck are intrinsic. Preserves crossed posts, detached arm marks and arched legs; no detached-head gap applies to its connected neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c70ea39-7950-45b9-ba02-0823de80f5aa'
SOURCE_PATH = 'pictographic-primitives/logos/mr wong logo_6c70ea39-7950-45b9-ba02-0823de80f5aa.svg'
AUTHOR = 'gpt-6'

class MisterWongLogo(Solo48):
    icon_id = 'mister-wong-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('mister-wong', 'bookmark', 'figure', 'logo', 'brand', 'social', 'character')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        chain('bar',(8,12),(16,12),(32,12),(40,12))
        self.add_contour('bar',*[f'bar-{i}' for i in range(1,4)])
        for side,x in [('l',16),('r',32)]:
         self.add_line(side+'-post',(x,4),(x,12))
         for m in (['bar-1','bar-2'] if side=='l' else ['bar-2','bar-3']):self.relate('connect',side+'-post',m)
        self.add_arc('face-left',(16,12),(24,20),radius_x=8,sweep=False)
        self.add_arc('face-right',(24,20),(32,12),radius_x=8,sweep=False)
        self.add_contour('face','face-left','face-right')
        for a,bs in [('face-left',['l-post','bar-1','bar-2']),('face-right',['r-post','bar-2','bar-3'])]:
         for b in bs:self.relate('connect',a,b)
        chain('stem',(24,20),(24,32),(24,44));self.add_contour('stem','stem-1','stem-2')
        for a in ['face-left','face-right']:self.relate('connect','stem-1',a)
        self.add_arc('legs-left',(12,44),(24,32),radius_x=12)
        self.add_arc('legs-right',(24,32),(36,44),radius_x=12)
        self.add_contour('legs','legs-left','legs-right')
        for a in ['legs-left','legs-right']:
         for b in ['stem-1','stem-2']:self.relate('connect',a,b)
        self.add_line('arm-left',(8,30),(12,26));self.add_line('arm-right',(36,26),(40,30))
