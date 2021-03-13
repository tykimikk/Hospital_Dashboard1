// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Age
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Moins de 20", "20 a 40" ,"40 a 60", "Plus de 60"],
    datasets: [{
      data: [casesage.tw.length, casesage.ttf.length, casesage.fts.length,casesage.six.length],
      backgroundColor: ['#1cc88a','#f7d377','#3EBCCE' , '#ecb390'],
      hoverBackgroundColor: ['#17a673' , '#f6c23e','#2791a1', '#df7861'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// TRT
var trtc = document.getElementById("trtmedChir");
var trtmedChir = new Chart(trtc, {
  type: 'doughnut',
  data: {
    labels: ["Trt Medicale Seulement", "Trt Medical + Chirurgical"],
    datasets: [{
      data: [casestrt.chir.length, casestrt.med.length],
      backgroundColor: ['#f2966f','#1CC88A'],
      hoverBackgroundColor: ['#e48257','#01ba76'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});

// TRT
var sirsl = document.getElementById("sirs");
var sirs = new Chart(sirsl, {
  type: 'doughnut',
  data: {
    labels: ["SIRS POSITIF", "SIRS NEGATIF"],
    datasets: [{
      data: [sirs.pos.length, sirs.neg.length],
      backgroundColor: ['#E18E7D','#77B255'],
      hoverBackgroundColor: ['#E18E7D','#77B255'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 50,
  },
});