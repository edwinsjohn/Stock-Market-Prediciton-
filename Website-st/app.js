const express=require("express");
const bodyParser=require("body-parser");
const app=express();
const axios = require('axios');



app.set("view engine","ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({
  extended: true
}));

app.get("/",function(req,res){
  res.render('home')
});

app.get("/a2cWithOut",function(req,res){

  res.render('a2cWithOut',{p_id:"a2cWT_P",s_id:"a2cWT_s"});
});

app.get("/a2cWith",function(req,res){

  res.render('a2cWith',{p_id:"a2cT_P",s_id:"a2cT_s"});
});

app.get("/a2cRf",function(req,res){
  res.render('a2cRf',{s_id:"a2cd_s"});
});


app.get("/json",function(req,res){
  axios.get('http://127.0.0.1:8000')
      .then(response => {
        chartdata=response.data.data;
        res.send(chartdata);
      })
      .catch(error => {
        console.log(error);
        return error
      });
});

app.get("/news",function(req,res){
  axios.get('http://127.0.0.1:8000/news')
      .then(response => {
        chartdata=response.data.data;
        res.send(chartdata);
      })
      .catch(error => {
        console.log(error);
        return error
      });
});



app.listen(3000,function(){
  console.log("Website Server on Port 3000");
});
