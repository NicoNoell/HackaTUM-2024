import { useRef, useEffect } from "react";
import mapboxgl, { LngLat } from "mapbox-gl";

import "mapbox-gl/dist/mapbox-gl.css";
import "./Map.css";
import { useScenario } from "../utils";

function Map({ id }) {
  const { scenario, isLoading, isError } = useScenario(id);
  const mapRef = useRef();
  const mapContainerRef = useRef();

  useEffect(() => {
    mapboxgl.accessToken =
      "pk.eyJ1IjoiZmx4d3UiLCJhIjoiY2pucWIxenh3MDBlYzNxa3l4NThsd3AwNiJ9.xRXLfJfu0uVxtHrj7CFyOw";
    mapRef.current = new mapboxgl.Map({
      container: mapContainerRef.current,
      center: [11.576124, 48.137154],
      zoom: 10.12,
    });

    scenario["customers"].forEach(element => {
        if (element.awaitingService){
            new mapboxgl.Marker({"color":"#404040"}).setLngLat(new LngLat(element["coordY"], element["coordX"])).addTo(mapRef.current);
        } 
        else {
            new mapboxgl.Marker({"color":"#90ee90"}).setLngLat(new LngLat(element["coordY"], element["coordX"])).addTo(mapRef.current);
        }
    });

    scenario["vehicles"].forEach(element => {
        new mapboxgl.Marker({"color":"#eaab54"}).setLngLat(new LngLat(element["coordY"], element["coordX"])).addTo(mapRef.current); 
    });

    return () => {
      mapRef.current.remove();
    };
  }, []);

  return <div id="map-container" ref={mapContainerRef} />;
}

export default Map;
