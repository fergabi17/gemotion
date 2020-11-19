// Global Options
// Chart.defaults.global.defaultFontFamily = 'Kanit';
// Chart.defaults.global.defaultFontSize = 8;
// Chart.defaults.global.defaultFontColor = '#151515';
// Chart.defaults.global.animation.duration = 2000;
// Chart.defaults.global.animation.easing = 'easeInOutBounce';


function chartData(canvasId, data, title, label, legend, colors, type) {
    return {
        canvasId: canvasId,
        data: data.replace(/&quot;/g, '\"'),
        title: title,
        label: label,
        legend: legend,
        colors: colors,
        type: type,
    }
}

function createChart(chartObject) {
    var canvas = document.getElementById(chartObject.canvasId).getContext('2d');
    chartObject.data = JSON.parse(chartObject.data);

    var colors = [
        'rgba(255,255,255,0.6)',
        'rgba(155,155,155,0.6)',
        'rgba(80,80,80,0.4)',
        'rgba(0,0,0,0.2)',
    ];


    new Chart(canvas, {
        type: chartObject.type, // bar, horizontalBar, pie, line, doughnut, radar, polarArea
        labels: "labels fora",
        data: {
            labels: false,
            datasets: [{
                label: "esse eh o label",
                data: Object.values(chartObject.data).concat([0]),
                backgroundColor: chartObject.colors,
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.8)',
                hoverBorderWidth: 3,
                hoverBorderColor: 'rgba(91, 192, 222,0.8)'
            }]
        },
        options: function () {
            if (chartObject.canvasId == 'category-chart') {
                return {
                    scale: {
                        ticks: {
                            beginAtZero: true,
                            min: 0,
                            //   max: 100,
                            stepSize: 1
                        },
                        pointLabels: {
                            fontSize: 16
                        }
                    },
                    tooltips: {
                        enabled: true
                    },
                }
            } else {
                return {
                    title: {
                        display: chartObject.title[0],
                        text: chartObject.title[1],
                        fontStyle: 'light'
                    },
                    legend: {
                        display: chartObject.legend,
                        position: 'bottom',
                        labels: {
                            fontColor: '#000',
                            fontSize: 12,
                        }
                    },
                    layout: {
                        padding: {
                            left: 10,
                            right: 10,
                            bottom: 0,
                            top: 0
                        }
                    },
                    tooltips: {
                        enabled: true
                    }
                }
            }
        }  
    })
}    
