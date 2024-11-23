import React from "react";
import { useScenario } from "../utils";
import Map from "./Map";

function ScenarioOverview({ id }) {
  const { scenario, isLoading, isError } = useScenario(id);
  if (isError) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  const renderData = () => (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>Scenario Dashboard</h1>
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          gap: '20px',
          alignItems: 'stretch',
          height: 'calc(100vh - 200px)', // Adjust to fit viewport height
        }}
      >
        {/* Vehicles Table */}
        <div
          style={{
            flex: 1,
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
            borderRadius: '8px',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <h2
            style={{
              textAlign: 'center',
              padding: '10px 0',
              fontSize: '18px',
              color: '#333',
              backgroundColor: '#cce7ff',
              borderBottom: '1px solid #eee',
            }}
          >
            Vehicles
          </h2>
          <div style={{ flex: 1, overflowY: 'auto' }}>
            <table
              style={{
                width: '100%',
                borderCollapse: 'collapse',
                textAlign: 'center',
                height: '100%',
              }}
            >
              <thead>
                <tr
                  style={{
                    fontWeight: 'bold',
                    padding: '10px',
                    textAlign: 'center',
                  }}
                >
                  <th>Position</th>
                  <th>Speed</th>
                  <th>Client</th>
                  <th>
                    Remaining
                    <br />
                    Time
                  </th>
                  <th>
                    Distance
                    <br />
                    Travelled
                  </th>
                  <th>Active Time</th>
                  <th>Trips</th>
                  <th>Id</th>
                </tr>
              </thead>
              <tbody>
                {scenario?.vehicles.map((item) => (
                  <tr
                    className={item.isAvailable ? 'available' : 'occupied'}
                    style={{
                      background: item.isAvailable ? '#d4edda' : '#f8d7da',
                      borderBottom: '1px solid #ddd',
                    }}
                  >
                    <td>{`${(item.coordX ?? 0).toFixed(2)}, ${(item.coordY ?? 0).toFixed(2)}`}</td>
                    <td>{(item.vehicleSpeed ?? 0).toFixed(2)}</td>
                    <td className="idTabledata">{item.customerId ?? 'N/A'}</td>
                    <td>{(item.remainingTravelTime ?? 0).toFixed(2)}</td>
                    <td>{(item.distanceTravelled ?? 0).toFixed(2)}</td>
                    <td>{(item.activeTime ?? 0).toFixed(2)}</td>
                    <td>{item.numberOfTrips ?? 0}</td>
                    <td className="idTabledata">{item.id ?? 'N/A'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
  
        {/* Customers Table */}
        <div
          style={{
            flex: 1,
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
            borderRadius: '8px',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <h2
            style={{
              textAlign: 'center',
              padding: '10px 0',
              fontSize: '18px',
              color: '#333',
              backgroundColor: '#cce7ff',
              borderBottom: '1px solid #eee',
            }}
          >
            Customers
          </h2>
          <div style={{ flex: 1, overflowY: 'auto' }}>
            <table
              style={{
                width: '100%',
                borderCollapse: 'collapse',
                textAlign: 'center',
                height: '100%',
              }}
            >
              <thead>
                <tr
                  style={{
                    fontWeight: 'bold',
                    padding: '10px',
                    textAlign: 'center',
                  }}
                >
                  <th>Position</th>
                  <th>Destination</th>
                  <th>Id</th>
                </tr>
              </thead>
              <tbody>
                {scenario?.customers.map((item) => (
                  <tr
                    className={item.awaitingService ? 'occupied' : 'available'}
                    style={{
                      background: item.awaitingService ? '#f8d7da' : '#d4edda',
                      borderBottom: '1px solid #ddd',
                    }}
                  >
                    <td>{`${(item.coordX ?? 0).toFixed(2)}, ${(item.coordY ?? 0).toFixed(2)}`}</td>
                    <td>{`${(item.destinationX ?? 0).toFixed(2)}, ${(item.destinationY ?? 0).toFixed(2)}`}</td>
                    <td className="idTabledata">{item.id ?? 'N/A'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
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
