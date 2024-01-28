<script lang="ts">
    import { onMount } from 'svelte';

    let apiURL = 'http://127.0.0.1:5000';
    let movieName = '';
    let year = '';
    let trivia = '';

    function getData(): void {

        const yearData = {
        
        };
        // Make a simple POST request to the Flask API endpoint
        fetch(apiURL + '/get-movie', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({"year": document.getElementById('text_find').value})
            
        })
            .then((response) => response.json())
            .then((data) => {
            movieName = data.movie_name;
            year = data.year;
            trivia = data.trivia;
            console.log(data);
            // Show the data in the window-pane
            const windowPane = document.querySelector('.window-pane');
            windowPane.innerHTML = `Movie name: ${movieName}<br><br>Year: ${year}<br><br>Trivia: ${trivia}`;
        })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }
</script>


<head>
    <title>NostalgAI</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="https://unpkg.com/@sakun/system.css" />
</head>
<body>
    <div class="window">
        <div class="title-bar">
          <button aria-label="Close" class="close"></button>
          <h1 class="title">Welcome To NostalgAI</h1>
          <button aria-label="Resize" class="resize"></button>
        </div>
        <div class="details-bar">
          <span>Revive</span>
          <span>The</span>
          <span>Past</span>
        </div>
      
        <div class="window-pane">
          Find a nostlagic movie from 1980 to 2015!
        </div>
      </div>
    <div class="window">
        <div class="title-bar"> 
            <button aria-label="Close" class="close"></button>
            <h1 class="title">Search</h1>
            <button aria-label="Resize" disabled class="hidden"></button>
        </div>
        <div class="separator"></div>
        
        <div class="modeless-dialog">
            <section class="field-row" style="justify-content: flex-start">
                <label for="text_find" class="modeless-text">Enter year:</label>
                <input id="text_find" type="text" style="width:100%;" placeholder="">
            </section>
            <section class="field-row" style="justify-content: flex-end">
                <button class="btn" style="width:95px;" on:click={getData}>Find</button>
            </section>
        </div>
    </div>
    <div class="window">
        <div class="title-bar">
          <button aria-label="Close" class="close"></button>
          <h1 class="title">Results</h1>
          <button aria-label="Resize" class="resize"></button>
        </div>
        <div class="separator"></div>
      
        <div class="window-pane">
          
        </div>
      </div>
        
</body>



<style>
    @import "src/lib/theme/style.css"
</style>