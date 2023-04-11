<script lang="ts">
  import "./fonts.css";
  import "./styles.css";

  import Navbar from "$lib/blockons/Navbar.svelte";
  import ScrollUp from "$lib/blockons/ScrollUp.svelte";

  import { scroll_status } from "$lib/blockons/scroll_status";
</script>
<svelte:window on:scroll={() => scroll_status.compute()} />

<Navbar />

<main id="main">
  <slot />
</main>

<ScrollUp />

<style>
  main {
    margin-top: 5em;
  }

  main :global(*) {
    scroll-margin-top: 6em;
  }
</style>
