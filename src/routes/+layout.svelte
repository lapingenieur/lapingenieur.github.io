<script lang="ts">
  import "./fonts.css";
  import "./styles.css";

  import Navigation from "$lib/blockons/Navigation.svelte";
  import ScrollUp from "$lib/blockons/ScrollUp.svelte";

  import { scroll_status } from "$lib/blockons/scroll_status";
</script>
<svelte:window on:scroll={() => scroll_status.compute()} />

<ScrollUp />
<Navigation />

<main id="main">
  <slot />
</main>

<style>
  main {
    margin-top: 3.4em;
  }

  main :global(*) {
    scroll-margin-top: .5em;
  }

  @media screen and (min-width: 450px) {
    main :global(*) {
      scroll-margin-top: 4.4em;
    }
  }

  @media screen and (min-width: 1220px) {
    main {
      margin-top: 5em;
    }
    main :global(*) {
      scroll-margin-top: 6em;
    }
  }
</style>
