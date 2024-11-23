import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useState, useEffect } from 'react';

function GetCarComponent(name){
    return (
        <h1>{name}</h1>
    )
}

function App() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true); 

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/getData")
          .then((res) => {
            if (!res.ok) throw new Error("Fehler beim Abrufen der Daten");
            return res.json();
          })
          .then((data) => {
            setData(data); 
            setLoading(false);
          })
      }, []);

      if (loading) return <p>Lädt...</p>;

  return (
    <div className="App">
        <h1>Taxi-Overview</h1>
        {data.vehicles.map((item) => (
          <div key={item.id} class={item.isAvailable ? "vehicle available" : "vehicle occupied"} >
            <div class="positionProperty"> <b>Position:</b> {item.coordX}, {item.coordY}</div>
            <div class="idProperty">ID: {item.id}</div>
          </div>
        ))}
    </div>
  );
}

export default App;
