const http = require('http');
const server = http.createServer((req,res)=>{
    res.write("<h1> Hello Genesys </h1>");
    res.end();
});

server.listen(4000,(err,result)=>{
    if(err){
        console.log(err);
    }
    else{
        console.log("Server Running in the port 4000")
    }
})