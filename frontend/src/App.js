import React, { useState } from "react";
import "./App.css";
import ScenarioOverview from "./components/ScenarioOverview";

function App() {
  const [scenarioId, setScenarioId] = useState(null);
  const [scenarioLoaded, setScenarioLoaded] = useState(false);

  const startScenario = async (sc) => {
    const res = await fetch(
      `http://127.0.0.1:5000/api/startScenario?scenarioId=${sc}`
    );
    if (!res.ok) throw new Error("Error when starting scenario.");
    setTimeout(() => {
      setScenarioId(sc);
    }, 2000);
  };

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
            startScenario(scenarioId);
            setScenarioLoaded(true);
          }}
          className={`rounded bg-indigo-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600}`}>
          Start
        </button>
      </div>
      <div className="mt-15">
        {scenarioLoaded ? (
          <ScenarioOverview id={scenarioId} />
        ) : (
          <div>Please enter a scenario id!</div>
        )}
      </div>
    </div>
  );
}

export default App;
