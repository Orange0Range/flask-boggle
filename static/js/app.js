let timeUp = false

$('button').on('click', async function(e){
    e.preventDefault();
    const guess = $('#guess').val();
    if(!timeUp){
        
        let res = await axios.post("/guess", {guess:guess})
        reply = res.data.result
        score = res.data.score
        $('body').append(`<h4>${reply}</h4> <h4>Score: ${score}</h4>`)
    }
    else{
        $('body').append(`<h4>Game Over!</h4>`)
    }

    setTimeout(function(){
        $('h4').remove()
    }, 1000);

    $('#guess').val("")
})


setTimeout(async function(){
    timeUp = true
    let res = await axios.post("/done", {data: 'done'})
    console.debug(res)
}, 60000)