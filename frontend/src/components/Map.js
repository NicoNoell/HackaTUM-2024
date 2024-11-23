import { useRef, useEffect } from "react";
import mapboxgl from "mapbox-gl";

import "mapbox-gl/dist/mapbox-gl.css";
import "./Map.css";

function Map() {
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

    return () => {
      mapRef.current.remove();
    };
  }, []);

  return <div id="map-container" ref={mapContainerRef} />;
}

export default Map;
