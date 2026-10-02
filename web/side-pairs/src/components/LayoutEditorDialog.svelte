<script>
  // The layout editor: presets, the editing canvas (main and sub drawn whole, centerline in red), the combined result
  // and its outputs at 32 / 48 / 64 px, the element list, and Apply to pairs using this main. Its state and actions
  // are lib/editor.svelte.js.
  import '../styles/editor.css';
  import {STROKE, SIDES, fmt, scales, boxOf, unionOf, keyOf} from '../lib/editor.svelte.js';
  let {editor} = $props();
  let dialog = $state(), canvas = $state(), width = $state(0);
  $effect(() => { editor.shown;if (editor.open && dialog && !dialog.open) dialog.showModal(); else if (!editor.open && dialog?.open) dialog.close(); });

  // The editor changes its state in place; the view gets a fresh copy of it (and of every unit) on each change, so
  // everything drawn from it redraws.
  const ctx = $derived((editor.version, editor.ctx && {...editor.ctx}));
  const loaded = $derived(!!ctx?.loaded);
  const c = $derived(ctx?.canvas || 64);
  // Strokes do not stretch with a unit: drawn in screen pixels, 4 canvas units wide.
  const px = $derived(width > 0 ? width / (c + 2) : 6);
  const roles = $derived((editor.version, loaded ? Object.entries(ctx.roles).map(([role, r]) => [role, {...r, units: r.units.map(u => ({...u}))}]) : []));
  const list = $derived((editor.version, loaded ? editor.selected().map(u => ({...u})) : []));
  const box = $derived(list.length ? unionOf(list) : null);
  const bad = $derived((editor.version, loaded && editor.anyOutside()));
  const pairs = $derived((editor.version, loaded ? editor.pairsWithMain(ctx.main.icon, ctx.pair.id) : []));
  const layoutNow = $derived((editor.version, loaded ? editor.layout() : null));

  // A unit's elements drawn whole (artwork, or its centerline trace).
  function unitArt(group, {markup, paths, px, trace}) {
    const draw = ({markup, paths, px, trace}) => {
      group.replaceChildren();
      const parsed = new DOMParser().parseFromString(`<svg xmlns="http://www.w3.org/2000/svg">${paths.map(p => markup[p]).join('')}</svg>`, 'image/svg+xml').documentElement;
      [...parsed.children].forEach((child, n) => {
        const e = document.importNode(child, true);e.setAttribute('data-path', paths[n]);e.setAttribute('vector-effect', 'non-scaling-stroke');
        if (trace) { e.setAttribute('stroke', '#ef4444');e.setAttribute('stroke-width', 1.3);e.setAttribute('fill', 'none'); }
        else e.setAttribute('stroke-width', STROKE * px);
        group.append(e);
      });
    };
    draw({markup, paths, px, trace});
    return {update: draw};
  }
  // The combined result, with its centerline traced on top when that view is on.
  function result(element, {svg, centerline}) {
    const draw = ({svg, centerline}) => {
      element.replaceChildren();if (!svg) return;
      const root = new DOMParser().parseFromString(svg, 'image/svg+xml').documentElement;
      root.setAttribute('class', 'side-layout-result');root.removeAttribute('width');root.removeAttribute('height');root.setAttribute('role', 'img');root.setAttribute('aria-label', 'Combined result');
      if (centerline) for (const id of ['main-icon-clipped', 'state-icon']) {
        const g = root.querySelector(`[id="${id}"]`);if (!g) continue;
        const t = g.cloneNode(true);t.setAttribute('opacity', '1');
        for (const n of [t, ...t.querySelectorAll('*')]) { n.removeAttribute('id');n.setAttribute('stroke', '#ef4444');n.setAttribute('fill', 'none');n.setAttribute('stroke-width', '1.2');n.setAttribute('vector-effect', 'non-scaling-stroke'); }
        g.setAttribute('opacity', '.35');root.append(t);
      }
      element.append(document.importNode(root, true));
    };
    draw({svg, centerline});
    return {update: draw};
  }
  // The output SVG as it ships: black strokes only.
  const output = $derived(ctx?.result?.svg ? 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(ctx.result.svg.replace(/currentColor/g, '#000000')) : '');

  // Pointer: pick, move the selection, or resize it from a corner or an edge with the opposite side pinned.
  const point = e => { const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(canvas.getScreenCTM().inverse());return [p.x, p.y]; };
  function down(e) {
    const additive = e.shiftKey || e.metaKey || e.ctrlKey, target = e.target;
    const unitOf = el => { const art = el?.closest?.('.art');return art ? {role: art.dataset.role, unit: Number(art.dataset.unit), path: el.closest('[data-path]') ? Number(el.closest('[data-path]').dataset.path) : null} : null; };
    const hit = {handle: target.dataset?.handle || null, move: target.hasAttribute?.('data-move'), ...(unitOf(target) || {role: null})};
    if (hit.move) {
      // Artwork under the selection frame (the arrow inside a selected monitor) can still be picked.
      const nodes = document.elementsFromPoint(e.clientX, e.clientY);
      const art = nodes.map(n => n.closest?.('.art')).find(Boolean), path = nodes.map(n => n.closest?.('[data-path]')).find(n => n?.closest('.art'));
      if (art) hit.under = {role: art.dataset.role, unit: Number(art.dataset.unit), path: path ? Number(path.dataset.path) : null};
    }
    const d = editor.press(hit, additive);
    if (!d) return;
    canvas.focus();canvas.setPointerCapture?.(e.pointerId);e.preventDefault();
    const start = point(e);
    const move = ev => editor.drag(d, start, point(ev), ev.shiftKey);
    const up = () => { canvas.removeEventListener('pointermove', move);canvas.removeEventListener('pointerup', up);canvas.removeEventListener('pointercancel', up);editor.release(d); };
    canvas.addEventListener('pointermove', move);canvas.addEventListener('pointerup', up);canvas.addEventListener('pointercancel', up);
  }
  function key(e) { if (editor.key(e)) { e.preventDefault();e.stopPropagation(); } }

  // Presets: the sizes and keyshape tiles of a role at its chosen size.
  const presetRows = $derived.by(() => {
    editor.version;if (!loaded) return [];
    return ['main', 'sub'].filter(role => editor.hasPresets(role)).map(role => {
      const r = ctx.roles[role], own = editor.ownShape(role), {state, now} = editor.presetState(role), {base, sizes, label} = editor.presets[role];
      const current = unionOf(r.units);
      const shapes = [...(own ? [] : [{id: 'own', label: 'Own shape'}]), ...editor.shapes(role)].map(s => ({s, b: editor.presetBox(role, state.size, s.id)})).filter(x => x.b);
      return {role, own, state, now, base, label, painted: `${current[2] - current[0] + 4}×${current[3] - current[1] + 4}`,
              sizes: sizes.filter(size => editor.presetBox(role, size, state.shape)), shapes};
    });
  });
  const shapeIcon = (w, h, circle) => { const k = 18 / Math.max(w, h);return {sw: w * k, sh: h * k, circle}; };
  // Dashed outline of each role's chosen keyshape at its chosen size (painted), behind the artwork.
  const guides = $derived.by(() => {
    editor.version;if (!loaded) return [];
    return ['main', 'sub'].flatMap(role => {
      const state = ctx.preset?.[role];if (!editor.hasPresets(role) || !state?.size) return [];
      const b = editor.presetBox(role, state.size, state.shape);if (!b) return [];
      const shape = editor.shapes(role).find(s => s.id === state.shape);
      return [{role, circle: !!shape?.circle, p: [b[0] - 2, b[1] - 2, b[2] + 2, b[3] + 2]}];
    });
  });
  const handles = $derived(box ? (() => { const p = [box[0] - 2, box[1] - 2, box[2] + 2, box[3] + 2], mx = (p[0] + p[2]) / 2, my = (p[1] + p[3]) / 2;
    return {p, list: [['nw', p[0], p[1]], ['n', mx, p[1]], ['ne', p[2], p[1]], ['e', p[2], my], ['se', p[2], p[3]], ['s', mx, p[3]], ['sw', p[0], p[3]], ['w', p[0], my]]}; })() : null);
  const named = (r, u) => u.paths.some(p => !['path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon'].includes(r.names[p]));
  const nTargets = $derived((editor.version, ctx?.targets?.size || 0));
