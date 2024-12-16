import React, { useState } from "react";
import axios from "axios";
import "./Airlines.css";

const AIRLINES_API_URL = "http://localhost:8080/airlines";

function Airlines() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const makeRequest = async (shouldError) => {
    const apiUrl = shouldError ? `${AIRLINES_API_URL}?raise=true` : AIRLINES_API_URL;

    console.log(shouldError);
    console.log(apiUrl);

    try {
      const response = await axios.get(apiUrl);
      setData(response.data);
      setError(null);
    } catch (error) {
      setError(error.message);
      setData(null);
    }
  }

  return (
    <div className="airlines">
      Airlines
      <div>
        <button className="app-btn" onClick={() => makeRequest(false)}>Get Airlines</button>
      </div>
      <div>
        <button className="app-btn" onClick={() => makeRequest(true)}>Make Error Request</button>
      </div>
      {error ? <p>Error: {error}</p> : null}
      {data ? <p>Response: {JSON.stringify(data)}</p> : null}
    </div>
  );
}

export default Airlines;
