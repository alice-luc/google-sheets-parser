import React, { useState, useEffect } from "react";
import TableList from "./components/Table";
import Chart from "./components/Chart";
import { Spinner } from 'react-spinner-animated';

import 'react-spinner-animated/dist/index.css'

function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api/get-statistics")
    .then((response) =>response.json())
    .then((data) => setData(data));
  }, [])
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