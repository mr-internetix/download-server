const express = require("express")
const fs = require("fs")
const { Stream } = require("stream")
const send = require('send')
const path = require('path')
const app = express()

const PORT =  process.env.PORT | 5000


app.get('/',(req,res)=>{
    // res.setHeader('Content-Disposition', 'attachment; filename="exams.pdf"').download('exams.zip')
    // send(req,'./exams.zip').pipe(res)
    
    res.set('Content-Type','application/zip');
    res.set('Content-Disposition',`attachment; filename=download.zip`);
    res.download(path.resolve('./files.zip'))

})



app.get('/stream',(req,res)=>{

    const stream = fs.createReadStream(path.resolve('./files.zip'));

    res.setHeader('Content-Type', 'application/zip');
    res.setHeader('Content-Disposition', 'inline; filename="exams.zip"');
    stream.pipe(res);
})



app.get('/att',(req,res)=>{

    res.setHeader('Content-Type', 'application/zip').attachment(path.resolve('./files.zip')).send()
})




app.listen(PORT, ()=>{

    console.log(`server is running on port ${PORT}`)
})