const express = require('express');
const router = express.Router();
const {menu,contactus, metrics} = require("../controllers/user.controller")
router.get("/home",(req,res)=>{
    res.send("Home page");
})

router.get('/about',(req,res)=>{
res.send("About");

})

router.get('/menu',menu)
router.get('/contactus',contactus)
router.get('/metrics',metrics)

module.exports = router;