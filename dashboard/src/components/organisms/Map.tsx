import React from 'react';
import { MBox } from '../boxes';
import { Title } from '../text';
import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';

const containerStyle = {
    width: '600px',
    height: '400px',
    margin: 'auto',
    borderRadius: '10px',
  };
  
const center = {
  lat: 20.9863018,
  lng: -89.733405
};

const position = {
  lat: 20.9878394,
  lng: -89.7368373
}

const Mapper: React.FC = () => {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyCQI16Yuf-JyXwumvuFEUr9kGOZedQwoy0"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map:any) {
    const bounds = new window.google.maps.LatLngBounds(center);
    map.fitBounds(bounds);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map:any) {
    setMap(null)
  }, [])

  return isLoaded ? (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={center}
      zoom={0}
      onLoad={onLoad}
      onUnmount={onUnmount}
    >
      { /* Child components, such as markers, info windows, etc. */ }
      
        <Marker
          position={position}
        />
    </GoogleMap>
) : <></>
}

const Map: React.FC = () => {
    return (
        <MBox>
            <Title title='Map'/>
            <Mapper/>
        </MBox>
    );
};

export default Map;