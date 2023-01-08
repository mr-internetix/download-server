const express = require("express")
const fs = require("fs")
const { Stream } = require("stream")
const send = require('send')
const app = express()

const PORT =  process.env.PORT | 5000


const readStream = fs.createReadStream('exams.zip')
app.get('/',(req,res)=>{
    // res.setHeader('Content-Disposition', 'attachment; filename="exams.pdf"').download('exams.zip')
    // send(req,'./exams.zip').pipe(res)
    res.set('Content-Type','application/zip');
    res.set('Content-Disposition',`attachment; filename=download.zip`);
    res.download('exams.zip')

})



app.listen(PORT, ()=>{

    console.log(`server is running on port ${PORT}`)
})