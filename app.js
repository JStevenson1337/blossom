import React from 'react-leaflet';
import SearchBox from './SearchBox';
import Maps from './Maps'

function App() {
    return (
        <div style={{ border: '2px solid red', 
        display: "flex", 
        flexDirection: "row", 
        width: '100vh', 
        height: '100vh',
    }}
    >
        <div style={{ border: '2px solid red', width: '50vw', height: '100vh' }}>
            <Maps />
        </div>
        <div style={{ border: '2px solid red', width: '50vw', height: '100vh' }}>
            <SearchBox />
        </div>
        </div>
        );
}

export default App;
