<script>
  let rand = -1;
  let msg;

  import axios from "axios";
  import { onMount } from "svelte";

  function shutdown() {
      axios.get("./shutdown")
      .then( res => {
        msg = JSON.stringify(res.data);
        console.log(res.data);
      })
  }

  onMount( () => {
    console.log("app started!!!");
    
  })

  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }

  function test() {
    axios.get("./ping")
    .then( res => {
      msg = JSON.stringify(res.data);
      console.log(res.data);
    })
  }

</script>

<h1>Your number is {rand}!</h1>
{#if msg != undefined }
<h3>Heres the message : {msg}</h3>
{/if}
<button on:click={test}>Get message</button>
<button on:click={getRand}>Get a random number</button>
<button on:click={shutdown}>shutdown server</button>
