"""Advisory repair priorities for measured pairs; does not alter icon geometry."""
from collections import Counter
from pathlib import Path
import json,html

def recommendation(host,row):
    native,small=row[7:9];prototype=row[14] if len(row)>14 else None
    if native!='fail' and not (prototype and prototype['fit']=='fail'):
        return None
    name=host['name']
    if native=='pass':
        return {'action':'keep-32','reason':'Keep the passing native sub-icon. Reject the enlarged prototype because it violates padding.','verified':True}
    if host['area_status']!='vector':
        return {'action':'review-interior','reason':'Confirm the intended interior or overlay first. A collision alone cannot determine a resize for an open or overlapping composition.','verified':False}
    if name=='gift-box-container':
        return {'action':'review-shape','reason':'Original gift container restored at user request. Preserve it unchanged; a compact sub-icon layout is still needed. Do not enlarge the container automatically.','verified':False}
    if host.get('parent',name) in ('gift-box-container','liquid-soap-dispenser-bottle','right-pointing-label-tag','simple-folded-booklet'):
        return {'action':'sub-24' if small=='pass' else 'review-shape','reason':'Preserve the recognizable container proportions. Prefer a smaller, grid-authored sub-icon.'+(' The 24-unit simulation passes.' if small=='pass' else ' The exact smaller drawing still needs a fit check.'),'verified':False}
    if name in ('open-handle-shopping-basket','arched-handle-shopping-basket'):
        return {'action':'container-first','reason':'Keep the native 32 × 32 sub-icon. Propose a taller basket body: rim at y=18 and base at y=62, with shortened handles above the rim. Retain the tapered basket silhouette; recheck side clearance after a grid-snapped redraw.','verified':False}
    if small=='pass' and name in ('double-concentric-circles','photo-camera-container-v2','sedan-profile-container-v2'):
        return {'action':'sub-24','reason':'Container inspected in the 37-container repair pass. Preserve its characteristic shape; the remaining pair needs an authored 24 × 24 sub-icon. The size simulation passes.','verified':False}
    distinctive=any(word in name for word in ('droplet','heart','triangle','diamond','star','leaf','flame','pin','ribbon','medal','flag','cloud','sack','trophy','cross-container','round-wrist','round-smartwatch','circular','globe','molecular'))
    if distinctive and small=='pass':
        return {'action':'sub-24','reason':'Preserve this distinctive container silhouette. Suggest an authored 24 × 24 sub-icon; the size simulation passes, but final grid-snapped geometry still needs validation.','verified':False}
    if distinctive:
        return {'action':'review-shape','reason':'Neither tested size has a verified fit. Preserve the distinctive silhouette; review the content position and local contour before deciding between a container repair and a 24 × 24 redraw.','verified':False}
    if any(word in name for word in ('monitor','screen','window','board','phone','card','frame','camera')):
        fix='Increase the display/content opening and move dividers or hardware away from it while preserving the outer device identity.'
    elif any(word in name for word in ('bag','basket','box','storefront','padlock','cup','bottle','dispenser','tank')):
        fix='Increase the usable body area and shorten or reposition the rim, handles, lid or other interior details.'
    else:
        fix='Inspect the nearest colliding contour; enlarge the usable interior or move nonessential internal details while preserving the subject.'
    return {'action':'container-first','reason':'Prioritize the native 32 × 32 sub-icon. '+fix+(' A 24 × 24 simulation passes as a fallback if a container repair harms the shape.' if small=='pass' else ' The 24 × 24 test also lacks a verified fit; shrinking alone is not a confirmed solution.'),'verified':False}

def apply(data,out):
    cases=[]
    for row in data['rows']:
        del row[15:]
        h=data['hosts'][row[0]];rec=recommendation(h,row);row.append(rec)
        if rec:
            row[13]=rec['reason']
            if row[14] and rec['action']=='container-first':row[14]['label']='24-unit fallback test · container repair preferred'
            cases.append({'pair_id':row[9],'concept':row[10],'container':h['name'],'sub':data['subs'][row[1]]['name'],'native_fit':row[7],'size24_fit':row[8],'native_gap':row[5],'size24_gap':row[6],**rec})
    report={'policy':'Preserve recognizable container proportions first. Keep native 32 only when practical; prefer smaller authored sub-icons over distorting the subject. All proposed container repairs require visual review.','counts':dict(Counter(c['action'] for c in cases)),'cases':cases}
    out=Path(out);(out/'repair-priorities.json').write_text(json.dumps(report,indent=2))
    esc=html.escape
    labels={'container-first':'Repair container · keep 32','sub-24':'Redraw sub at 24','review-shape':'Shape review','review-interior':'Interior / overlay review','keep-32':'Keep native 32'}
    rows=''.join('<tr><td>'+esc(c['concept'])+'<small>'+esc(c['container']+' + '+c['sub'])+'</small></td><td>'+labels[c['action']]+'</td><td>32: '+str(c['native_fit'])+'<br>24: '+str(c['size24_fit'])+'</td><td>'+esc(c['reason'])+'</td></tr>' for c in cases)
    (out/'repair-priorities.html').write_text('<!doctype html><meta charset="utf-8"><title>Container repair priorities</title><style>body{font:15px system-ui;padding:24px;color:#243046}table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:14px;border-bottom:1px solid #ddd;vertical-align:top}small{display:block;margin-top:8px;color:#68768a}input{padding:10px;width:360px}</style><h1>Padding violations · repair priorities</h1><p>'+esc(report['policy'])+'</p><p>'+esc(str(report['counts']))+'</p><p><a href="index.html">Back to vector grid</a></p><input placeholder="Search concept, container or recommendation" oninput="for(const r of document.querySelectorAll(\'tbody tr\'))r.hidden=!r.textContent.toLowerCase().includes(this.value.toLowerCase())"><table><thead><tr><th>Pair</th><th>Priority</th><th>Measured fit</th><th>Proposed fix</th></tr></thead><tbody>'+rows+'</tbody></table>')
    return report
