import { useState, useEffect } from 'react'
import GameMap from './components/GameMap';
import axios from 'axios';

// Use relative URL for production (same domain), or localhost for dev
const API_URL = import.meta.env.PROD ? '' : 'http://localhost:8000';

function App() {
    const [count, setCount] = useState(0)
    const [acreages, setAcreages] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        fetchMap();
    }, []);

    const fetchMap = async () => {
        try {
            const res = await axios.get(`${API_URL}/map`);
            setAcreages(res.data);
        } catch (error) {
            console.error("Failed to fetch map", error);
        }
    };

    const handleInitWorld = async () => {
        setLoading(true);
        try {
            await axios.post(`${API_URL}/admin/init`);
            await fetchMap();
        } catch (error) {
            console.error("Failed to init world", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-4">
            <header className="w-full max-w-6xl flex justify-between items-center mb-4">
                <h1 className="text-3xl font-bold text-yellow-500">OilQuest</h1>
                <div className="flex gap-4">
                    <button
                        className="px-4 py-2 bg-green-600 hover:bg-green-700 rounded transition-colors disabled:opacity-50"
                        onClick={handleInitWorld}
                        disabled={loading}
                    >
                        {loading ? 'Generating...' : 'Generate World'}
                    </button>
                    <div className="px-4 py-2 bg-gray-800 rounded">
                        Turn: {count}
                    </div>
                </div>
            </header>

            <main className="w-full max-w-6xl flex-grow flex flex-col gap-4">
                <div className="w-full h-[600px] bg-gray-800 rounded-lg overflow-hidden border border-gray-700 shadow-2xl relative">
                    <GameMap
                        acreages={acreages}
                        onAcreageClick={(id) => console.log("Clicked", id)}
                    />
                    {acreages.length === 0 && (
                        <div className="absolute inset-0 flex items-center justify-center bg-black/50 z-[1000] pointer-events-none">
                            <p className="text-xl font-bold">World not initialized. Click "Generate World".</p>
                        </div>
                    )}
                </div>
            </main>
        </div>
    )
}

export default App
