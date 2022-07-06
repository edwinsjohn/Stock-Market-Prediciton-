// Make an HTTP request to the /json/ route of our express server:
const log = console.log;

const chartProperties = {
  width:1271,
  height:536,
  timeScale:{
    timeVisible:true,
    secondsVisible:false,
  }
}

const domElement = document.getElementById('tvchart');
const news1_i = document.getElementById('news1_img');
const news1_title = document.getElementById('news1_t');
const news2_i = document.getElementById('news2_img');
const news2_title = document.getElementById('news2_t');
const news3_i = document.getElementById('news3_img');
const news3_title = document.getElementById('news3_t');
const news4_i = document.getElementById('news4_img');
const news4_title = document.getElementById('news4_t');
const news5_i = document.getElementById('news5_img');
const news5_title = document.getElementById('news5_t');


const priceH3= document.getElementById('live-price');
const chart = LightweightCharts.createChart(domElement,chartProperties);
const candleSeries = chart.addCandlestickSeries();
// cdata=[{'time': 1656084240, 'open': 853.3, 'high': 853.5, 'low': 853.0, 'close': 853.0}, {'time': 1656084300, 'open': 853.0, 'high':
// 853.9, 'low': 852.6, 'close': 853.45}, {'time': 1656084360, 'open': 853.8, 'high': 854.0, 'low': 853.2, 'close': 853.5}, {'time': 1656084420, 'open': 853.5, 'high': 853.8, 'low': 853.35, 'close':
// 853.7}, {'time': 1656084480, 'open': 853.7, 'high': 853.95, 'low': 853.1, 'close': 853.5}, {'time': 1656084540, 'open': 853.45, 'high': 853.7, 'low': 851.1, 'close': 852.0}]
// log(cdata);
// candleSeries.setData(cdata);
dataList=[]



fetch('/json')
  .then(res => res.json())
  .then(data => {
    candleSeries.setData(data);
  })
  .catch(err => log(err))

  fetch('/news')
    .then(res => res.json())
    .then(data => {
      console.log(data)
      news1_i.src=data.news1.img;
      news1_title.innerText=data.news1.head
      news2_i.src=data.news2.img;
      news2_title.innerText=data.news2.head
      news3_i.src=data.news3.img;
      news3_title.innerText=data.news3.head
      news4_i.src=data.news4.img;
      news4_title.innerText=data.news4.head
      news5_i.src=data.news5.img;
      news5_title.innerText=data.news5.head
    })
    .catch(err => log(err))

//   const socket = new WebSocket('ws://localhost:8001');
//
// socket.addEventListener('message', function (event) {
//
//     a=JSON.parse(event.data);
//     log(a);
//     candleSeries.update(a);
// });

const socket1 = new WebSocket('ws://localhost:8001');

socket1.addEventListener('message', function (event) {

    live=JSON.parse(event.data);
    // console.log(live)
    price=(live.chartdata.close);
    // console.log(price)
    priceH3.innerText=price
    // candleSeries.update(live);
});

const socket2 = new WebSocket('ws://localhost:8005');

socket2.addEventListener('message', function (event) {

    model=JSON.parse(event.data);
     console.log(model)
    if(!!document.getElementById("a2cWT_P")){

      t_price=(model.A2C_W_T.price);
      document.getElementById("a2cWT_P").innerText=parseFloat(t_price).toFixed(2);
      document.getElementById("a2cWT_s").innerText=model.A2C_W_T.state;
    }
    if(!!document.getElementById("a2cT_P")){

      t_price=(model.A2CT.price);
      document.getElementById("a2cT_P").innerText=parseFloat(t_price).toFixed(2);
      document.getElementById("a2cT_s").innerText=model.A2CT.state;
    }
    if(!!document.getElementById("a2cd_s")){
      console.log(model.A2CD.state)
      document.getElementById("a2cd_s").innerText=model.A2CD.state;
    }




});



//
// const axios = require('axios');
// const getdata = () => {
//     return axios.get('http://127.0.0.1:8000')
//       .then(response => {
//         chartdata=response.data.data;
//         return chartdata
//       })
//       .catch(error => {
//         console.log(error);
//         return error
//       });
// };
//
// getdata().then(function(result) {
//    module.exports={getdata}// "Some User token"
// })
