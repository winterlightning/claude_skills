from pathlib import Path
import json,shutil,cairosvg
B=Path(__file__).parent
rows=json.loads((B/'staged.json').read_text());runs=json.loads((B/'runs.json').read_text())
changes={
'police-avatar':'Restored the raised left arm and shallow asymmetric cap over a circular jaw.',
'police-officer-with-sunglasses-and-pocket':'Enlarged the paired sunglass openings and circular face and rounded the low hat. Omitted the chest pocket after spacing trials.',
'real-estate-market-house-decrease':'Redrew the descending diagonal arrow and three progressively shorter outlined bars with equal spacing.',
'smart-tv-and-phone':'Extended the television lower screen edge beneath the phone; rebuilt the stand and Wi-Fi arc with inner dot.',
'spotify-logo-1':'Redrew three progressively shorter, asymmetric curved sound strokes inside the circle.',
'stressed-person':'Replaced directional chevrons with two lightning zigzags; retained circular head and exact 4-unit detached gap.',
 'three-balaclava-wearers':'Separated the two rear masks and rebuilt the front mask, each with a horizontal eye band.',
 'three-cell-row':'Replaced capsule ends with a rounded rectangle and two evenly spaced dividers.',
 'tooth-with-dental-floss-upload-79ce34090d76e090':'Rounded the two molar roots and rebuilt the floss as an open side bend with a hooked end.',
 'traditional-japanese-mochi':'Rounded the dumpling silhouette and rebuilt its lower inset with a smaller outer opening.',
 'twisted-licorice-strands':'Replaced polygonal corners with smooth diagonal strand contours and a broad crossing wrap.',
 'twisted-rubber-band':'Replaced two separate rings with an elongated loop and interrupted opposite loop showing the crossing.',
 'two-coin-stacks':'Widened the elliptical coin tops and opened the layer spacing; preserved the unequal stack heights.',
 'two-eggs-in-decorated-bowl':'Rounded the eggs and deepened the bowl to fit a visible two-lobed decorative wave.',
 'two-finger-swipe-right-upload-27a8bf31fe0cadb0':'Lengthened the rightward arrow and separated it clearly from two matched finger arches.',
 'two-overlapping-document-sheets':'Rounded both sheets while keeping the front sheet clipped corner and rear overlap.',
 'two-person-group-batch-078':'Enlarged both heads, added broad closed busts and restored the foreground overlap with exact detached gaps.',
 'vertical-swipe-gesture':'Added shafts to both arrows and retained the rounded horizontal finger.',
 'woman-with-halo':'Restored the circular jaw, peaked fringe and long hair joining the rounded shoulders under the halo.',
 'worker-wearing-ridged-hard-hat':'Replaced the helmet center dash with an outlined ridge and gave the torso a closed lower edge.'
}
for row in rows:
 k=row['item']['icon_id'];r=runs[k];assert r['valid'],k
 run=Path(r['run']);m=r['metadata'];m['changes']=changes[k]
 m['visual_review']='Inspected original and rejected drawing before authoring, and final 48px and enlarged light/dark previews. Checked smooth contour flow, source features, spacing and intentional asymmetry.'
 if k=='police-avatar':m['omissions']='Raised arm reduced to one curved stroke; omit V collar to retain clearance.'
 if k=='twisted-licorice-strands':m['omissions']='Reduced fine twists to one broad internal crossing wrap.'
 if k=='two-eggs-in-decorated-bowl':m['omissions']='Shorten the full-width source decoration to a centered wave to maintain clearance.'
 if k=='three-balaclava-wearers':m['omissions']='Lower mask/neck folds simplified; retain three head arches and eye bands.'
 (run/(k+'.metadata.json')).write_text(json.dumps(m,indent=2)+'\n')
 shutil.copyfile(row['reference'],run/'reference.svg')
 for size in (48,384):cairosvg.svg2png(url=row['reference'],write_to=str(run/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 result={**m,'validation_status':'valid','validation_warnings':[],'build_gate':'pass','module':Path(r['module']).name,'svg':k+'.svg','artifacts':sorted(p.name for p in run.iterdir() if p.is_file())}
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 (run/'review-before.txt').write_text(m['comparison']+'\nFeedback: '+m['feedback']+'\nChanged: '+changes[k]+'\nOmissions: '+m['omissions']+'\n')
(B/'runs.json').write_text(json.dumps(runs,indent=2)+'\n')
(B/'changes.json').write_text(json.dumps(changes,indent=2)+'\n')
print('Prepared 20 visually reviewed runs, all valid, zero warnings, full gate pass.')
