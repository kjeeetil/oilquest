import { MapContainer, TileLayer, Rectangle, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useEffect, useState } from 'react';

// Fix for Leaflet default icon issue
import L from 'leaflet';
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';

let DefaultIcon = L.icon({
    iconUrl: icon,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

L.Marker.prototype.options.icon = DefaultIcon;

interface Acreage {
    id: number;
    lat: number;
    lon: number;
    status: string;
    owner_id: number | null;
}

interface GameMapProps {
    acreages: Acreage[];
    onAcreageClick: (id: number) => void;
}

// Component to fit bounds
function MapBounds({ acreages }: { acreages: Acreage[] }) {
    const map = useMap();

    useEffect(() => {
        if (acreages.length > 0) {
            const bounds = L.latLngBounds(acreages.map(a => [a.lat, a.lon]));
            map.fitBounds(bounds, { padding: [50, 50] });
        }
    }, [acreages, map]);

    return null;
}

export default function GameMap({ acreages, onAcreageClick }: GameMapProps) {
    const STEP = 0.5; // Must match backend

    const getColor = (status: string) => {
        switch (status) {
            case 'OWNED': return 'blue';
            case 'EXPLORED': return 'green';
            case 'PRODUCING': return 'black';
            default: return 'transparent';
        }
    };

    return (
        <MapContainer center={[55, 5]} zoom={5} style={{ height: '100%', width: '100%' }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <MapBounds acreages={acreages} />
            {acreages.map((acreage) => (
                <Rectangle
                    key={acreage.id}
                    bounds={[
                        [acreage.lat, acreage.lon],
                        [acreage.lat + STEP, acreage.lon + STEP]
                    ]}
                    pathOptions={{
                        color: 'gray',
                        weight: 1,
                        fillColor: getColor(acreage.status),
                        fillOpacity: acreage.status === 'AVAILABLE' ? 0.1 : 0.5
                    }}
                    eventHandlers={{
                        click: () => onAcreageClick(acreage.id)
                    }}
                >
                    <Popup>
                        <div>
                            <p>ID: {acreage.id}</p>
                            <p>Status: {acreage.status}</p>
                            <p>Owner: {acreage.owner_id || 'None'}</p>
                        </div>
                    </Popup>
                </Rectangle>
            ))}
        </MapContainer>
    );
}
