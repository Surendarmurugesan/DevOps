const express = require("express");
const app = express();
const { createServer } = require("http");
const { Server } = require("socket.io");
const httpServer = createServer(app);
const io = new Server(httpServer, { /* options */ });

app.get("/", (req,res)=>{
    const filePath = __dirname;
    console.log(filePath)
    res.sendFile(filePath+"/client/index.html");
});

io.on("connection", (socket) => {

    console.log(socket.id);

    socket.on('disconnect', ()=>{
        console.log("User disconnected =",socket.id)
    });
    socket.on('privateMessage', (userid,data)=>{
        io.to(userid).emit(data);
    });

    io.emit("groupMessage",socket.id+"has joined.");
    //listen to the chat message sent by the client

    socket.on('chat',(data)=>{
        console.log(data);
        io.emit('groupMessage',data)
    })
    socket.emit("Welcome","Im from the server")

});

httpServer.listen(3000,(err)=>{
    if(err){
        console.log(err);
    }
    else{
        console.log("Server running on port 3000");
    }
});