"""Fresh round-two attempts; previous runs remain read-only."""
from pathlib import Path
import json,re,importlib.util,textwrap
import cairosvg

AUTHOR='gpt-6'
HERE=Path(__file__).parent
ROWS=json.loads((HERE/'batch-inputs.json').read_text())
SOURCE_ICON_ID=tuple(r['source_uuid'] for r in ROWS)
SOURCE_PATH=tuple(r['reference_path'] for r in ROWS)

PLANS=[
'Retain bindings, header and horizontal 18+; rebalance digit and operator spacing without dropping characters.',
'Retain oval speech bubble and PM; use a broader P bowl and narrower shared-axis M.',
'A wrapped burrito with bowed seam and diagonal fold; split both curved contact locations at integer shared endpoints.',
'Hand holding a portrait business card; flatten the upper hand clearance and shorten the shoulder bowl while retaining the portrait.',
'Approved contract held in two hands; enlarge the sheet and separate text rows; circular approval seal retained.',
'Three-binding calendar with 2+1; redistribute the three glyphs across a wide keyshape.',
'Calendar with a continuous telephone receiver; simplify the handset to a centerline hook with distinct earpiece ends.',
'Calendar with a three-sector pie; enlarge the content area and use exact radial attachment points.',
'Mirrored car body and lightning zigzag; leave real clearance at the roof and base.',
'Broader mirrored car roof with a smaller double-ended wrench; repeated jaws share radius and shaft height.',
'Overlapping spade and diamond cards; widen the front card and rebalance its spade inside the available opening.',
'Three outlined diamonds on an upright playing card; enlarge corner diamonds and reduce the center to test the spacing budget.',
'Two suit cards and foreground die; restore the reference two-pip face and enlarge the die opening.',
'Three hearts on an upright playing card; reduce the central suit while preserving both opposing corner marks.',
'Child symbol in a square card; isolate straight shoulder junction for an exact detached-head gap and curve the raised arms outside it.',
'Interrupted battery and charge bar with central lightning; use a centerline bolt to release clearance while retaining the terminal.',
'Four mirrored charging waves around a narrow centerline bolt; shared nested arc parameters preserve repetition.',
'Two overlapping speech bubbles and a front heart; redistribute front-bubble area and use an oblique rear tail.',
'Check above a pointing hand; lower the fingertip and enlarge the gap in the occluded check edge.',
'Three overlapping wafer-like pieces above a bowl; separate stacked edges and attach the right flourish at a true contour point.'
]

def replace_build(src,body):
    return src[:src.index('    def build(self):')]+ '    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'

