const express=require('express');

var app=express();
app.get('/',(req,res)=>{
    res.send("<marquee><h1>hello</h1></marquee><br><marquee><h1>Welcome to Ooty</h1></marquee>");
});
app.get('/home',(req,res)=>{
    res.send(' [{"name":"tom","age":23},{"name":"riya","age":23}]');
});

app.listen(3000);