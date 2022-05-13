const express = require('express');
const { home, about } = require('../controllers/user.controller')
const router = express.Router();

// router.get("/",(req,res)=>{
//     res.send("<h1>Home</h1>")
// })

// router.get("/about",(req,res)=>{
//     res.send("<h1>About us</h1>")
// });

router.get("/",home);
router.get("/about",about);
router.get('/metrics',metrics)

module.exports = router;