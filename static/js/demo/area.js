// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';




function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin", "Juil", "Aug", "Sep", "Oct", "Nov", "Dec"],
    datasets: [{
      label: "2019 : ",
      lineTension: 0.3,
      backgroundColor: "#fff",
      borderColor: "#ecb390",
      pointRadius: 3,
      pointBackgroundColor: "#df7861",
      pointBorderColor: "#df7861",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "#E74A3B",
      pointHoverBorderColor: "#E74A3B",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [casesmonth19.Jan.length, casesmonth19.Feb.length, casesmonth19.Mar.length, casesmonth19.Apr.length, casesmonth19.May.length, casesmonth19.Jun.length, casesmonth19.Jul.length, casesmonth19.Aug.length, casesmonth19.Sep.length, casesmonth19.Oct.length, casesmonth19.Nov.length, casesmonth19.Dec.length],
    },{
      label: "2020 : ",
      lineTension: 0.3,
      backgroundColor: "#fff",
      borderColor: "#1CC88A",
      pointRadius: 3,
      pointBackgroundColor: "#1CC88A",
      pointBorderColor: "#1CC88A",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "#1CC88A",
      pointHoverBorderColor: "#1CC88A",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [casesmonth20.Jan.length, casesmonth20.Feb.length, casesmonth20.Mar.length, casesmonth20.Apr.length, casesmonth20.May.length, casesmonth20.Jun.length, casesmonth20.Jul.length, casesmonth20.Aug.length, casesmonth20.Sep.length, casesmonth20.Oct.length, casesmonth20.Nov.length, casesmonth20.Dec.length],
    },{
      label: "2021 : ",
      lineTension: 0.3,
      backgroundColor: "#fff",
      borderColor: "#59B3C0",
      pointRadius: 3,
      pointBackgroundColor: "#59B3C0",
      pointBorderColor: "#59B3C0",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "#59B3C0",
      pointHoverBorderColor: "#59B3C0",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [casesmonth21.Jan.length, casesmonth21.Feb.length, casesmonth21.Mar.length, casesmonth21.Apr.length, casesmonth21.May.length, casesmonth21.Jun.length, casesmonth21.Jul.length, casesmonth21.Aug.length, casesmonth21.Sep.length, casesmonth21.Oct.length, casesmonth21.Nov.length, casesmonth21.Dec.length],
    }
  ],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return  number_format(value)  ;
          }
        },
        gridLines: {
          color: "#d4e2d4",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return   datasetLabel + number_format(tooltipItem.yLabel) + " Cas" ;
        }
      }
    }
  }
});

// Area Chart Example
var lip = document.getElementById("lipaseLines");
var lipaseLines = new Chart(lip, {
  type: 'scatter',
  data: {
    datasets: [{
        label: 'Scatter Dataset',
        data: [{
            x: -10,
            y: 0
        }, {
            x: 0,
            y: 10
        }, {
            x: 10,
            y: 5
        }]
    }]
},
  
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return  number_format(value)  ;
          }
        },
        gridLines: {
          color: "#d4e2d4",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return  number_format(tooltipItem.yLabel) + " " + datasetLabel   ;
        }
      }
    }
  }
});
///////

