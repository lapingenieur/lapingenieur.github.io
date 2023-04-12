<script lang="ts">
  import TableContents from "$lib/blockons/TableContents.svelte";
  import WebDev from "$lib/blockons/WebDev.svelte";
  import Bits from "$lib/blockons/Bits.svelte";
  import Python from "$lib/blockons/Python.svelte";
  import Workflow from "$lib/blockons/Workflow.svelte";
  import Milky from "$lib/blockons/Milky.svelte";

  import Blockon from "$lib/blockons/Blockon.svelte";

</script>

<div class="page">
  <div class="main">
    {#if import.meta.env.DEV}
      <Blockon color="null">
        <h1>TODOS</h1>

        <ul>
          <li><input disabled type="checkbox" checked>Navbar reactivity</li>
          <li><input disabled type="checkbox" checked>Navbar as menu for small devices ?</li>
          <li><input disabled type="checkbox" checked>Make the navbar smaller when scrolling down</li>
          <li><input disabled type="checkbox" checked>Scroll up button</li>
          <li><input disabled type="checkbox" checked>Build export and upload to github.io</li>
          <li><input disabled type="checkbox">Low levels</li>
          <li><input disabled type="checkbox">Misc: icon, page title...</li>
          <li><input disabled type="checkbox">Test if correcly works from github.io</li>
          <li><input disabled type="checkbox">Ask papi mami to test if correcly works from github.io</li>
          <li><input disabled type="checkbox">If all good and got time then only then add dynamic (loaded on click) video player for bits</li>
          <li><input disabled type="checkbox">Then may possibly new page/s for 8bits, others ? <i>only if there's the time and everything ok</i></li>
        </ul>
      </Blockon>
    {/if}

    <TableContents />
    <WebDev />
    <Bits />
    <Workflow />
    <Python />
    <Milky />
  </div>
</div>

<style>
  ul {
    padding: 0;
    list-style-type: none;
  }
  li input {
    margin: 0 .2em .25em -1.4em;
  }

  .page {
    width: 100%;
    display: flex;

    flex-direction: column;
    align-items: center;
  }

  .main {
    width: 100%;
    max-width: 64rem;
    padding: 1em 0;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1em;
  }

  @media screen and (min-width: 550px) {
    .main {
      margin: 0 1em;
      width: calc(100% - 2em);

      gap: 2em;
    }
  }
</style>
