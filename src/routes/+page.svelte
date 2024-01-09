<script lang="ts">
  import TableContents from "$lib/blockons/TableContents.svelte";
  import WebDev from "$lib/blockons/WebDev.svelte";
  import Bits from "$lib/blockons/Bits.svelte";
  import Python from "$lib/blockons/Python.svelte";
  import Workflow from "$lib/blockons/Workflow.svelte";
  import Milky from "$lib/blockons/Milky.svelte";
  import LowLevel from "$lib/blockons/LowLevel.svelte";
  import Self from "$lib/blockons/Self.svelte";

  import Blockon from "$lib/blockons/Blockon.svelte"
</script>

<div class="page">
  <div class="main">
    <TableContents />
    <Self />
    <WebDev />
    <Bits />
    <LowLevel />
    <Workflow />
    <Python />
    <Milky />
  </div>

  <div class="footer">
    <p>
      Merci d'avoir lu jusqu'ici&nbsp;!
    </p>

    <p>
      Vous pouvez également regarder mon <a href="https://github.com/lapingenieur">GitHub</a>
      ou me contacter par mail&nbsp;: <a href="mailto:lapingenieur@gmail.com">lapingenieur@gmail.com</a>.
    </p>

    <p>
      Ce site est hébergé grâce à <a href="https://pages.github.com/">GitHub Pages</a>
      et son code source est exposé sur <a href="https://github.com/lapingenieur/lapingenieur.github.io">ce dépôt</a>.
      <br />

      Candidat Parcoursup n°500 506 — lapingenieur — Avril 2023.
    </p>
  </div>
</div>

<style>
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

  .footer {
    align-self: stretch;
    background-color: #3a383e;
    padding: 1em;

    box-shadow: 0 0 10px rgba(0,0,0,0.5);

    color: #9e9aa2;
  }
  .footer a {
    color: #9e9aa2;
    text-decoration: underline;
  }
  .footer p{
    text-align: center;
  }

  @media screen and (min-width: 550px) {
    .main {
      margin: 0 1em;
      width: calc(100% - 2em);

      gap: 2em;
    }
  }
</style>
