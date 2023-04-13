<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
  import Plate from "$lib/blockons/Plate.svelte";
</script>

<Blockon id="lowlevel">
  <h1>
    Programmation Bas-Niveau
  </h1>

  <p>
    Un autre pan de l'informatique que j'apprécie est la programmation davantage bas-niveau&nbsp;:
    j'ai des connaissances en <a href="https://fr.wikipedia.org/wiki/C_(langage)">langage C</a>,
    et dans les plus modernes <a href="https://rust-lang.org/">Rust</a>,
    <a href="https://go.dev">Go</a> et <a href="https://vlang.io">V</a>. Quelques uns de mes projets&nbsp;:
  </p>

  <ul>
    <li>
      <a href="https://github.com/lapingenieur/rsmpeg">Rsmpeg</a> une frêle interface graphique au logiciel
      <a href="https://ffmpeg.org/">FFmpeg</a> en langage Rust,
      avec la librairie <a href="https://github.com/emilk/egui">egui</a>.
    </li>

    <li>
      J'ai programmé différents projets sur des cartes <a href="https://www.arduino.cc/">Arduino</a>,
      notamment la gestion automatique de la porte d'un poulailler.
    </li>

    <li>
      <a href="https://fr.wikipedia.org/wiki/Windows_Subsystem_for_Linux">WSL2</a> est isolé dans un sous-réseau
      virtuel, on ne peut pas y accéder depuis le réseau local. <a href="https://github.com/lapingenieur/tunnel">Tunnel</a>,
      écrit en langage V, met en place une session <a href="https://fr.wikipedia.org/wiki/Secure_Shell">SSH</a>
      <a href="https://doc.ubuntu-fr.org/tutoriel/reverse_ssh">renversée</a>
      qui connecte un port local (WSL) au port équivalent exposé sur le réseau local (Windows).
    </li>
  </ul>

  <p>
    Je suis également à l'iniciative de la page française
    <a href="https://fr.wikipedia.org/wiki/Types_de_donn%C3%A9e_du_langage_C">types de données du langage C</a>
    du site Wikipédia.
  </p>
</Blockon>

<style>
  ul > li:not(:last-child) {
    margin-bottom: 1em;
  }
</style>
