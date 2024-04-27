// game
const gameRoom = document.querySelector(".game-container")
const boxes = document.querySelectorAll(".box")
const gameMessage = document.querySelector(".game-message")


// update game
const box1 = document.querySelector(".box1")
const box2 = document.querySelector(".box2")
const box3 = document.querySelector(".box3")
const box4 = document.querySelector(".box4")
const box5 = document.querySelector(".box5")
const box6 = document.querySelector(".box6")
const box7 = document.querySelector(".box7")
const box8 = document.querySelector(".box8")
const box9 = document.querySelector(".box9")
const gameNotStarted = document.querySelector(".game-not-started")
const startButt = document.querySelector(".game-not-started button")
const player2 = document.querySelector(".player2")


setInterval(()=>{
    roomId = gameRoom.getAttribute("data-id")
    formData = new FormData()
    formData.append("id", roomId)

    fetch("/update-game", {
        body: formData,
        method: "POST",
    }).then(response=>response.json())
    .then(data=>{
        if(data){
            if (data.waiting){
                gameMessage.textContent = data.message
                gameNotStarted.style.display = "flex"
                
            }
            
            if (data.started){
                gameMessage.textContent = data.message
                gameNotStarted.style.display = "none"
    
                player2.textContent = data.player2
                box1.textContent = data.box1
                box2.textContent = data.box2
                box3.textContent = data.box3
                box4.textContent = data.box4
                box5.textContent = data.box5
                box6.textContent = data.box6
                box7.textContent = data.box7
                box8.textContent = data.box8
                box9.textContent = data.box9
                gameMessage.textContent = data.message

                if(data.next_player){
                    boxes.forEach(box=>{
                        console.log(box.textContent)
                        box.onclick = ()=>{
                            playGame(box)
                        }
                    })
                }else{
                    boxes.forEach(box=>{
                        console.log(box.textContent)
                        box.onclick = ()=>{}
                    })
                }
            }

        }
    })
}, 1500)


const playGame = (box)=>{
    if(box.textContent == ""){
        gameNotStarted.style.display = "flex"
        boxNumber = box.getAttribute("data-box")
        roomId = gameRoom.getAttribute("data-id")
        formData = new FormData()
        formData.append("box", boxNumber)
        formData.append("id", roomId)

        console.log(roomId)
        console.log(boxNumber)

        fetch("/play-game", {
            body: formData,
            method: "POST",
        }).then(response=>response.json())
        .then(data=>{
            if(data.message){
                gameMessage.textContent = data.message
            }
        })
    }
}


boxes.forEach(box=>{
    console.log(box.textContent)
    box.onclick = ()=>{
        gameNotStarted.style.display = "flex"
        playGame(box)
    }
})
