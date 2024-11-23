import React from "react";
import { useState, useEffect } from "react";
import { useScenario } from "../utils";

function ScenarioOverview({ id }) {
  const { scenario, isLoading, isError } = useScenario(id);
  if (isError) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  return (
    <div>
      {scenario.vehicles.map((item) => (
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
      ))}
    </div>
  );
}

export default ScenarioOverview;
