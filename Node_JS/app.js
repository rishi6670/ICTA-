const express=require('express');
const xphbs=require('express-handlebars');

var app=express();

app.engine('handlebars',xphbs({defaultLayout:'mainpage'}));
app.set('view engine','handlebars');

app.use(express.static('views/images'));
app.use(express.urlencoded());

app.get('/',(req,res)=>{
    res.render('index');
});
app.get('/about',(req,res)=>{
    res.render('about');
});
app.get('/contact',(req,res)=>{
    res.render('contact');
});
app.get('/gallery',(req,res)=>{
    res.render('gallery');
});

app.post('/getdata',(req,res)=>{
    var name=req.body.getname;
    //res.send(name);
    console.log(name);
    var address=req.body.getaddress;
    //res.send(address);
    console.log(address);
    var place=req.body.getplace;
    console.log(place);
});



app.listen(5000);