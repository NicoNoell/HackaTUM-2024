import React from "react";
import { useScenario } from "../utils";

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
          //   <div
          //     key={item.id}
          //     >
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
