import React, { useState, useEffect } from "react";

function App() {

  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/api/get-statistics")
    .then((response) =>response.json())
    .then((data) => setData(data));
  }, [])
  return (
    <div>
      <tr>
        {( typeof data === "undefined" ) ? (
        <p>Loading...</p>
      ): (
        (Object.keys(data)).map((value, i) => (
          <th key={i}>{value}</th>
        ) && (
          (Object.values(data)).map((value, i) => ( <th key={i}>{value}</th> 
          ))
        ))

        )}
      </tr>
      {/* {( typeof data['заказ №']=== "undefined" ) ? (
        <p>Loading...</p>
      ): (

        data['заказ №'].map((value, i) => (
          <p key={i}>{value}</p>
        ))
      )} */}
    </div>
  )
};

export default App;