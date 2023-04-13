<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
</script>

<Blockon id="milky">
  <h1>Chiptune : MilkyTracker</h1>

  <p>
    J'ai découvert la programmation de musique dite "chiptune" ou plus couramment "8-bits" pendant le confinement
    de 2020, via le logiciel <a href="https://milkytracker.org/">MilkyTracker</a>.
    Le musicien programme sa création dans une sorte de tableau/matrice avec des valeurs hexadécimales,
    avec une colonne par piste et les lignes représentant l'avancement dans le temps.
    Chaque piste peut jouer de différents instruments, et chaque instrument peut être composé d'un ou plusieurs samples.
    Des effets rudimentaires tels que le vibrato ou glissando peuvent être indiqués.
  </p>

  <div class="img-1">
    <img src="https://doc.ubuntu-fr.org/_media/tutoriel/tracker/milkytracker_01.png" alt="Logiciel MilkyTracker" />
  </div>

  <p>
    Voici une reprise du <a href="https://youtu.be/hN-HSJU6G18">thème de Riju</a> que j'ai écrite avec ce logiciel.
  </p>

  <p>
    Écrire une musique de cette manière permettait aux programmeurs des débuts de l'informatique d'intégrer
    une bande son à leurs jeux sans trop utiliser d'espace mémoire.
    Des compositions comme <a href="https://youtu.be/pgPEaI0GHBI">Commando</a> de Rob Hubbards rendent à perfection
    cet aspect&nbsp;: peu plaisant à l'oreille, ces morceaux sont d'une complexité remarquable.
    Le chiptune n'a aujourd'hui plus aucun intérêt de ce point de vue.
  </p>
</Blockon>

<style>
  .img-1 {
    max-width: 100%;
    max-height: 100%;

    display: flex;
    justify-content: center;
  }
  .img-1 img {
    max-height: 30em;
    max-width: 100%;
  }
</style>
