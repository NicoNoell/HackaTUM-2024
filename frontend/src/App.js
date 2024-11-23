import logo from "./logo.svg";
import "./App.css";
import React from "react";
import { useState, useEffect } from "react";
import ScenarioOverview from "./components/ScenarioOverview";

function App() {
  const [scenarioId, setScenarioId] = useState(null);
  const [scenarioLoaded, setScenarioLoaded] = useState(false);

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

  const renderData = () => (
    <div>
    <h2>Vehicles</h2>
    <table>
        <tr>
            <th>Position</th>
            <th>Speed</th>
            <th>CustomerId</th>
            <th>Remaining<br/>TravelTime</th>
            <th>Distance<br/>Travelled</th>
            <th>activeTime</th>
            <th>Trips</th>
            <th>Id</th>
        </tr>
    {data?.vehicles.map((item) => (
    //   <div
    //     key={item.id}
    //     >
        <tr class={item.isAvailable ? "available" : "occupied"}>
            <td>{item.coordX}, {item.coordY}</td>
            <td>{item.vehicleSpeed}</td>
            <td class="idTabledata">{item.customerId}</td>
            <td>{item.remainingTravelTime}</td>
            <td>{item.distanceTravelled}</td>
            <td>{item.activeTime}</td>
            <td>{item.numberOfTrips}</td>
            <td class="idTabledata">{item.id}</td>
        </tr>
    ))}
    </table>
    
    <h2>Customers</h2>
    <table>
        <tr>
            <th>Position</th>
            <th>Destination</th>
            <th>Awaiting Service</th>
            <th>Id</th>
        </tr>
    {data?.customers.map((item) => (
        <tr class={item.awaitingService ? "occupied" : "available"}>
            <td>{item.coordX}, {item.coordY}</td>
            <td>{item.destinationX}, {item.destinationY}</td>
            <td>{item.customerId}</td>
            <td class="idTabledata">{item.id}</td>
        </tr>
    ))}
    </table>
    </div>);

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
            setScenarioLoaded(true);
          }}
          className="rounded bg-indigo-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
          Load
        </button>
      </div>

      {scenarioLoaded ? (
        <ScenarioOverview id={scenarioId} />
      ) : (
        <div>Please enter a scenario id!</div>
      )}
    </div>
  );
}

export default App;
