const express = require("express")
const fs = require("fs")
const { Stream } = require("stream")
const send = require('send')
const app = express()

const PORT =  process.env.PORT | 5000


// const readStream = fs.createReadStream('exams.zip')
app.get('/',(req,res)=>{
    // res.setHeader('Content-Disposition', 'attachment; filename="exams.pdf"').download('exams.zip')
    send(req,'./exams.zip').pipe(res)
})



app.listen(PORT, ()=>{

    console.log(`server is running on port ${PORT}`)
})