def author():
    for i,r in enumerate(ROWS):
        o=Path(r['result_dir']);parent=Path(r['parent_result']).parent
        old=next(parent.glob('*.py'));src=old.read_text()
        src=re.sub(r'^SOURCE_PATH\s*=.*$',f"SOURCE_PATH = {r['reference_path']!r}",src,flags=re.M)
        src=re.sub(r'^AUTHOR\s*=.*$',f"AUTHOR = {AUTHOR!r}",src,flags=re.M)
        src=re.sub(r'^    icon_id\s*=.*$',f"    icon_id = {r['icon_id']!r}",src,flags=re.M)
        src=src.replace('class Drawing(Solo48):',f'PLAN = {PLANS[i]!r}\nPARENT_RESULT = {r["parent_result"]!r}\n\nclass Drawing(Solo48):')
        r['parent_module']=str(old);r['plan']=PLANS[i];r['omissions']=[]
        if i==0:
            src=src.replace('(13,26),(16,24),(16,35)','(12,26),(14,24),(14,34)')
            src=src.replace('24,26,2','23,26,3').replace('24,32,4','23,32,3')
            src=src.replace('(32,30),(35,30),(38,30)','(33,30),(36,30),(39,30)').replace('(35,27),(35,30),(35,33)','(36,27),(36,30),(36,33)')
        elif i==1:
            src=src.replace('(14,29),(14,22),(14,16)','(14,28),(14,24),(14,16)')
            src=src.replace('("A",(17,22),3,3,True),("L",(14,22))','("A",(17,24),4,4,True),("L",(14,24))')
            src=src.replace('(25,29),(28,16),(31,25),(34,16),(37,29)','(29,28),(29,17),(32,24),(35,17),(35,28)')
        elif i==2:
            src=replace_build(src,'''
            self.add_line('top',(18,10),(30,10))
            self.add_arc('right',(30,10),(30,38),radius_x=14)
            self.add_line('bottom',(30,38),(18,38))
            self.add_arc('left-lower',(18,38),(4,24),radius_x=14)
            self.add_arc('left-upper',(4,24),(18,10),radius_x=14)
            self.add_contour('outline','top','right','bottom','left-lower','left-upper',closed=True)
            self.add_bezier('seam-upper',(18,10),((20,12),(22,14),(24,18)))
            self.add_bezier('seam-lower',(24,18),((28,26),(26,36),(18,38)))
            self.add_contour('seam','seam-upper','seam-lower')
            self.add_line('fold',(4,24),(24,18))
            self.relate('connect','seam-upper','top','left-upper')
            self.relate('connect','seam-lower','bottom','left-lower')
            self.relate('connect','fold','left-lower','left-upper','seam-upper','seam-lower')
            ''')
        elif i==3:
            src=src.replace("self.add_polyline('hand-back',(24,10),(30,6),(42,10))","self.add_bezier('hand-back',(24,6),((30,6),(36,6),(42,6)))")
            src=src.replace("(10,40),(22,40),radius_x=6,sweep=True","(12,37),(20,37),radius_x=4,radius_y=3,sweep=True")
        elif i==4:
            src=src.replace('(26,44),(16,44),(16,36),(16,4),(36,4),(36,30)','(26,44),(14,44),(14,36),(14,4),(38,4),(38,28)')
            src=src.replace('(8,6),(8,28),(16,36)','(8,6),(8,28),(14,36)')
            src=src.replace("circle('seal',26,15,6)","circle('seal',26,15,7)")
            src=src.replace("self.add_line('text',(23,27),(28,27))","self.add_line('text',(22,27),(28,27))\n        self.add_line('text-lower',(22,35),(24,35))")
        elif i==5:
            src=src.replace('Keyshape.SQUARE','Keyshape.HRECT_L')
            # Widen the complete calendar; every glyph is still retained in order.
            a=src.index('    def calendar(');b=src.index('    def build',a)
            cal=src[a:b].replace('(6,','(4,').replace('(42,','(44,').replace('(10,','(8,').replace('(38,','(40,').replace(',42)',',40)').replace(',38)',',36)').replace('(x,6)','(x,8)').replace('(x,10)','(x,12)').replace(',10)',',12)')
            src=src[:a]+cal+src[b:]
            src=src.replace('(12,23)','(13,23)').replace('(12,34)','(13,31)').replace('(20,34)','(20,31)')
            src=src.replace('(24,27),(28,27),(32,27)','(27,26),(29,26),(31,26)').replace('(28,23),(28,27),(28,31)','(29,24),(29,26),(29,28)')
            src=src.replace('(34,22),(37,20),(37,34)','(37,22),(39,20),(39,31)')
        elif i==6:
            src=src.replace('Keyshape.SQUARE','Keyshape.VRECT_L')
            src=replace_build(src,'''
            self.browser()
            for x in (16,32):
                self.add_line(f'binding-{x}',(x,4),(x,8))
                self.relate('connect',f'binding-{x}','browser-top')
            # One coherent receiver stroke: rounded bend and two cuff ends.
            self.add_polyline('earpiece',(19,22),(16,25),(18,27))
            self.add_bezier('receiver',(18,27),((21,32),(25,35),(28,35)))
            self.add_polyline('mouthpiece',(28,35),(32,31),(29,28))
            self.relate('connect','earpiece','receiver')
            self.relate('connect','receiver','mouthpiece')
            ''')
            r['omissions']=['Outlined handset reduced to one curved receiver stroke with two cuff ends.']
        elif i==7:
            src=replace_build(src,'''
            # Shallower top rim increases the circular chart's available height.
            self.path('frame',(10,8),[('L',(14,8)),('L',(24,8)),('L',(34,8)),('L',(38,8)),('A',(42,12),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,12)),('A',(10,8),4,4,True)],True)
            for x in (14,24,34):
                self.add_line(f'binding-{x}',(x,6),(x,8))
                self.relate('connect',f'binding-{x}','frame')
            # Radius 8 supports a spacious chart. The last spoke is set at the
            # lower cardinal point to keep every attachment exactly on-grid.
            self.circle('pie',24,25,8)
            for n,end in [('up',(24,17)),('right',(32,25)),('down',(24,33))]:
                self.add_line('spoke-'+n,(24,25),end)
                self.relate('connect','spoke-'+n,'pie')
            self.relate('connect','spoke-up','spoke-right','spoke-down')
            ''')
            r['omissions']=['Lower-left divider squared to a downward radius so all three sector joins use exact integer circular endpoints.']
        elif i==8:
            src=src.replace('(26,16),(20,22),(28,22),(22,26)','(26,17),(20,22),(28,22),(22,25)')
        elif i==9:
            src=src.replace('(8,20),(12,20),(14,8),(34,8),(36,20),(40,20)','(8,20),(12,8),(36,8),(40,20)')
            src=src.replace('(16,18),(20,22),radius_x=4','(17,19),(20,22),radius_x=3').replace('(20,22),(16,26),radius_x=4','(20,22),(17,25),radius_x=3')
            src=src.replace('(32,18),(28,22),radius_x=4','(31,19),(28,22),radius_x=3').replace('(28,22),(32,26),radius_x=4','(28,22),(31,25),radius_x=3')
        elif i==10:
            src=src.replace("rounded('front',6,6,28,36,3)","rounded('front',6,6,32,36,3)")
            src=src.replace("(28,14),(42,18),(34,42)","(32,14),(42,18),(34,42)")
            src=src.replace('(17,14),(11,22)','(19,15),(15,22)').replace('(11,22),(17,24),radius_x=4','(15,22),(19,23),radius_x=3').replace('(17,24),(23,22),radius_x=4','(19,23),(23,22),radius_x=3').replace('(23,22),(17,14)','(23,22),(19,15)').replace('(17,24),(17,29)','(19,23),(19,27)')
            src=src.replace('(28,22),(35,27),(31,34),(28,32)','(32,22),(37,27),(33,34),(32,32)')
            src+="        self.relate('connect','diamond','front')\n"
        elif i==11:
            src=src.replace("('main',24,24,7,9),('upper',16,12,3,4),('lower',32,36,3,4)","('main',24,24,6,8),('upper',16,12,4,5),('lower',32,36,4,5)")
        elif i==12:
            src=src.replace("rounded('die',26,26,42,42,3)","rounded('die',18,24,42,42,3)")
            src=src.replace('(26,34),(12,42),(6,16),(20,10),(26,26)','(18,34),(12,42),(6,16),(20,10),(24,24)')
            src=src.replace('(20,10),(24,6),(42,10),(38,26)','(20,10),(24,6),(42,10),(38,24)')
            a=src.index('        for row in range(2):')
            src=src[:a]+"        for j,x in enumerate((26,34)): self.add_dot(f'pip-{j}',(x,33))\n"
            r['omissions']=['Removed the two extra lower pips invented by the parent; the supplied reference has two visible pips.']
        elif i==13:
            src=src.replace("heart('main',24,23,4,10)","heart('main',24,24,3,7)").replace("heart('upper',16,12,2,4)","heart('upper',17,13,2,4)").replace("heart('lower',32,36,2,4,True)","heart('lower',31,35,2,4,True)")
        elif i==14:
            a=src.index("        self.add_arc('arm-left'");src=src[:a]+'''
        self.add_bezier('arm-left',(15,25),((16,28),(18,29),(20,29)))
        self.add_polyline('shoulder',(20,29),(24,29),(28,29))
        self.add_bezier('arm-right',(28,29),((30,29),(32,28),(33,25)))
        self.add_line('torso',(24,29),(24,33))
        self.relate('connect','arm-left','shoulder')
        self.relate('connect','shoulder','arm-right','torso')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
        # Actual head bottom 21; torso junction 29: 29-21-4=4 ink gap.
'''
        elif i==15:
            src=src.replace('(16,12),(8,12)','(14,12),(8,12)')
            src=src.replace('(30,12),(36,12)','(34,12),(36,12)')
            src=src.replace("self.add_polyline('flash',(26,8),(14,26),(22,26),(20,40),(32,22),(24,22),closed=True)","self.add_polyline('flash',(26,8),(20,24),(28,24),(22,40))")
            r['omissions']=['Closed lightning outline reduced to the open centerline bolt used by the inspected Lucide battery-charging construction.']
        elif i==16:
            src=src.replace("self.add_polyline('flash',(26,8),(16,26),(24,26),(22,40),(32,22),(24,22),closed=True)","self.add_polyline('flash',(26,8),(22,24),(26,24),(22,40))")
            src=src.replace("[('outer',10,6,14),('inner',16,4,7)]","[('outer',8,4,14),('inner',14,1,6)]")
            r['omissions']=['Closed bolt reduced to a narrow centerline zigzag; inner wave bows made shallower while retaining both pairs.']
        elif i==17:
            a=src.index("        self.add_polyline('rear'")
            src=src[:a]+'''
        self.add_polyline('rear',(30,14),(30,6),(6,6),(6,22),(10,22),(6,30),(14,24))
        self.add_polyline('front',(14,14),(42,14),(42,38),(36,38),(36,42),(32,38),(14,38),closed=True)
        self.relate('connect','front','rear')
        self.add_arc('heart-left',(24,25),(28,25),radius_x=2)
        self.add_arc('heart-right',(28,25),(32,25),radius_x=2)
        self.add_polyline('heart-point',(32,25),(28,29),(24,25))
        self.add_contour('heart','heart-left','heart-right','heart-point-1','heart-point-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='heart-point']
'''
        elif i==18:
            src=src.replace("'check',(16,26)","'check',(12,26)")
            src=src.replace("'finger-left',(24,32),(24,24)","'finger-left',(24,34),(24,28)")
            src=src.replace("'tip',(24,24),(32,24)","'tip',(24,28),(32,28)")
            src=src.replace("'finger-right',(32,24),(32,32),(36,32),(36,36)","'finger-right',(32,28),(32,34),(36,34),(36,36)")
            src=src.replace("'palm-left',(16,36),(16,32),(24,24)","'palm-left',(16,36),(16,34),(24,28)")
            r['omissions']=['Amount box and small writing rows remain reduced to two line marks, preserving the check-and-pointing-hand composition.']
        elif i==19:
            a=src.index("        self.add_polyline('diagonal-wafer'")
            src=src[:a]+'''
        self.add_polyline('diagonal-wafer',(6,22),(22,6),(28,12),(12,28),closed=True)
        self.add_line('wafer-top',(22,6),(34,6))
        self.add_arc('wafer-upper',(34,6),(38,10),radius_x=4)
        self.add_arc('wafer-lower',(38,10),(34,14),radius_x=4)
        self.add_line('wafer-bottom',(34,14),(26,14))
        self.add_contour('upper-wafer','wafer-top','wafer-upper','wafer-lower','wafer-bottom')
        self.relate('connect','upper-wafer','diagonal-wafer')
        self.add_polyline('lower-wafer',(18,22),(34,22),(34,14))
        self.relate('connect','lower-wafer','upper-wafer','diagonal-wafer')
        self.add_bezier('right-curve',(38,10),((40,10),(42,14),(42,18)),((42,21),(42,23),(42,26)))
        self.relate('connect','right-curve','wafer-upper','wafer-lower')
        self.add_arc('rim-top',(16,35),(40,35),radius_x=12,radius_y=4)
        self.add_arc('rim-bottom',(40,35),(16,35),radius_x=12,radius_y=4)
        self.add_contour('rim','rim-top','rim-bottom',closed=True)
        self.add_arc('bowl',(40,35),(16,35),radius_x=12,radius_y=7)
        self.relate('connect','rim','bowl')
'''
        module=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
        (o/module).write_text(src);r['module']=module
    (HERE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2)+'\n')

