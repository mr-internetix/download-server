const express = require("express")

const app = express()

const PORT =  process.env.PORT | 500



app.get('/',(req,res)=>{

    res.json({message: "it is working "})
})



app.listen(PORT, ()=>{

    console.log(`server is running on port ${PORT}`)
})