import { useRef, useEffect } from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
import "./Map.css";
import { useScenario } from "../utils";

function Map({ id }) {
  const { scenario, isLoading, isError } = useScenario(id);
  const mapRef = useRef(null);
  const mapContainerRef = useRef(null);
  const markersRef = useRef([]);

  useEffect(() => {
    if (!mapContainerRef.current) return;

    mapboxgl.accessToken =
      "pk.eyJ1IjoiZmx4d3UiLCJhIjoiY2pucWIxenh3MDBlYzNxa3l4NThsd3AwNiJ9.xRXLfJfu0uVxtHrj7CFyOw";

    // Only initialize map once
    if (!mapRef.current) {
      mapRef.current = new mapboxgl.Map({
        container: mapContainerRef.current,
        center: [11.576124, 48.137154],
        zoom: 11.2,
      });
      mapRef.current.on("load", () => {
        console.log("Map successfully loaded!");
      });
    }

    return () => {
      // Cleanup map instance on component unmount
      if (mapRef.current) {
        mapRef.current.remove();
        mapRef.current = null;
      }
    };
  }, []);

  useEffect(() => {
    // Wait until the map is initialized and scenario is loaded
    if (!mapRef.current || isLoading || isError || !scenario) return;

    const map = mapRef.current;

    // Remove existing markers
    markersRef.current.forEach((marker) => marker.remove());
    markersRef.current = [];

    // Add customer markers
    scenario.customers.forEach((customer) => {
      const color = customer.awaitingService ? "#404040" : "#90ee90";
      const marker = new mapboxgl.Marker({ color })
        .setLngLat([customer.coordY, customer.coordX])
        .addTo(map);

      markersRef.current.push(marker);
    });

    // Add vehicle markers
    scenario.vehicles.forEach((vehicle) => {
      const marker = new mapboxgl.Marker({ color: "#eaab54" })
        .setLngLat([vehicle.coordY, vehicle.coordX])
        .addTo(map);

      markersRef.current.push(marker);
    });
  }, [scenario, isLoading, isError]); // Update markers when scenario changes

  return (
    <div
      id="map-container"
      ref={mapContainerRef}
      style={{ width: "100%", height: "100%" }}
    />
  );
}

export default Map;
