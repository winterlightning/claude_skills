"""Standalone batch 16 authoring; output confined to the supplied run folders."""
import json
from pathlib import Path
import importlib.util
import cairosvg
from PIL import Image, ImageDraw, ImageOps

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = '11f861f7-9062-4cbd-a3fd-0cba990dfc4b'
SOURCE_PATH = 'icon_set/work/todo-references/folder open_11f861f7-9062-4cbd-a3fd-0cba990dfc4b.svg'
BASE = Path(__file__).parent
ROWS = json.loads((BASE/'batch-inputs.json').read_text())

HELPERS = '''
    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)
'''

# Each definition is a semantic plan, keyshape, construction reference, omissions,
# and fresh SOLO48 geometry. No source SVG coordinates are read.
DESIGNS = [
('HRECT_L','An open folder with an angled front flap.','folder-open','Tiny corner fillets on the sloping flap are reduced to round joins.', '''
        # Plan: tabbed back wall and a tilted front panel sharing the lower left.
        self.add_polyline('back',(4,40),(4,8),(16,8),(22,14),(36,14),(36,22))
        self.add_polyline('front',(4,40),(12,22),(44,22),(40,40),closed=True)
        self.relate('connect','back','front')
'''),
('HRECT_L','An open folder with a tab on its front panel.','folder-open','Small rounded corner transitions become round joins.', '''
        # Plan: detached rear lip above a broad, tapered tabbed front.
        self.add_polyline('rear',(8,8),(40,8),(40,16))
        self.add_polyline('front',(4,18),(16,18),(20,26),(44,26),(40,40),(8,40),closed=True)
'''),
('HRECT_L','An open folder with a broad upright back and skewed front.','folder-open','Minor corner fillets reduced to round joins.', '''
        # Plan: tall tabbed back; front shares both lower-left and rear-right joints.
        self.add_polyline('back',(4,40),(4,8),(16,8),(22,14),(36,14),(36,22))
        self.add_polyline('front',(4,40),(4,28),(10,22),(44,22),(40,40),closed=True)
        self.relate('connect','back','front')
'''),
('SQUARE','Two peanut kernels crossed by an allergy prohibition slash.','none','Kernel vein marks are reduced to one per visible lobe.', '''
        # Plan: two diagonal peanut silhouettes separated visually by the slash.
        self.add_bezier('upper-nut',(18,12),((22,2),(33,6),(33,15)),((33,21),(28,22),(28,22)))
        self.add_bezier('lower-nut',(17,23),((6,25),(6,38),(15,38)),((20,38),(22,32),(22,32)))
        self.add_bezier('right-nut',(29,22),((39,17),(46,29),(38,34)))
        self.add_bezier('bottom-nut',(22,34),((20,44),(30,43),(33,38)))
        self.add_line('slash',(6,6),(42,42))
        self.add_line('vein-upper',(25,14),(27,12))
        self.add_line('vein-lower',(13,31),(15,29))
'''),
('CIRCLE','A large check mark entering an open approval circle.','circle-check','None; the open ring and extended check are retained.', '''
        # Plan: cardinal three-quarter circle plus an independently drawn check.
        self.add_arc('ring-top',(4,24),(24,4),radius_x=20)
        self.add_arc('ring-bottom',(24,44),(4,24),radius_x=20)
        self.add_arc('ring-right',(44,24),(24,44),radius_x=20)
        self.add_contour('ring','ring-right','ring-bottom','ring-top')
        self.add_polyline('check',(15,22),(24,32),(40,8))
'''),
('SQUARE','A fingertip presses a horizontal touch surface with a downward arrow.','hand','Tiny impact rays are omitted to retain finger and press direction.', '''
        # Plan: bent index silhouette, long surface, central downward arrow.
        self.add_bezier('finger',(34,6),((27,8),(24,14),(20,20)),((18,23),(16,27),(14,26)),((10,24),(15,19),(17,15)),((21,8),(23,7),(25,6)))
        self.add_bezier('thumb',(34,12),((30,13),(29,18),(28,21)),((26,25),(23,21),(25,17)))
        self.add_line('surface-left',(6,32),(16,32))
        self.add_line('surface-right',(32,32),(42,32))
        self.add_line('arrow-stem',(24,32),(24,42))
        self.add_polyline('arrow-tip',(20,38),(24,42),(28,38))
        self.relate('connect','arrow-stem','arrow-tip')
'''),
('SQUARE','A forensic scalpel above a sample trace beside a DNA helix.','dna','DNA rungs reduced to the two end rungs; small blade details omitted.', '''
        # Plan: diagonal scalpel in upper left; trace below; mirrored helix right.
        self.add_bezier('scalpel',(6,28),((12,28),(19,24),(26,16)),((31,11),(34,8),(31,6)),((29,4),(26,6),(23,9)))
        self.add_line('blade-edge',(23,9),(6,28))
        self.add_contour('knife','scalpel','blade-edge',closed=True)
        self.add_line('blade-join',(20,13),(25,18))
        self.relate('connect','knife','blade-join')
        self.add_bezier('sample',(7,36),((6,44),(16,44),(17,38)),((18,34),(21,38),(22,32)))
        for side in (-1,1):
            x=36+side*6
            self.add_bezier('helix-'+str(side),(x,24),((x,32),(36-side*6,34),(36-side*6,42)))
        self.add_line('rung-top',(30,24),(42,24))
        self.add_line('rung-bottom',(30,42),(42,42))
        self.relate('connect','helix--1','helix-1','rung-top','rung-bottom')
'''),
('HRECT_M','The outlined characters 4WD denote four-wheel drive.','none','None; all three characters retained.', '''
        # Plan: hand-built 4, symmetric W, and rounded D on one baseline.
        self.add_polyline('four',(12,10),(4,30),(16,30))
        self.add_line('four-stem',(12,10),(12,38))
        self.relate('connect','four','four-stem')
        self.add_polyline('w',(20,10),(23,38),(27,22),(31,38),(34,10))
        self.add_line('d-stem',(38,10),(38,38))
        self.add_arc('d-bowl',(38,10),(38,38),radius_x=6,radius_y=14)
        self.add_contour('d','d-stem')
        self.relate('connect','d-stem','d-bowl')
'''),
('VRECT_L','A human portrait inside a frame between two detached horizontal rules.','square-user-round','Facial detail omitted as in the original; shoulder width reduced for the frame.', '''
        # Plan: mirror the bust around x=24; retain two detached frame rules.
        self.add_line('top-rule',(8,4),(40,4))
        self.add_line('bottom-rule',(8,44),(40,44))
        self.rect('frame',8,12,32,24)
        self.circle('head',24,20,4)
        # Shared human reference: detached head ends y=24, shoulders begin y=32.
        self.add_arc('shoulder-left',(16,36),(24,32),radius_x=8,radius_y=4)
        self.add_arc('shoulder-right',(24,32),(32,36),radius_x=8,radius_y=4)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','shoulders','frame')
'''),
('SQUARE','A human portrait in a frame with top and bottom bands.','square-user-round','No facial details; rounded reference neck translated to shared circular-head vocabulary.', '''
        # Plan: outer frame, two integral rails, circular head and mirrored bust.
        self.rect('frame',6,6,36,36)
        for y in (14,34):
            self.add_line('rail-'+str(y),(6,y),(42,y))
            self.relate('connect','frame','rail-'+str(y))
        self.circle('head',24,22,4)
        # Exactly 8 centerline units from head bottom 26 to shoulder top 34.
        self.add_arc('shoulders',(15,42),(33,42),radius_x=9,radius_y=8)
        self.relate('connect','shoulders','frame')
        self.relate('connect','shoulders','rail-34')
'''),
('SQUARE','A male portrait in a rounded frame with top and bottom bands.','square-user-round','Ear notches and hair texture reduced to a simple short-hair cap.', '''
        # Plan: framed bust with short hair cap; bilateral shoulder construction.
        self.rect('frame',6,6,36,36)
        for y in (14,36):
            self.add_line('rail-'+str(y),(6,y),(42,y))
            self.relate('connect','frame','rail-'+str(y))
        self.circle('head',24,23,5)
        self.add_arc('hair',(19,23),(29,23),radius_x=5)
        self.relate('connect','hair','head')
        # Head bottom 28 and shoulder crest 36 have exactly 4 visible units.
        self.add_arc('shoulders',(14,42),(34,42),radius_x=10,radius_y=6)
        self.relate('connect','shoulders','frame')
        self.relate('connect','shoulders','rail-36')
'''),
('VRECT_L','A bob-haired female portrait in a frame between two horizontal rules.','square-user-round','Small hair parting and neck corners reduced; bob silhouette retained.', '''
        # Plan: nested frame, detached rules, circular jaw and a flared bob.
        self.add_line('top-rule',(8,4),(40,4))
        self.add_line('bottom-rule',(8,44),(40,44))
        self.rect('frame',8,12,32,24)
        self.circle('head',24,21,4)
        self.add_bezier('hair',(16,29),((19,24),(15,15),(24,15)),((33,15),(29,24),(32,29)))
        self.add_line('hair-left-tip',(16,29),(19,29))
        self.add_line('hair-right-tip',(32,29),(29,29))
        self.relate('connect','hair','hair-left-tip')
        self.relate('connect','hair','hair-right-tip')
        # Head bottom 25; shoulder crest 33: exact detached ink gap 4.
        self.add_arc('shoulders',(15,36),(33,36),radius_x=9,radius_y=3)
        self.relate('connect','shoulders','frame')
'''),
('VRECT_L','A rectangular picture frame with an inset rectangular opening.','none','None; both concentric rectangles retained.', '''
        # Plan: two concentric rectangles with a shared 8-unit centerline inset.
        x,y,w,h=8,4,32,40
        self.add_polyline('outer',(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
        inset=8
        self.add_polyline('inner',(x+inset,y+inset),(x+w-inset,y+inset),
                          (x+w-inset,y+h-inset),(x+inset,y+h-inset),closed=True)
'''),
('HRECT_L','The freeCodeCamp flame logo sits between curved parentheses.','flame','Minor flame ripples reduced; both parentheses and inner flame retained.', '''
        # Plan: matched parentheses flank an intentionally asymmetric flame.
        self.add_bezier('left-paren',(8,10),((3,16),(3,32),(8,38)))
        self.add_bezier('right-paren',(40,10),((45,16),(45,32),(40,38)))
        self.add_bezier('flame',(18,40),((8,30),(25,22),(22,8)),
            ((34,13),(29,24),(32,26)),((34,29),(35,24),(35,23)),
            ((43,37),(30,40),(30,40)))
        self.add_bezier('inner-flame',(21,40),((17,35),(22,31),(25,28)),
            ((25,34),(31,33),(28,40)))
'''),
]

