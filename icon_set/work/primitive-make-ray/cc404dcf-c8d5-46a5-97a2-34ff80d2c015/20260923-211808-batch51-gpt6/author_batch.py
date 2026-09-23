"""Batch 51: fresh SOLO48 candidates, in supplied order, folder-only outputs."""
from pathlib import Path
import ast, importlib.util, json, io, traceback
import cairosvg
from PIL import Image, ImageDraw
SOURCE_ICON_ID = 'cc404dcf-c8d5-46a5-97a2-34ff80d2c015'
SOURCE_PATH = 'icon_set/work/todo-references/touch up_cc404dcf-c8d5-46a5-97a2-34ff80d2c015.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).resolve().parent
ROWS = json.loads((ROOT/'batch-inputs.json').read_text())
# Reuse only the generic emission helpers; every subject below is authored here.
prior = Path('icon_set/work/primitive-make-ray/4a473edf-a356-4eca-8cfd-195e95d6bc62/20260923-210743-batch50-gpt6/author_batch.py')
HELPERS = next(ast.literal_eval(n.value) for n in ast.parse(prior.read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
BOUNDS={'SQUARE':((4,4,44,44),(6,6,42,42)),'VRECT_L':((6,2,42,46),(8,4,40,44)),'HRECT_L':((2,6,46,42),(4,8,44,40)),'CIRCLE':{'center':(24,24),'centerline_radius':20,'ink_radius':22}}

SPECS=[
('CIRCLE','An upward arrow emerges from an open circle.','Concentric target envelope and mirrored arrowhead share x24.',[],'none','''
        self.add_arc('target',(8,12),(40,12),radius_x=20,large_arc=True,sweep=False)
        self.add_line('shaft',(24,4),(24,24))
        self.add_polyline('arrowhead',(18,10),(24,4),(30,10));self.join('shaft','arrowhead')
'''),
('SQUARE','A location pin hovers above a winding route on a perspective map.','Map outline is interrupted behind the pin; a continuous winding route ends on its lower edge.',[],'map-pin','''
        self.add_polyline('map',(18,14),(10,14),(6,42),(22,42),(42,42),(38,14),(36,14))
        self.path('pin',(20,14),[('A',(36,14),8,8,True),('C',(36,20),(31,26),(28,30)),('C',(25,26),(20,20),(20,14))],True)
        self.circle('pin-hole',28,14,2)
        self.add_bezier('route',(20,22),((10,25),(12,28),(23,30)),((36,32),(29,38),(22,42)))
        self.join('map','route')
'''),
('SQUARE','A trophy sits above a branching tournament diagram.','A symmetric cup owns paired handles and a central stem; two capsule nodes repeat below.',[],'trophy','''
        self.path('cup',(14,6),[('L',(34,6)),('L',(34,10)),('L',(34,18)),('A',(24,28),10,10,True),('A',(14,18),10,10,True),('L',(14,10))],True)
        self.path('handle-left',(14,10),[('L',(10,10)),('A',(6,14),4,4,False),('A',(10,18),4,4,False),('L',(14,18))])
        self.path('handle-right',(34,10),[('L',(38,10)),('A',(42,14),4,4,True),('A',(38,18),4,4,True),('L',(34,18))])
        self.join('cup','handle-left');self.join('cup','handle-right')
        self.add_line('stem',(24,28),(24,32));self.join('cup','stem')
        self.add_polyline('bracket',(12,34),(12,32),(24,32),(36,32),(36,34));self.join('stem','bracket')
        for name,x in [('node-left',6),('node-right',30)]:
            self.rect(name,x,34,12,8,4,split_x=(x+6,));self.join(name,'bracket')
'''),
('SQUARE','A tract is shown as a written sheet with a curled upper-right edge.','One tall sheet and one curved roll share exact attachment nodes; two text rules form a series.',[],'scroll','''
        self.path('sheet',(38,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(30,42)),('A',(34,38),4,4,False),('L',(34,22)),('L',(34,14)),('A',(38,6),4,8,True)],True)
        self.path('curl',(38,6),[('A',(42,14),4,8,True),('L',(42,18)),('A',(38,22),4,4,True),('L',(34,22))]);self.join('sheet','curl')
        for i,y in enumerate((16,25)):self.add_line(f'text-{i}',(15,y),(25,y))
'''),
('SQUARE','An open book carries an ascending trading chart.','Mirrored lower page curves meet at the spine; a directional zigzag rises above the open top.',[],'book-open','''
        self.path('book',(12,12),[('L',(10,12)),('A',(6,16),4,4,False),('L',(6,34)),('A',(10,38),4,4,False),('C',(18,38),(21,40),(24,42)),('C',(27,40),(30,38),(38,38)),('A',(42,34),4,4,False),('L',(42,16)),('A',(40,12),4,4,False)])
        self.add_line('spine',(24,22),(24,42));self.join('book','spine')
        self.add_polyline('chart',(14,20),(22,12),(28,18),(40,6))
        self.add_polyline('arrow',(34,6),(40,6),(40,12));self.join('chart','arrow')
'''),
('SQUARE','A news page contains a header, text rules and rising market chart.','Rounded page owns a header box and two lower content groups.',[],'file','''
        self.rect('page',6,6,36,36,4)
        self.rect('header',14,14,20,8,2)
        self.add_line('text-long',(14,29),(23,29));self.add_line('text-short',(14,36),(18,36))
        self.add_polyline('chart',(22,36),(28,30),(32,34),(38,26))
        self.add_polyline('arrow',(32,26),(38,26),(38,32));self.join('chart','arrow')
'''),
('SQUARE','A hand connects by a curved tube to a raised blood-transfusion bag.','Hand and bag retain opposite upper positions; a U-shaped tube links their lower ports.',['Outlined medical cross reduced to a centered cross stroke.'],'hand','BLOOD_HIGH'),
('SQUARE','A hand connects to a lower blood-transfusion bag.','Raised hand at left, lower bag at right, and a broad connecting tube.',['Outlined medical cross reduced to a centered cross stroke.'],'hand','BLOOD_LOW'),
('SQUARE','Two route endpoints and opposed bends surround a stop X.','Opposed semicircular turns and paired endpoint circles create a diagonal route; X stays centered.',[],'none','''
        self.circle('start',10,10,4);self.circle('end',38,38,4)
        self.path('right-turn',(28,10),[('L',(34,10)),('A',(34,26),8,8,True)])
        self.path('left-turn',(18,22),[('L',(14,22)),('A',(14,38),8,8,False),('L',(18,38))])
        self.add_line('dash-top',(21,10),(24,10));self.add_line('dash-bottom',(23,38),(26,38))
        self.cross('stop',24,24,3,True)
'''),
('VRECT_L','A transom window has a shallow upper pane above a divided lower pane.','Nested straight rectangles share a central mullion and exact 8-unit bands.',[],'none','''
        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.add_polyline('upper',(16,12),(32,12),(32,20),(24,20),(16,20),closed=True)
        self.add_polyline('lower',(16,28),(24,28),(32,28),(32,36),(24,36),(16,36),closed=True)
        self.add_line('mullion-top',(24,20),(24,28));self.join('upper','mullion-top');self.join('lower','mullion-top')
        self.add_line('mullion-bottom',(24,28),(24,36));self.join('lower','mullion-bottom');self.join('mullion-top','mullion-bottom')
'''),
('SQUARE','A sailboat on waves is surrounded by two transfer arrows.','Triangular sail, curved hull and wave form the boat; opposed curved arrows stay separate.',[],'none','''
        self.add_polyline('sail',(18,6),(6,24),(18,24),(18,30));self.add_line('mast',(18,6),(18,24));self.join('sail','mast')
        self.path('hull',(6,30),[('L',(18,30)),('L',(30,30)),('C',(26,38),(22,36),(18,36)),('C',(14,38),(10,36),(6,30))],True);self.join('sail','hull')
        self.add_bezier('wave',(18,36),((24,40),(28,34),(34,36)),((38,38),(40,34),(42,36)));self.join('hull','wave')
        self.add_bezier('transfer-top',(32,12),((38,14),(40,18),(40,22)))
        self.add_polyline('arrow-top',(36,18),(40,22),(42,18));self.join('transfer-top','arrow-top')
        self.add_bezier('transfer-bottom',(8,34),((10,39),(16,40),(20,40)))
        self.add_polyline('arrow-bottom',(16,36),(20,40),(16,42));self.join('transfer-bottom','arrow-bottom')
'''),
('SQUARE','An elevator doorway sits beside separate up and down arrows.','Nested doorway rails keep a common floor; two arrow strokes repeat vertically.',[],'none','''
        self.add_polyline('door',(6,42),(6,6),(30,6),(30,42),(22,42),(14,42),(6,42))
        self.add_polyline('opening',(14,42),(14,14),(22,14),(22,42));self.join('door','opening')
        self.add_line('up-shaft',(38,6),(38,20));self.add_polyline('up-head',(34,10),(38,6),(42,10));self.join('up-shaft','up-head')
        self.add_line('down-shaft',(38,28),(38,42));self.add_polyline('down-head',(34,38),(38,42),(42,38));self.join('down-shaft','down-head')
'''),
('SQUARE','A rounded outer square encloses a smaller rounded square.','Two centered rounded rectangles with a 9-unit separating band.',[],'tv','''
        self.rect('outer',6,6,36,36,6)
        self.rect('inner',15,15,18,18,3)
'''),
('SQUARE','A square trapdoor panel sits inside a rounded frame with a lower seam.','Centered inner panel and outer frame share the bottom seam attachment axis.',[],'tv','''
        self.rect('frame',6,6,36,36,4,split_x=(24,))
        self.add_polyline('panel',(15,15),(33,15),(33,33),(24,33),(15,33),closed=True)
        self.add_line('seam',(24,33),(24,42));self.join('panel','seam');self.join('frame','seam')
'''),
('VRECT_L','A lidded trash can contains three horizontal list lines.','A shared handle, rounded lid and bin construction owns the repeated list.',[],'trash-2','TRASH_LINES'),
('VRECT_L','A lidded trash can contains a clock face.','A shared handle, rounded lid and bin construction encloses a circular clock.',[],'trash-2','TRASH_CLOCK'),
('VRECT_L','A lidded trash can contains a three-item bulleted list.','The bin owns repeated bullet-and-rule rows.',['Small square bullets reduced to round dots for native-size readability.'],'trash-2','TRASH_LIST'),
('VRECT_L','A lidded trash can contains a plus sign.','A shared bin silhouette encloses a centered four-ray plus.',[],'trash-2','TRASH_PLUS'),
('HRECT_L','A rounded warning triangle contains an exclamation mark.','Mirrored outer curves preserve exact horizontal extrema; the exclamation has a short stem and detached dot.',[],'triangle-alert','''
        self.path('triangle',(24,8),[('C',(26,8),(27,10),(28,12)),('L',(42,34)),('C',(43,36),(44,37),(44,38)),('C',(44,40),(42,40),(40,40)),('L',(8,40)),('C',(6,40),(4,40),(4,38)),('C',(4,37),(5,36),(6,34)),('L',(20,12)),('C',(21,10),(22,8),(24,8))],True)
        self.add_line('stem',(24,22),(24,24));self.add_dot('dot',(24,32))
'''),
('SQUARE','A road with broken centerline passes a location pin.','Converging road edges and a repeated centerline retain perspective; the pin occupies the upper right.',[],'map-pin','''
        self.add_line('road-left',(6,42),(18,6));self.add_line('road-right',(38,30),(42,42))
        self.add_line('center-far',(24,22),(24,26));self.add_line('center-near',(24,34),(24,42))
        self.path('pin',(26,14),[('A',(42,14),8,8,True),('C',(42,20),(37,25),(34,28)),('C',(31,25),(26,20),(26,14))],True)
        self.circle('pin-hole',34,14,3)
'''),
]

def blood(high):
    if high:
        hand='''
        self.path('hand',(8,42),[('L',(8,30)),('C',(8,26),(6,24),(6,20)),('C',(6,13),(7,6),(14,6)),('C',(17,6),(19,7),(18,11)),('L',(17,20)),('L',(21,17)),('C',(26,13),(25,22),(20,28)),('L',(20,34))])
        self.path('tube',(14,30),[('L',(14,34)),('A',(22,42),8,8,False),('L',(28,42)),('A',(36,34),8,8,False),('L',(36,26))])
'''
        y=6
    else:
        hand='''
        self.path('hand',(10,28),[('L',(10,24)),('C',(6,22),(6,17),(6,12)),('A',(14,6),8,6,True),('A',(22,14),8,8,True),('L',(22,16)),('C',(28,16),(28,22),(22,27)),('L',(22,35))])
        self.add_line('cuff',(10,28),(14,28));self.join('hand','cuff')
        self.path('tube',(14,24),[('L',(14,34)),('A',(22,42),8,8,False),('L',(34,42)),('A',(36,40),2,2,False)])
'''
        y=20
    return hand+f'''
        self.path('bag',(34,{y}),[('L',(38,{y})),('A',(42,{y+4}),4,4,True),('L',(42,{y+12})),('A',(38,{y+16}),4,4,True),('L',(38,{y+20})),('L',(34,{y+20})),('L',(34,{y+16})),('A',(30,{y+12}),4,4,True),('L',(30,{y+4})),('A',(34,{y}),4,4,True)],True)
        self.cross('medical-cross',36,{y+8},3)
        self.join('tube','bag')
'''

def trash(kind):
    body='''
        self.rect('lid',8,12,32,8,4,split_x=(18,30))
        self.path('handle',(18,12),[('L',(18,8)),('A',(22,4),4,4,True),('L',(26,4)),('A',(30,8),4,4,True),('L',(30,12))]);self.join('lid','handle')
        self.path('bin',(12,20),[('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(36,20))]);self.join('lid','bin')
'''
    if kind=='TRASH_PLUS':body+="        self.cross('plus',24,32,4)\n"
    elif kind=='TRASH_CLOCK':body+='''
        self.circle('clock',24,32,8)
        self.add_polyline('hands',(24,27),(24,32),(28,32))
'''
    elif kind=='TRASH_LINES':body+='''
        for i,y in enumerate((26,32,38)):self.add_line(f'list-{i}',(21,y),(27,y))
'''
    else:body+='''
        for i,y in enumerate((26,32,38)):
            self.add_dot(f'bullet-{i}',(20,y));self.add_line(f'list-{i}',(28,y),(30,y))
'''
    return body

def main():
    for i,(row,spec) in enumerate(zip(ROWS,SPECS)):
        out=Path(row['result_dir'])
        if (out/'result.json').exists():continue
        key,subject,plan,omissions,ref,body=spec
        if body.startswith('BLOOD_'):body=blood(body=='BLOOD_HIGH')
        if body.startswith('TRASH_'):body=trash(body)
        refs=['Supplied SVG, rendered and visually inspected.']
        refs += [f'Lucide original/{ref}.svg and atomic-debug/{ref}.svg: coherent contours, shared nodes, consistent rounding; re-authored on SOLO48.' if ref!='none' else 'No useful local Lucide subject match used; shared geometric construction principles applied.']
        if ref=='hand':refs+=['Shared human-reference.md and human_ref references: coherent human-part construction; no detached head occurs.']
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
        source=f'''"""{subject}
Plan: {plan}
Keyshape {key}: exact ink and centerline envelopes {BOUNDS[key]!r}.
References: {' '.join(refs)}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
'''+HELPERS+'\n    def build(self):\n'+body
        (out/module_name).write_text(source)
        data=dict(row,keyshape=key,keyshape_bounds=BOUNDS[key],subject=subject,construction_plan=plan,omissions=omissions,references=refs,python=module_name)
        try:
            s=importlib.util.spec_from_file_location(f'batch51_{i}',out/module_name);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
            icon=m.Drawing();report=icon.validate_icon();data['validation_status']=report.status;(out/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(out/(row['icon_id']+'.svg')).write_text(svg);data['export_status']='success'
            for size in (48,192):
                alpha=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size))).convert('RGBA').getchannel('A')
                for theme,bg,ink in [('light','white','black'),('dark','#16191d','#f4f5f6')]:
                    im=Image.new('RGB',(size,size),bg);im.paste(ink,(0,0,size,size),alpha);im.save(out/f'{theme}-{size}.png')
        except Exception:
            data.setdefault('validation_status','error');data['export_status']='error';data['error']=traceback.format_exc();(out/'error.txt').write_text(data['error'])
        (out/'attempt-findings.json').write_text(json.dumps(data,indent=2)+'\n');print(i+1,row['concept'],data['validation_status'],data['export_status'],flush=True)
    sheet=Image.new('RGB',(1080,7*270),'#dadde0');d=ImageDraw.Draw(sheet)
    for i,row in enumerate(ROWS):
        out=Path(row['result_dir']);x=i%3*360;y=i//3*270;d.text((x+4,y+4),f"{i+1}. {row['concept'][:36]}",fill='black')
        for j,theme in enumerate(('light','dark')):
            if (out/f'{theme}-192.png').exists():
                sheet.paste(Image.open(out/f'{theme}-192.png').resize((160,160)),(x+j*180,y+26));sheet.paste(Image.open(out/f'{theme}-48.png'),(x+j*180+56,y+198))
    sheet.save(ROOT/'authored-review.png')
if __name__=='__main__':main()
