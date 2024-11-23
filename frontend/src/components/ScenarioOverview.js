import React from "react";
import { useScenario } from "../utils";
import Map from "./Map";

function ScenarioOverview({ id }) {
  const { scenario, isLoading, isError } = useScenario(id);
  if (isError) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  const renderData = () => (
    <div>
      <h2>Vehicles</h2>
      <table>
        <tr>
          <th>Position</th>
          <th>Speed</th>
          <th>CustomerId</th>
          <th>
            Remaining
            <br />
            TravelTime
          </th>
          <th>
            Distance
            <br />
            Travelled
          </th>
          <th>activeTime</th>
          <th>Trips</th>
          <th>Id</th>
        </tr>
        {scenario?.vehicles.map((item) => (
          <tr class={item.isAvailable ? "available" : "occupied"}>
            <td>
              {item.coordX}, {item.coordY}
            </td>
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
        {scenario?.customers.map((item) => (
          <tr class={item.awaitingService ? "occupied" : "available"}>
            <td>
              {item.coordX}, {item.coordY}
            </td>
            <td>
              {item.destinationX}, {item.destinationY}
            </td>
            <td>{item.customerId}</td>
            <td class="idTabledata">{item.id}</td>
          </tr>
        ))}
      </table>
    </div>
  );

  return (
    <div className="flex flex-col items-center">
      <div className="map-wrapper">
        <Map id={id} />
      </div>
      {renderData()}
    </div>
  );
}

export default ScenarioOverview;
