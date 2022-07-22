import React, { useState, useEffect } from "react";
import TableList from "./components/Table";
import Chart from "./components/Chart";
import { Spinner } from 'react-spinner-animated';

import 'react-spinner-animated/dist/index.css'

function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api")
    .then((response) =>{
      console.log(response);
      return response.json()
    })
    .then((data) => setData(data));
  }, [])
  // console.log(data, 'App');

  return (
    <div>
      {!data.length ? (
        <Spinner/>
      ) : (      
      <div  style={{ display: 'grid' }}>
        <Chart data = {data} />
        <TableList data = {data} />
      </div>)}
    </div>
  )
};

export default App;