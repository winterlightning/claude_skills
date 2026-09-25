"""A framed nonsexual female torso.
Symbol plan and construction: human_ref/user.svg and full_body_ref.png: paired human contours; source supplies headless torso and frame.
Keyshape: SQUARE balances the surrounding frame and mirrored anatomy.
Omissions: Nipple and navel dots removed to open the anatomical contours.
Review: Approved: paired chest and waist contours remain visible in both themes. Lower ends moved up one unit for frame clearance. Headless torso: no detached head/body gap applies."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f11ccece-81b6-415d-a20a-a1bdd3fceb3c'
SOURCE_PATH = 'pictographic-primitives/other/woman nude_f11ccece-81b6-415d-a20a-a1bdd3fceb3c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='woman-nude'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('woman', 'nude')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Nonsexual frontal female torso, preserving the chest and waist.
        # Shared human guidance owns smooth paired anatomy; the source has no head.
        self.rect('frame',6,6,42,42,3)
        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            n='torso-'+str(side)
            self.add_bezier(n,p(8,15),(p(9,17),p(10,20),p(9,22)),
                (p(8,25),p(5,27),p(6,29)),(p(6,31),p(7,32),p(8,33)))
        self.add_bezier('chest',(15,22),((15,27),(20,27),(24,25)),((28,27),(33,27),(33,22)))
        self.relate('connect','chest','torso--1')
        self.relate('connect','chest','torso-1')



    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # Shared rectangle parameters own radii, symmetry and attachment nodes.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)
