<script>
  // A main or sub tile: its picture on a grid, a caption with its ink size, and a Fix badge with the reasons a drawing
  // does not count (a sub's SUB32 problems, failed checks, a disapproval). Clicking it opens the inspector.
  import '../styles/part.css';
  import {dataURL, round, ink, subProblems, drawingProblems} from '../lib/rules.js';
  import {openInspect} from '../lib/inspect.svelte.js';
  let {s, label, item, size, isSub, drawing, concept} = $props();

  const caption = $derived(!item ? `${label} · ${size}×${size}` : item.native_text ? `${label} ${round(item.canvas_width)}×${round(item.canvas_height)} · native`
    : item.document ? `${label} ${round(ink(item, isSub)[0])}×${round(ink(item, isSub)[1])} / ${size}` : `${label} · generated`);
  // A sub drawn here (with its SUB32 measures): its own problems first, as the old grid marked it.
  // Read with the store's version: reviews and repair flags are plain data that change under the same item.
  const own = $derived((s.version, isSub && item?.document ? subProblems(s, item, s.flagged) : []));
  // Then the drawing the tile shows: failed checks or its review state.
  const shown = $derived((s.version, !own.length && item ? drawingProblems(s, drawing) : []));
  const problems = $derived(own.length ? own : shown);
  const badge = $derived(own.length ? 'Fix sub' : shown.length ? 'Fix ' + label.toLowerCase() : '');
  const text = $derived(shown.length ? `${label} · ${drawing.status === 'pass' ? 'needs fix' : 'fails validation'}` : caption);

  function factsOf(width, height) {
    const rows = [['Pair', concept], ['Family', item.family || item.model_key?.split('/')[0] || 'generated'], ['Canvas', `${round(width)}×${round(height)}`]];
    if (item.bounds) { const [w, h] = ink(item, isSub);rows.push(['Ink', `${round(w)}×${round(h)} / ${size}`]); }
    if (item.sizing_kind) rows.push(['Sizing', item.sizing_kind]);
    if (item.model_validation) rows.push(['Validation', item.model_validation]);
    if (item.sub32_status) rows.push(['SUB32 status', item.sub32_status + (item.sub32_reason ? ' · ' + item.sub32_reason : '')]);
    if (isSub && item.document) rows.push(['Problems', subProblems(s, item, s.flagged).join(' · ') || 'None']);
    if (item.pending) rows.push(['Status', 'Waiting to combine']);
    if (item.python_source) rows.push(['Python model', item.python_source]);
    if (item.svg) rows.push(['SVG', item.svg]);
    return rows;
  }
  const open = () => openInspect(label, item, size, concept, factsOf);
</script>

<figure class="side-part" class:needs-fix={problems.length > 0} title={problems.join(' · ')}>
  {#if item}
    <div class={'side-part-art side-grid-' + size + ' side-inspectable'} tabindex="0" role="button" aria-label={`Inspect ${label.toLowerCase()} ${item.icon}`}
         onclick={open} onkeydown={e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault();open(); } }}>
      <img src={item.document ? dataURL(item.document) : item.preview_url} alt={label + ' ' + item.icon} loading="lazy">
      {#if badge}<span class="side-fix-badge" title={problems.join(' · ')}>{badge}</span>{/if}
    </div>
  {:else}
    <div class={'side-part-art side-grid-' + size + ' side-part-missing'}><span>{label} needed</span></div>
  {/if}
  <figcaption>{text}</figcaption>
</figure>
