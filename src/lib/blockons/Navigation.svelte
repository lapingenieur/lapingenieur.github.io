<script lang="ts">
  import NavBar from "$lib/blockons/navigation/NavBar.svelte";
  import NavRod from "$lib/blockons/navigation/NavRod.svelte";

  const regions: Array<[string, string]> = [         // name -> id
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
</script>

<div class="bar">
  <NavBar {regions} />
</div>
<div class="rod">
  <NavRod {regions} />
</div>

<style>
  @media screen and (min-width: 750px) {
    .rod {
      display: none;
    }
  }
  @media screen and (max-width: 750px) {
    .bar {
      display: none;
    }
  }
</style>
