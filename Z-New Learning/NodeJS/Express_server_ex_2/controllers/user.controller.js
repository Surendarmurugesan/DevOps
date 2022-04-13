const { default: axios } = require("axios");
const path =require("path");
module.exports.menu = (req,res) => {
    res.send("Menu");
};

module.exports.contactus = (req,res) =>
{
    var file =path.join(global.appRoot,'/public/contactus.html')
    res.sendFile(file);
}

module.exports.metrics = async(req,res) =>
{

    //getMetrics().then(result =>{
     // res.send(result);
    //}).catch(
      //res.send({error : "Error in fwtching"})
    //)
    
    try{
        let result = await getMetrics();
        res.send(result);
    }
    catch(ex)
    {
        res.json({error : "Error in fetching"})
    }
}


const getMetrics = async () =>
{
    try{
        let result = await axios('https://luckyblock.brugu.io/api/v1/getTotalMetrics')
        console.log(result.data.data);
        return result.data.data;
    }
    catch(ex){
        console.log(ex);
        throw ex;
    }
}