</script>

<dialog class="side-layout" bind:this={dialog} onclose={() => editor.close()}>
  <header><h2>Adjust layout · {ctx?.pair.concept || ''}</h2><button type="button" onclick={() => editor.close()}>Close</button></header>
  <div class="side-layout-bar side-layout-presets" role="group" aria-label="Main and sub size">
    {#each presetRows as row (row.role)}
      <div class={'side-layout-sizes ' + row.role}><span>{row.label} size</span>
        {#each row.sizes as size (size)}
          <button type="button" aria-pressed={String(!!row.now && row.now.size === size)} title={size === row.base ? 'Automatic size' : null}
                  onclick={() => { editor.applyPreset(row.role, size, row.state.shape);canvas?.focus(); }}>{size}</button>
        {/each}
        <button type="button" aria-pressed={String(!row.now)} title={`Resize the ${row.role} freely: drag its handles`} onclick={() => { editor.free(row.role);canvas?.focus(); }}>Free</button>
        <small>painted {row.painted}</small>
      </div>
      <div class={'side-layout-shapes ' + row.role}><span>{row.label} keyshape at {row.state.size}</span>
        {#each row.shapes as {s, b} (s.id)}
          {@const w = b[2] - b[0] + 4}{@const h = b[3] - b[1] + 4}{@const icon = shapeIcon(w, h, s.circle)}
          <button type="button" class="side-layout-shape" aria-pressed={String(!!row.now && row.now.shape === s.id)}
                  title={`${s.label}${s.names ? ' (' + s.names.join(', ') + ')' : ''}: painted ${w}×${h} at size ${row.state.size}`}
                  onclick={() => { editor.applyPreset(row.role, row.state.size, s.id);canvas?.focus(); }}>
            <svg viewBox="0 0 22 22" width="22" height="22" aria-hidden="true">
              {#if icon.circle}<circle cx="11" cy="11" r={icon.sw / 2} fill="none" stroke="currentColor" stroke-width="1.6" />
              {:else}<rect x={11 - icon.sw / 2} y={11 - icon.sh / 2} width={icon.sw} height={icon.sh} rx="2" fill="none" stroke="currentColor" stroke-width="1.6" />{/if}
            </svg>
            <span>{s.label}</span><small>{w}×{h}{s.id === row.own ? ' · own' : ''}</small>
          </button>
        {/each}
      </div>
    {/each}
  </div>
  <div class="side-layout-bar"><span>Click selects</span>
    {#each [['whole', 'Whole icon', null], ['element', 'Element', null], ['path', 'Path', 'One path of a connected element (the stand of a monitor)']] as [level, label, title] (level)}
      <button type="button" aria-pressed={String(ctx?.level === level)} {title} disabled={!loaded} onclick={() => editor.setLevel(level)}>{label}</button>
    {/each}
    <label><input type="checkbox" checked={editor.centerline} onchange={e => editor.setCenterline(e.currentTarget.checked)}> Centerline</label><span class="spacer"></span>
    <button type="button" disabled={!loaded || ctx.busy || !ctx.saved} onclick={() => editor.reset()}>Reset to automatic</button>
    <button type="button" disabled={!ctx} onclick={() => editor.discard()}>Discard changes</button>
    <button type="button" class:side-layout-stale-button={ctx?.stale && !ctx?.combining} title="Combine the main and sub with this layout to see the result"
            disabled={!loaded || ctx.busy || ctx.combining || bad} onclick={() => editor.applyLayout()}>{ctx?.combining ? 'Combining…' : 'Apply layout'}</button>
    <button type="button" class="side-layout-save" disabled={!loaded || ctx.busy || bad || !ctx.dirty.size} onclick={() => editor.save()}>Save layout</button>
  </div>
  <div class="side-layout-stages">
    <figure bind:clientWidth={width}>
      <svg class="side-layout-canvas" tabindex="0" role="application" aria-label={`Layout editor, ${c} by ${c} grid`} viewBox={`-1 -1 ${c + 2} ${c + 2}`}
           data-centerline={editor.centerline ? '' : null} bind:this={canvas} onpointerdown={loaded ? down : null} onkeydown={key}>
        {#if loaded}
          <g pointer-events="none">
            {#each Array.from({length: c + 1}, (_v, i) => i) as i (i)}
              <line x1={i} y1="0" x2={i} y2={c} stroke={i % 8 === 0 ? '#9eb3bd' : '#dae4e9'} stroke-width={i % 8 === 0 ? .13 : .055} />
              <line x1="0" y1={i} x2={c} y2={i} stroke={i % 8 === 0 ? '#9eb3bd' : '#dae4e9'} stroke-width={i % 8 === 0 ? .13 : .055} />
            {/each}
          </g>
          {#each guides as g (g.role)}
            {#if g.circle}<circle class={'guide ' + g.role} fill="none" cx={(g.p[0] + g.p[2]) / 2} cy={(g.p[1] + g.p[3]) / 2} r={(g.p[2] - g.p[0]) / 2} />
            {:else}<rect class={'guide ' + g.role} fill="none" x={g.p[0]} y={g.p[1]} width={g.p[2] - g.p[0]} height={g.p[3] - g.p[1]} rx="1" />{/if}
          {/each}
          {#each roles as [role, r] (role)}
            <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              {#each r.units as u, i (role + i + ':' + u.paths.join(','))}
                {@const [sx, sy] = scales(u)}
                <g class={'art' + (ctx.sel.has(keyOf(role, i)) ? ' picked' : '')} data-role={role} data-unit={i}
                   transform={`matrix(${sx} 0 0 ${sy} ${u.x - u.src[0] * sx} ${u.y - u.src[1] * sy})`} use:unitArt={{markup: r.markup, paths: u.paths, px, trace: false}}></g>
              {/each}
            </g>
          {/each}
          {#if editor.centerline}
            <g class="trace" fill="none" stroke="#ef4444">
              {#each roles as [role, r] (role)}
                {#each r.units as u, i (role + i + ':' + u.paths.join(','))}
                  {@const [sx, sy] = scales(u)}
                  <g transform={`matrix(${sx} 0 0 ${sy} ${u.x - u.src[0] * sx} ${u.y - u.src[1] * sy})`} use:unitArt={{markup: r.markup, paths: u.paths, px, trace: true}}></g>
                {/each}
              {/each}
            </g>
          {/if}
          {#if handles}
            {#each list as u, n (n)}
              {@const b = boxOf(u)}
              {#if list.length > 1 || editor.outside(b)}<rect class={'unit' + (editor.outside(b) ? ' out' : '')} x={b[0] - 2} y={b[1] - 2} width={b[2] - b[0] + 4} height={b[3] - b[1] + 4} />{/if}
            {/each}
            <rect class="move" x={handles.p[0]} y={handles.p[1]} width={handles.p[2] - handles.p[0]} height={handles.p[3] - handles.p[1]} data-move="" />
            <rect class={'sel' + (editor.outside(box) ? ' out' : '')} x={handles.p[0]} y={handles.p[1]} width={handles.p[2] - handles.p[0]} height={handles.p[3] - handles.p[1]} />
            <!-- Live size on the frame: painted ink (stroke included) and the centerline bounding box. -->
            <text class="size-label" x={handles.p[0]} y={handles.p[1] > 4 ? handles.p[1] - 1.2 : handles.p[3] + 3.2}>ink {fmt(handles.p[2] - handles.p[0])}×{fmt(handles.p[3] - handles.p[1])} · box {fmt(box[2] - box[0])}×{fmt(box[3] - box[1])} · at {fmt(handles.p[0])},{fmt(handles.p[1])}</text>
            {#each handles.list as [name, x, y] (name)}
              <rect class={'handle ' + name} data-handle={name} x={x - .8} y={y - .8} width="1.6" height="1.6" />
            {/each}
          {/if}
        {/if}
      </svg>
      <figcaption>Editing view: main and sub drawn whole, centerline in red.</figcaption>
    </figure>
    <div class="side-layout-result-column"><figure>
      <div class="side-layout-preview">
        {#if ctx?.stale}<p class="side-layout-stale">{bad ? 'Move the artwork back inside the canvas, then Apply layout.' : 'Layout changed. Click Apply layout to see the combined result.'}</p>{/if}
        {#if ctx?.result}<div use:result={{svg: ctx.result.svg, centerline: editor.centerline}}></div>{:else}<span>{ctx ? 'Loading…' : ''}</span>{/if}
      </div>
      <figcaption>Combined result (the sub erases the main where they meet).</figcaption></figure>
      <div class="side-layout-output" aria-label="Output SVG at 32, 48 and 64 pixels">
        {#if output}{#each [32, 48, 64] as size (size)}<figure><img src={output} width={size} height={size} alt={`Output at ${size} pixels`}><figcaption>{size} px</figcaption></figure>{/each}{/if}
      </div>
    </div>
    <div class="side-layout-list" aria-label="Elements">
      {#each roles as [role, r] (role)}
        <section><h3>{role === 'main' ? 'Main elements' : 'Sub elements'}</h3>
          {#each r.units as u, i (role + i + ':' + u.paths.join(','))}
            {@const isNamed = named(r, u)}
            <label><input type="checkbox" checked={ctx.sel.has(keyOf(role, i))} onchange={e => editor.toggleUnit(role, i, e.currentTarget.checked)}>
              <span>{isNamed ? u.paths.map(p => r.names[p]).join(' + ') : `${role === 'sub' && ctx.pair.native_text ? 'Glyph' : 'Element'} ${i + 1}`}<small>{' · '}{fmt(u.w + 4)}×{fmt(u.h + 4)}</small></span></label>
            <!-- Child paths of a connected element: ticking one splits the element and selects that path. -->
            {#if u.paths.length > 1}
              {#each u.paths as p (p)}
                <label class="child"><input type="checkbox" onchange={() => editor.pickPath(role, i, p)}><span>{isNamed ? r.names[p] : `path ${p + 1}`}</span></label>
              {/each}
            {/if}
          {/each}
          <div class="row-actions"><button type="button" onclick={() => editor.selectRole(role)}>Select all</button></div>
        </section>
      {/each}
      {#if loaded}
        <div class="row-actions">
          <button type="button" title="Resize the paths of a connected element one by one" disabled={!list.some(u => u.paths.length > 1)} onclick={() => editor.split()}>Split into paths</button>
          <button type="button" disabled={!ctx.sel.size} onclick={() => editor.clearSelection()}>Clear selection</button>
        </div>
      {/if}
    </div>
  </div>
  {#if loaded && pairs.length}
    <!-- Other side pairs using this main: choose which ones get this layout too. -->
    <details class="side-layout-apply" open={ctx.applyOpen !== false} ontoggle={e => { editor.ctx.applyOpen = e.currentTarget.open; }}>
      <summary>Also apply to pairs using this main ({pairs.length})</summary>
      <p>Main and sub carry over. Other sides are re-anchored: main and sub keep their size and edits, each in its own corner. A different sub keeps its own shape, fitted to the edited sub's box.</p>
      {#each [[`Same side · ${SIDES[ctx.pair.position] || ctx.pair.position}`, pairs.filter(p => p.position === ctx.pair.position)], ['Other sides', pairs.filter(p => p.position !== ctx.pair.position)]] as [title, group] (title)}
        {#if group.length}
          <h4>{title} ({group.length})</h4>
          <div class="targets">
            {#each group as p (p.id)}
              {@const result = ctx.applyResults?.[p.id]}
              <label class="target"><input type="checkbox" checked={ctx.targets.has(p.id)} onchange={e => { if (e.currentTarget.checked) ctx.targets.add(p.id); else ctx.targets.delete(p.id);editor.touchView(); }}>
                {#if p.preview}<img src={p.preview} alt="" loading="lazy">{:else}<span class="none"></span>{/if}
                <span>{p.concept}<small>{SIDES[p.position] || p.position} · {p.sub}</small>
                  {#if p.sub !== ctx.sub.icon}<span class="badge">different sub</span>{/if}{#if p.adjusted}<span class="badge warn" title="This pair has its own saved layout; applying replaces it.">adjusted</span>{/if}
                  {#if result}<small class={result.ok ? 'ok' : 'fail'}>{result.ok ? '✓ applied' : '✕ ' + result.error}</small>{/if}
                </span>
              </label>
            {/each}
          </div>
        {/if}
      {/each}
      <div class="actions">
        <button type="button" onclick={() => { pairs.forEach(p => ctx.targets.add(p.id));editor.touchView(); }}>Select all</button>
        <button type="button" onclick={() => { ctx.targets.clear();editor.touchView(); }}>Select none</button>
        <button type="button" class="side-layout-save apply-go" disabled={ctx.busy || !nTargets || !layoutNow || bad} onclick={() => editor.applyToTargets()}>Save + apply to {nTargets} pair{nTargets === 1 ? '' : 's'}</button>
        <small class="apply-note">{layoutNow ? '' : 'Adjust this pair first; its layout is what gets applied.'}</small>
      </div>
    </details>
  {/if}
  <p class="side-layout-readout" class:bad={editor.readout.bad} role="status">{editor.readout.text}</p>
  <p class="side-layout-hint">The main and sub sizes (every 4) and a keyshape snap the main / sub onto that keyshape at that size (purple / teal dashes) — the middle size on the own keyshape is automatic; Free lets you drag it to any size. Click selects a whole icon, a connected element, or one path of it (Path splits that element for you). Shift- or ⌘-click (or tick the list) to choose several. Drag to move; drag a corner or edge to resize — width and height change independently, hold Shift to keep proportions. Arrow keys move 1 unit (Shift: 8); Alt+arrows change width / height by 1; + and − change both. Everything snaps to the grid; the stroke stays 4. Edits do not combine by themselves: click Apply layout to see the combined result, then Save layout to keep it.</p>
  <p class="side-layout-error" role="alert">{editor.error}</p>
</dialog>
