const express = require("express")
const fs = require("fs")
const { Stream } = require("stream")
const send = require('send')
const path = require('path')
const app = express()
app.use(express.static('public'))
const PORT =  process.env.PORT | 5000


app.get('/',(req,res)=>{
    res.download(path.resolve('./public/files.zip'))

})



app.get('/stream',(req,res)=>{

    const stream = fs.createReadStream(path.resolve('./files.zip'));

    res.setHeader('Content-Type', 'application/zip');
    res.setHeader('Content-Disposition', 'inline; filename="exams.zip"');
    stream.pipe(res);
})



app.listen(PORT, ()=>{

    console.log(`server is running on port ${PORT}`)
})