def export(indices=None):
    rows=json.loads((HERE/'batch-inputs.json').read_text())
    for i,r in enumerate(rows):
        if indices is not None and i not in indices:continue
        o=Path(r['result_dir'])
        if (o/'result.json').exists():continue
        try:
            sp=importlib.util.spec_from_file_location('r2_'+str(i),o/r['module']);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
            icon=m.Drawing();report=icon.validate_icon();r['validation_status']=report.status;r['keyshape']=icon.keyshape.name
            (o/'validation.txt').write_text(report.describe());svg=icon.to_svg();(o/(r['icon_id']+'.svg')).write_text(svg)
            for t,bg,neg in [('light','white',False),('dark','#181818',True)]:
                for sz in (48,192):cairosvg.svg2png(bytestring=svg.encode(),output_width=sz,output_height=sz,background_color=bg,negate_colors=neg,write_to=str(o/f'{t}-{sz}.png'))
            r.pop('error',None);print(i+1,r['concept'],report.status,flush=True)
        except Exception as e:
            r['validation_status']='error';r['error']=repr(e);(o/'validation.txt').write_text(repr(e));print(i+1,repr(e),flush=True)
    (HERE/'batch-inputs.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':
    import sys
    if 'export' not in sys.argv:author()
    indices={int(n)-1 for n in sys.argv[2:]} if len(sys.argv)>2 else None
    export(indices)
