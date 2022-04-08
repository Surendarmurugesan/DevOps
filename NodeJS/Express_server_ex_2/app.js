const express = require('express');
const app = express();
const router = require('./routes');
const path =require("path");
global.appRoot =path.resolve(__dirname);
console.log(global.appRoot);
app.get("/",(req,res) =>{
    res.json({message :"Welcome to Genesys"});
})

app.use("/genesys",router);

app.listen(4050);