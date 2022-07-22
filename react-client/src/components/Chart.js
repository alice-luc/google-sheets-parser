import React, { useRef, useLayoutEffect } from 'react'
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";


function Chart(props) {
  const chart = useRef(null);
  // console.log(props.data, "Chart");

  const total_data = {
    usd: 0,
    rub: 0,
    num: 0
  }; 
  const style = {
    main: {
      border: '2px solid #2596be', 
      borderRadius: '5px', 
      marginBottom: "30px", 
      marginTop: "30px", 
      display: 'flex', 
      alignItems: 'flex-start', 
      marginLeft: '10px', 
      marginRight: '10px'
      },
    total: {
      marginLeft: '50px', 
      display: 'flex', 
      alignItems: 'center', 
      flexDirection: 'column',
      border: '2px solid #2596be', 
      borderRadius: '5px',
      marginBottom: '20px'
      },
    totalHeader: { 
      textAlign: "center", 
      fontSize: "20px", 
      paddingTop: '20px', 
      paddingBottom: '20px', 
      backgroundColor: '#2596be', 
      width: '100%', 
      color: '#FFFFFF',
      },
    totalText: {
      paddingTop: '10px'
    }
  }
  props.data.forEach((obj) => {
    total_data.rub += obj.rub_price;
    total_data.usd += obj.usd_price;
    total_data.num += 1;
  })
  useLayoutEffect(() => {
    let x = props.data && am4core.create("chartdiv", am4charts.XYChart);

    x.paddingRight = 20;
    x.paddingTop = 50;

    for (let i = 0; i < props.data.length; i++) {
      const date = props.data[i].date.split('.');
      // console.log(date)
      x.data.push({ 
        date: new Date(date[2], parseInt(date[1])-1, date[0]),
        name: props.data[i].order_num,
        value: props.data[i].rub_price.toFixed(2)
    })

  }
    x.events.on("beforedatavalidated", function(ev) {
      x.data.sort((a, b) => {
        return (new Date(a.date)) - (new Date(b.date));
      });
    });
    // console.log(x.data)
    
    let title = x.titles.create();
    title.text = "Статистика поставок";
    title.fontSize = 25;
    title.fontWeight = "500";
    title.fontFamily = "Montserrat"
    title.fill = '#888'

    title.paddingTop = 10;
    title.paddingBottom = 50;
    
    let dateAxis = x.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.grid.template.location = 0;
    dateAxis.title.text = "Дата поставки";
    dateAxis.title.fill = '#888';
    dateAxis.title.fontFamily = "Montserrat";

    let valueAxis = x.yAxes.push(new am4charts.ValueAxis());
    valueAxis.tooltip.disabled = true;
    valueAxis.renderer.minWidth = 35;
    valueAxis.title.text = "Стоимость, ₽";
    valueAxis.title.fill = '#888';
    valueAxis.title.fontFamily = "Montserrat";

    let series = x.series.push(new am4charts.LineSeries());
    series.dataFields.dateX = "date";
    series.dataFields.valueY = "value";
    series.fill = '#2596be';
    series.tooltipText = "Дата: {date.formatDate('d MMM, yyyy')}\n Стоимость: {valueY.value} ₽";
    x.cursor = new am4charts.XYCursor();

    let circleBullet = series.bullets.push(new am4charts.CircleBullet());
    circleBullet.circle.stroke = am4core.color("#fff");
    circleBullet.circle.strokeWidth = 2;
    
    chart.current = x;

    return () => {
      x.dispose();
    };
  }, [props]);

  return (
    <div style={style.main}>

      <div id="chartdiv" style={{ width: "70%", height: "500px"}}></div>
    
      <div style={{ width: '25%', marginTop: '80px'}}>
      <div style={style.total}>

        <h3 style={style.totalHeader}>Сумма, ₽</h3>

        <p style={style.totalText}>{total_data.rub.toLocaleString()}</p>

      </div>
      <div style={style.total}>

        <h3 style={style.totalHeader}>Сумма, $</h3>

        <p style={style.totalText}>{total_data.usd.toLocaleString()}</p>

      </div>
      <div style={style.total}>

        <h3 style={style.totalHeader}>Число поставок </h3>

        <p style={style.totalText}>{total_data.num}</p>
        </div>
      </div>
    </div>
  );
}

export default Chart