from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='3d250c41-6017-4d1f-9278-42fadf1fc93d'
SOURCE_PATH='pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg'
AUTHOR='gpt-6'
PLAN='LIKE uses typeface v2 at0.85 uniform centerline scale. Panel expanded by2 units per side within the same48 canvas to keep glyphs distinct; text spacing and exact keyshape fit are approved exceptions.'
CONSTRUCTION_REFERENCES='Lucide rectangle-ellipsis original and atomic-debug: rounded horizontal enclosure; supplied reference governs LIKE.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='rectangle-like-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'like', 'text')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


    def typeface_v2(self,text,scale,tracking,cx,cy):
        # Reuse the supplied v2 glyph curves; apply a uniform centerline fit.
        # Global stroke stays4. Explicit user exception owns text spacing/grid.
        from pathlib import Path
        import json
        from svgpathtools import parse_path,Line,CubicBezier
        from icon_set.model.primitives import Bezier,Point
        catalog={'source': 'icon_set/typeface/glyphs-v2.json', 'glyphs': [{'icon_id': 'letter-l-uppercase', 'character': 'L', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [7.0, 2.0, 10.9999, 17.0], 'measurement': 'source-body-band', 'paths': ['M 10.9999,17.0 C 9.88814,17.0 7.09011,17.0 7.00293,17.0 M 7.0,16.9916 L 7.0,2.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '2cc63d1908ebe2f3df0695cd3ff412876777d222a62bc03192a8dcbf5434d461', 'source_path': 'Letters/new/L.svg', 'source_sha256': '3065e114cd4fabca478d8530643b8a9d602b7eb5a921c5d3c026275ade055cd5', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 7.9999, 'ink_height': 19.0, 'ink_left': 5.0, 'ink_top': 0.0, 'centerline_width': 3.9999000000000002, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-i-uppercase', 'character': 'I', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [9.0, 2.0, 9.00143, 17.0], 'measurement': 'source-body-band', 'paths': ['M 9.00143,2.0 L 9.0,17.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '16029903932630f59fd8f2c434a4f40c25567b6403a80052c0ff3b9cf0c33da1', 'source_path': 'Letters/new/I.svg', 'source_sha256': '07b3850693618f7de927c01916485b560c0181079256b2bcad473b51ed313f44', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 4.001429999999999, 'ink_height': 19.0, 'ink_left': 7.0, 'ink_top': 0.0, 'centerline_width': 0.0014299999999991542, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-k-uppercase', 'character': 'K', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [6.0, 2.0, 14.0, 17.0], 'measurement': 'source-body-band', 'paths': ['M 14.0,17.0 L 6.0,9.0', 'M 13.0,2.0 L 6.0,9.0', 'M 6.0,2.0 L 6.0,17.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '9e329f0906942a3c2e69504e24672157f4b45a0da54bdd25318a34dff3fba438', 'source_path': 'Letters/new/K.svg', 'source_sha256': '19257b5918ce781cfec9cf09041fdb89cfddddfe4efa57d329a0e8c0b9c206e0', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.0, 'ink_height': 19.0, 'ink_left': 4.0, 'ink_top': 0.0, 'centerline_width': 8.0, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-e-uppercase', 'character': 'E', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [5.0, 2.0, 13.0, 16.9999], 'measurement': 'source-body-band', 'paths': ['M 5.0,9.49001 L 5.0,2.5047 C 5.0,2.23264 5.22033,2.01198 5.49239,2.01156 L 13.0,2.0', 'M 13.0,16.9998 L 5.49315,16.9999 C 5.22079,16.9999 5.0,16.7791 5.0,16.5068 L 5.0,9.48975', 'M 10.0,10.0 L 5.0,10.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '26d7440898c6bbdaf45ca6e5d207cb92388c253805f5e908cc788eef8c6c4268', 'source_path': 'Letters/new/E.svg', 'source_sha256': 'ed4480e4e7358fffb655c96829eba271e457c27afc79e274944e8839ba3045b0', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.0, 'ink_height': 18.9999, 'ink_left': 3.0, 'ink_top': 0.0, 'centerline_width': 8.0, 'centerline_height': 14.9999, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}]}
        glyphs={g['character']:g for g in catalog['glyphs']}
        width=sum((glyphs[c]['bounds'][2]-glyphs[c]['bounds'][0])*scale+4 for c in text)+tracking*(len(text)-1)
        cursor=cx-width/2+2
        top=cy-15*scale/2
        self.typeface_placements=[]
        for index,c in enumerate(text):
            g=glyphs[c];dx=cursor-g['bounds'][0]*scale;dy=top-g['body_top']*scale
            self.typeface_placements.append(dict(character=c,glyph_id=g['icon_id'],scale=scale,translate=[dx,dy],source_path=g['source_path'],path_sha256=g['svg_sha256']))
            def point(z):return (round(z.real*scale+dx,3),round(z.imag*scale+dy,3))
            for pi,d in enumerate(g['paths']):
                for si,sub in enumerate(parse_path(d).continuous_subpaths()):
                    n=f'text-{index}-{c}-{pi}-{si}';members=[]
                    for j,segment in enumerate(sub):
                        ident=n+'-'+str(j);members.append(ident)
                        if isinstance(segment,Line):self.add_line(ident,point(segment.start),point(segment.end))
                        elif isinstance(segment,CubicBezier):self.primitives.append(Bezier(ident,Point(*point(segment.start)),Point(*point(segment.end)),((point(segment.control1),point(segment.control2),point(segment.end)),)))
                        else:raise ValueError('Unexpected v2 glyph primitive')
                    self.add_contour(n,*members,closed=(sub.start==sub.end))
            cursor+=(g['bounds'][2]-g['bounds'][0])*scale+4+tracking

    def build(self):
        self.box('panel',2,8,46,40,4)
        self.typeface_v2('LIKE',0.85,1,24,24)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'LIKE uses typeface v2 at0.85 uniform centerline scale. Panel expanded by2 units per side within the same48 canvas to keep glyphs distinct; text spacing and exact keyshape fit are approved exceptions.', 'scope': ['typeface-v2 fractional coordinates', 'glyph spacing', 'expanded panel keyshape fit'], 'svg_sha256': 'a7748532b70ca526b6776ed0f0db2542954c9a27a17f006b6214d8f0ed790f9c', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'ca2df363f9afb9d6a063032cc5cca379fc636f25e8560d26ccd0c56ade8f1e9b', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '3d250c41-6017-4d1f-9278-42fadf1fc93d'}