def author():
    for meta,(key,subject,ref,omit,body) in zip(ROWS,DESIGNS):
        out=Path(meta['result_dir']); uid=meta['source_uuid']; iid=meta['icon_id']
        module_name=iid.replace('-','_')+'_'+uid.replace('-','_')+'.py'
        header=f'''"""{subject}
Construction: {ref}. {omit}
Keyshape {key}; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {meta['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {iid!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = {tuple(meta['concept'].split())!r}
'''
        (out/module_name).write_text(header+HELPERS+'\n    def build(self):\n'+body)
        meta.update(module=module_name,keyshape=key,subject=subject,lucide_reference=ref,omissions=omit)
        (out/(iid+'.metadata.json')).write_text(json.dumps(meta,indent=2))
    (BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))

def export():
    sheet=Image.new('RGB',(840,len(ROWS)*180),'white'); d=ImageDraw.Draw(sheet)
    for i,meta in enumerate(ROWS):
        out=Path(meta['result_dir']);iid=meta['icon_id'];p=out/meta['module']
        spec=importlib.util.spec_from_file_location('drawing_'+str(i),p)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        icon=m.Drawing(); report=icon.validate_icon()
        (out/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(out/(iid+'.svg')).write_text(svg)
        for size in (48,192):
            cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/f'light-{size}.png'),output_width=size,output_height=size,background_color='#ffffff')
            # Theme previews invert the direct Cairo render; emitted SVG is untouched.
            im=Image.open(out/f'light-{size}.png').convert('RGB')
            ImageOps.invert(im).save(out/f'dark-{size}.png')
        yy=i*180
        ref=Image.open(out/'reference.png').convert('RGBA');sheet.paste(ref,(0,yy),ref)
        for j,name in enumerate(['light-192.png','dark-192.png']):
            im=Image.open(out/name).resize((144,144));sheet.paste(im,(180+j*165,yy))
        for j,name in enumerate(['light-48.png','dark-48.png']):sheet.paste(Image.open(out/name),(530+j*65,yy+40))
        d.text((665,yy+15),meta['concept'],fill='black');d.text((665,yy+40),report.status,fill='black')
        meta['validation_status']=report.status
        print(i+1,meta['concept'],report.status, len(report.errors),len(report.warnings))
    sheet.save(BASE/'batch-review.png')
    (BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))

if __name__=='__main__':
    import sys
    if '--export-only' not in sys.argv: author()
    export()
