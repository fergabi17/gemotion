// Global Options
// Chart.defaults.global.defaultFontFamily = 'Kanit';
Chart.defaults.global.defaultFontSize = 14;
// Chart.defaults.global.defaultFontColor = '#151515';
// Chart.defaults.global.animation.duration = 2000;
// Chart.defaults.global.animation.easing = 'easeInOutBounce';


function createChart(chartObject) {
    var canvas = document.getElementById(chartObject.canvasId).getContext('2d');

    new Chart(canvas, {
        type: chartObject.type, // bar, horizontalBar, pie, line, doughnut, radar, polarArea
        data: chartObject.data,
        options: chartObject.options
    })
}

var playedChart = {
    canvasId: 'played-chart',
    type: 'pie',
    options: {
        legend: {
            display: false
        },
        tooltips: {
            callbacks: {
                label: function (tooltipItem, data) {
                    return data['labels'][tooltipItem['index']] + ': ' + data['datasets'][0]['data'][tooltipItem['index']] + '%';
                }
            }
        }
    },
    data: {
        labels: [],
        datasets: [{
            label: "Played chart label",
            data: [],
            backgroundColor: ['rgba(91, 192, 222, 0.9)', 'rgba(255,255,255, 0.9)'],
            borderWidth: 1,
            borderColor: 'rgba(0,0,0,0.0)',
            hoverBorderWidth: 3,
            hoverBorderColor: 'rgba(91, 192, 222,1)'
        }]
    }
};

var emotionsChart = {
    canvasId: 'emotions-chart',
    type: 'horizontalBar',
    options: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 0.7,
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                ticks: {
                    min: 0
                }
            }],
            yAxes: [{
                stacked: true
            }]
        },
        tooltips: {
            callbacks: {
                label: function (tooltipItem, data) {
                    return data['labels'][tooltipItem['index']] + ': ' + data['datasets'][0]['data'][tooltipItem['index']] + '%';
                }
            }
        }
    },
    data: {
        labels: [],
        datasets: [{
            backgroundColor: [
                'rgba(91, 192, 222, 1)',
                'rgba(91, 192, 222, 0.9)',
                'rgba(91, 192, 222, 0.8)',
                'rgba(91, 192, 222, 0.7)',
                'rgba(91, 192, 222, 0.6)',
                'rgba(91, 192, 222, 0.5)',
                'rgba(91, 192, 222, 0.4)',
                'rgba(91, 192, 222, 0.3)',
                'rgba(91, 192, 222, 0.2)',
                'rgba(91, 192, 222, 0.1)',
                'rgba(91, 192, 222, 0.0)',
            ],
            barPercentage: 0.5,
            barThickness: 1,
            maxBarThickness: 8,
            minBarLength: 2,
            data: []
        }]
    }
};

var categoryChart = {
    canvasId: 'category-chart',
    type: 'radar',
    options: {
        scale: {
            ticks: {
                stepSize: 10
            },
            pointLabels: {
                fontSize: 16
            }
        },
        legend: {
            display: false
        },
        tooltips: {
            callbacks: {
                label: function (tooltipItem, data) {
                    return data['labels'][tooltipItem['index']] + ': ' + data['datasets'][0]['data'][tooltipItem['index']] + '%';
                },
            }
        }
    },
    data: {
        labels: [],
        datasets: [{
            label: "",
            data: [],
            backgroundColor: ['rgba(91, 192, 222, 0.8)'],
            borderColor: "rgba(200,0,0,0.6)",
            radius: 6,
            pointRadius: 6,
            pointBorderWidth: 3,
            pointBackgroundColor: "white",
            pointBorderColor: "rgba(200,0,0,0.6)",
            pointHoverRadius: 10,
            borderWidth: 1,
            borderColor: 'rgba(255,255,255,0.0)',
            hoverBorderWidth: 2,
            hoverBorderColor: 'rgba(91, 192, 222,0.8)'
        }]
    }
}

function populateAndCreateChart(chartInfo, chartSettings) {
    chartInfo = JSON.parse(chartInfo.replace(/&quot;|&#x27;/g, '\"'));
    chartSettings.data.labels = Object.keys(chartInfo);
    chartSettings.data.datasets[0].data = Object.values(chartInfo);
    createChart(chartSettings);
}



