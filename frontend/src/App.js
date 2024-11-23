import logo from "./logo.svg";
import "./App.css";
import React from "react";
import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [scenarioId, setScenarioId] = useState(null);

  const fetchData = async (sc) => {
    setLoading(true);
    const res = await fetch(
      `http://127.0.0.1:5000/api/getData?scenarioId=${sc}`
    );
    if (!res.ok) throw new Error("Fehler beim Abrufen der Daten");
    const data = await res.json();
    setData(data);
    setLoading(false);
  };

  const renderData = () =>
    data?.vehicles.map((item) => (
      <div
        key={item.id}
        class={item.isAvailable ? "vehicle available" : "vehicle occupied"}>
        <div class="positionProperty">
          <b>Position:</b> {item.coordX}, {item.coordY}
        </div>
        <div>
          <b>isAvailable:</b> {item.isAvailable}
        </div>
        <div>
          <b>vehicleSpeed:</b> {item.vehicleSpeed}
        </div>
        <div>
          <b>customerId:</b> {item.customerId}
        </div>
        <div>
          <b>remainingTravelTime:</b> {item.remainingTravelTime}
        </div>
        <div>
          <b>distanceTravelled:</b> {item.distanceTravelled}
        </div>
        <div>
          <b>activeTime:</b> {item.activeTime}
        </div>
        <div>
          <b>numberOfTrips:</b> {item.numberOfTrips}
        </div>
        <div class="idProperty">ID: {item.id}</div>
      </div>
    ));

  return (
    <div className="App">
      <h1>Taxi-Overview</h1>

      <div className="flex flex-row justify-center">
        <input
          type="text"
          placeholder="Scenario ID"
          onChange={(e) => {
            setScenarioId(e.target.value);
          }}
          className="block w-30 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6"></input>
        <button
          onClick={(e) => {
            fetchData(scenarioId);
          }}
          className="rounded bg-indigo-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
          Load
        </button>
      </div>

      {loading ? <div>Loading...</div> : renderData()}
    </div>
  );
}

export default App;
