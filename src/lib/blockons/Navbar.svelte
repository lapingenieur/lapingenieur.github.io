<script lang="ts">
  import { scroll_status } from "./scroll_status";

  const regions = [         // name -> id
    ["Webdev", "webdev"],
    ["8-bits", "bits"],
    ["Workflow", "workflow"],
    ["Python", "python"],
    ["Chiptune", "milky"],
  ]

  ///// no need for this junk thanks to scroll-margin-top css in styles.css
  ///// but i'll keep it there cause it took me time and maybe i'll reuse it one day
  //
  // function jumpto(id: string) {
  //   let elm = document===undefined ? null : document.getElementById(id);
  //   if (elm === null) {
  //     alert("wronng");
  //     return;
  //   }
  //
  //   const main = document.getElementById("main");
  //   if (main === null) {
  //     alert("wronng");
  //     return;
  //   }
  //
  //   const margin = parseFloat(getComputedStyle(main).fontSize);
  //   const dims = elm.getBoundingClientRect();
  //   console.log(dims.top - 6*margin + window.scrollY);
  //   window.scrollTo({
  //     left: window.scrollX,
  //     top: dims.top - 6*margin + window.scrollY,
  //     behavior: "smooth"
  //   });
  // }

  let shrunk = false;
  let lastChange = 0;
  const offset = 60; // px

  function handleScroll() {
    // shrink or grow the navbar wether scrolled up or down or at the top of the page
    const scroll = window.pageYOffset;

    if (scroll <= offset) {
      // at top
      shrunk = false;
    } else if (lastChange - scroll - offset > 0) {
      // scrolled up
      shrunk = false;
      lastChange = scroll;
    } else if (scroll - lastChange - offset > 0) {
      // scrolled down
      shrunk = true;
      lastChange = scroll;
    }
  }
</script>
<svelte:window on:scroll={handleScroll} />

<nav class:shrunk>
  {#each regions as region}
    <!-- <span on:click={() => jumpto(region[1])}>{region[0]}</span> -->
    <div class="nav-element">
      <a href="#{region[1]}">
        {region[0]}
        <div class="shadow-holder">
          <div class="shadow-box"></div>
        </div>
      </a>
    </div>
  {/each}
</nav>

<style>
  nav {
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
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1.3em;
  }
  nav.shrunk {
    height: 3em;
  }

  .nav-element {
    padding: 1em;
    font-size: 1.3em;

    position: relative;
  }
  a {
    color: black;
    background: transparent;
    text-decoration: none;
    transition: color 0.2s;
  }
  a:hover {
    color: #403838;
  }
  .shrunk a {
    height: 100%;
  }

  .shadow-holder {
    position: absolute;
    top: -5%;
    left: -10%;
    width: 120%;
    height: 110%;

    display: flex;
    justify-content: center;
    align-items: center;
  }
  .shadow-holder .shadow-box {
    width: 100%;
    height: 90%;

    background: radial-gradient(rgba(0,0,0,0.2), transparent 70%);
    opacity: 0;
    transition: opacity 0.3s;
  }
  a:hover .shadow-holder .shadow-box {
    opacity: 0.5;
  }
</style>
