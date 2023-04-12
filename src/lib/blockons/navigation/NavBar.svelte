<script lang="ts">
  export let regions: Array<[string, string]>;

  let scrollY: number;

  let shrunk = false;
  let lastChange = 0;
  const offset = 60; // px

  function handleScroll() {
    // shrink or grow the navbar wether scrolled up or down or at the top of the page

    if (scrollY <= offset) {
      // at top
      shrunk = false;
    } else if (lastChange - scrollY - offset > 0) {
      // scrolled up
      shrunk = false;
      lastChange = scrollY;
    } else if (scrollY - lastChange - offset > 0) {
      // scrolled down
      shrunk = true;
      lastChange = scrollY;
    }
  }
</script>
<svelte:window
  on:scroll={handleScroll}
  bind:scrollY={scrollY}
/>

<nav class="bar" class:shrunk>
  <div class="the-title">
    <span>n°500 506</span>
  </div>
  {#each regions as region}
    <!-- <span on:click={() => jumpto(region[1])}>{region[0]}</span> -->
      <a class="nav-element" href="#{region[1]}">
        {region[0]}
        <div class="shadow-holder">
          <div class="shadow-box" />
        </div>
      </a>
  {/each}
</nav>

<style>
  nav.bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 5em;

    background: linear-gradient(45deg, #e66465, #9198e5);
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    transition: height 0.3s;
    overflow-y: hidden;

    display: flex;
    justify-content: center;
    align-items: center;
  }
  nav.bar.shrunk {
    height: 3.4em;
  }

  .the-title {
    padding: 1em;
  }
  .the-title span {
    font-size: 2.2em;
    font-style: italic;
    transition: font-size 0.3s;
  }
  .shrunk .the-title span {
    font-size: 2.2em;
  }

  .bar a {
    padding: 1em;
    position: relative;

    font-size: 1.3em;
    color: black;
    background: transparent;
    text-decoration: none;
    transition: color 0.2s;
  }
  .bar a:hover {
    color: #403838;
  }

  .bar .shadow-holder {
    position: absolute;
    top: -5%;
    left: -10%;
    width: 120%;
    height: 110%;

    display: flex;
    justify-content: center;
    align-items: center;

    pointer-events: none;
  }
  .bar .shadow-holder .shadow-box {
    width: 100%;
    height: 90%;

    background: radial-gradient(rgba(0,0,0,0.2), transparent 70%);
    opacity: 0;
    transition: opacity 0.3s;

    pointer-events: none;
  }
  .bar .nav-element:hover .shadow-holder .shadow-box {
    opacity: 0.5;
  }

  @media screen and (min-width: 770px) {
    .the-title {
      margin-right: min(calc(100% - 770px), 1em);
    }
    .the-title span {
      font-size: 2.5em;
    }
  }

  @media screen and (max-width: 1220px) {
    nav.bar {
      height: 3.4em;
    }
  }
</style>
