<script>
  // Clicking a main or sub opens it large on its own grid with its stroke centerline, and its facts.
  import '../styles/part.css';
  import {inspect} from '../lib/inspect.svelte.js';
  import {dataURL} from '../lib/rules.js';
  let dialog = $state();
  $effect(() => { inspect.shown;if (inspect.open && dialog && !dialog.open) dialog.showModal(); else if (!inspect.open && dialog?.open) dialog.close(); });
  function place(element, svg) { element.replaceChildren();if (svg) element.append(svg);return {update: next => { element.replaceChildren();if (next) element.append(next); }}; }
  // A click on the backdrop (outside the dialog's box) closes it.
  function backdrop(e) {
    if (e.target !== dialog) return;
    const r = dialog.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) inspect.open = false;
  }
</script>

<dialog class="side-inspect side-component-inspect" data-view={inspect.view} bind:this={dialog} onclose={() => { inspect.open = false; }} onclick={backdrop}>
  <header><h2>{inspect.label} · {inspect.item?.icon || ''}</h2><button type="button" class="side-inspect-close" onclick={() => { inspect.open = false; }}>Close</button></header>
  <div class="side-component-controls" role="group" aria-label="Display">
    {#each [['both', 'Artwork + centerline'], ['art', 'Artwork'], ['line', 'Centerline only']] as [view, label] (view)}
      <button type="button" data-view={view} aria-pressed={String(inspect.view === view)} onclick={() => { inspect.view = view; }}>{label}</button>
    {/each}
    {#if inspect.item}<a target="_blank" rel="noopener" href={inspect.item.document ? dataURL(inspect.item.document) : inspect.item.preview_url}>Open SVG</a>{/if}
  </div>
  <div class="side-stage">
    {#if inspect.error}<p class="muted">{inspect.error}</p>
    {:else if !inspect.svg}<p class="muted">Loading artwork…</p>
    {:else}<div use:place={inspect.svg}></div>{/if}
  </div>
  <dl class="side-component-facts">
    {#each inspect.facts as [k, v] (k)}<dt>{k}</dt><dd>{v}</dd>{/each}
  </dl>
</dialog>
