import React from 'react-leaflet'
import {
    MapContainer,
    TileLayer,
    useMap,
    } from 'https://cdn.esm.sh/react-leaflet'
import "leaflet/dist/leaflet.css";
import L from 'react-leaflet'

const position = [51.505, -0.09]
const icon = L.icon({
    iconURL: "../blossom/icons/location.png"
})

export default function Maps () {
return (
    <MapContainer center={position} zoom={13} style={{ width: '100%', height: '100%'}} scrollWheelZoom={false}>
    <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />
    <Marker position={position}>
        <Popup>
        A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
    </Marker>
    </MapContainer>
    )
}