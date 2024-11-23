import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useState, useEffect } from 'react';

function sayHi(){
    // alert("Hi");
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

        <form onSubmit={sayHi()}>
        <label>
          Scenario-Id: 
          <input type="text" value=""/>
        </label>
        <input type="submit" value="Load Scenario" />
      </form>

        {data.vehicles.map((item) => (
          <div key={item.id} class={item.isAvailable ? "vehicle available" : "vehicle occupied"} >
            <div class="positionProperty"><b>Position:</b> {item.coordX}, {item.coordY}</div>
            <div><b>isAvailable:</b> {item.isAvailable}</div>
            <div><b>vehicleSpeed:</b> {item.vehicleSpeed}</div>
            <div><b>customerId:</b> {item.customerId}</div>
            <div><b>remainingTravelTime:</b> {item.remainingTravelTime}</div>
            <div><b>distanceTravelled:</b> {item.distanceTravelled}</div>
            <div><b>activeTime:</b> {item.activeTime}</div>
            <div><b>numberOfTrips:</b> {item.numberOfTrips}</div>
            <div class="idProperty">ID: {item.id}</div>
          </div>
        ))}
    </div>
  );
}

export default App;
