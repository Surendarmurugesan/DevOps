const express = require("express");
const app = express();
const routes = require("./routes");
const path = require('path');
global.appRoot = path.resolve(__dirname);
console.log(global.appRoot);
// const app = router();
app.use("/gen", routes);

// //routes will be defined here.
// app.get("/",(req,res)=>{
//     res.json({message: "Welcome to Genesys"});
// })

app.listen(4000);