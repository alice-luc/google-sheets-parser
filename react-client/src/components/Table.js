import React from 'react'
import { Table } from '@mui/material'

function TableList(props) {
  const namesMap = {
    d_id: "№",
    order_num: "заказ, №",
    date: "срок поставки",
    usd_price: "стоимость, $",
    rub_price: "стоимость, ₽"
  };

  const style = {
    table: {
       border: '2px solid #2596be', 
       textAlign: 'center', 
       borderCollapse: 'separate',
       borderRadius: '5px',
    },
    tableHead: { 
      backgroundColor: "#2596be", 
      fontSize: 18, 
      fontWeight: "bold",
      color: '#FFFFFF',
      textTransform: 'uppercase',
    }

  };
  return (
    <div style={{ marginLeft: '10px', marginRight: '10px'}}>
  <Table className='table' style = {style.table}>
    <thead>
      <tr key='0' style={style.tableHead}>
        <td >{namesMap['d_id']}</td>
        <td>{namesMap['order_num']}</td>
        <td>{namesMap['date']}</td>
        <td>{namesMap['usd_price']}</td>
        <td>{namesMap['rub_price']}</td>
      </tr>
    </thead>
    <tbody>
    {props.data && props.data.map((value, i) => (
      
      <tr key={value.id}>
        <td>{value.d_id}</td>
        <td>{value.order_num}</td>
        <td>{value.date}</td>
        <td>{value.usd_price}</td>
        <td>{value.rub_price.toFixed(2)}</td>
      </tr>
      
    ))}
    </tbody>
  </Table>
  </div>

  )
}

export default TableList