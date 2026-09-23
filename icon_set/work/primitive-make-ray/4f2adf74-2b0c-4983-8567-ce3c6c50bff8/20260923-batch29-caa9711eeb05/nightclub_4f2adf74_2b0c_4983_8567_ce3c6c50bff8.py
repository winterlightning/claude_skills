"""Four musical notes rise over a nightclub building with an arched doorway.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Building cornice rounding omitted; both note pairs retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4f2adf74-2b0c-4983-8567-ce3c6c50bff8'
SOURCE_PATH='icon_set/work/todo-references/nightclub_4f2adf74-2b0c-4983-8567-ce3c6c50bff8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='nightclub'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('nightclub',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.add_polyline('cornice',(6,28),(8,28),(40,28),(42,28))
        self.add_polyline('building',(8,28),(8,42),(20,42),(28,42),(40,42),(40,28));self.relate('connect','building','cornice')
        self.add_line('door-left',(20,42),(20,38));self.add_arc('door-top',(20,38),(28,38),radius_x=4);self.add_line('door-right',(28,38),(28,42))
        self.add_contour('door','door-left','door-top','door-right');self.relate('connect','door','building')
        for j,x in enumerate((10,30)):
            self.circle('note-'+str(j)+'-left',x,17,2);self.circle('note-'+str(j)+'-right',x+8,15,2)
            n='beam-'+str(j);self.add_polyline(n,(x+2,17),(x+2,8),(x+10,6),(x+10,15))
            self.relate('connect',n,'note-'+str(j)+'-left');self.relate('connect',n,'note-'+str(j)+'-right')

# Final visible bounds: (4, 4, 44, 44)
# Construction: Round noteheads connect to coherent stems and beam runs.
# Final reductions: Cornice thickness reduced to one rail to keep eight-unit clearance below all four music notes.
# Visual review: Building, arched doorway and all four musical notes remain present. Cornice thickness reduced to one rail; note pairs retain directional stems.
