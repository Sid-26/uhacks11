<script>
    // logic goes here

</script>

<div class = "container">
    <div class="cohere">
    
    </div>
    <div class="input">
        <input
                type="text"
                id="cohere-input"
                class="form-control"
                placeholder="Nostalgia..."
        />
        <button id="send-button" style="margin-top: 10px;">Send</button>
    </div>
    
</div>


<style>
    .cohere {
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
    }

    
</style>