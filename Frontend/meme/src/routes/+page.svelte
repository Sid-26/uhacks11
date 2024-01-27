<script>
    // logic goes here

</script>


<head>
    <title>System.css Starter</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="https://unpkg.com/@sakun/system.css" />
</head>
<body>

    <div class="window">
        <div class="title-bar"> 
            <button aria-label="Close" class="close"></button>
            <h1 class="title">Search</h1>
            <button aria-label="Resize" disabled class="hidden"></button>
        </div>
        <div class="separator"></div>
        
        <div class="modeless-dialog">
            <section class="field-row" style="justify-content: flex-start">
                <label for="text_find" class="modeless-text">Find:</label>
                <input id="text_find" type="text" style="width:100%;" placeholder="">
            </section>
            <section class="field-row" style="justify-content: flex-end">
                <button class="btn">Cancel</button>
                <button class="btn" style="width:95px;">Find</button>
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
          Results will be shown here
        </div>
      </div>
        
</body>



<style>
    @import "src/lib/theme/style.css"
    
    /* .cohere {
        width: 100%;
        max-width: 1400px;
        height: 1000px;
        margin: 2rem auto;
        display: flex;
        flex-direction: column;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background: linear-gradient(135deg, #0000AA 0%, #000000 100%);
    }
    .container {
        width: 100%;
        max-width: 1400px;
        height: 1000px;
        margin: 2rem auto;
        display: flex;
        flex-direction: column;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background: linear-gradient(135deg, #0000AA 0%, #000000 100%);
    }

    button {
        width: 70px;
        background: linear-gradient(135deg, #0000AA 0%, #55FFFF 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 15px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        width: 100px;
    }

    .input {
        padding: 10px;
        background: linear-gradient(135deg, #0000AA 0%, #55FFFF 80%);
    }

    #cohere-input {
        width: 100%;
        padding: 10px;
        margin-right: 10px;
        border: none;
        border-radius: 25px;
        box-sizing: border-box;
        overflow: scroll; 
    } */

    
</style>