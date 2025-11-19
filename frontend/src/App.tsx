import { useState } from 'react'

function App() {
    const [count, setCount] = useState(0)

    return (
        <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
            <h1 className="text-4xl font-bold mb-4 text-yellow-500">OilQuest</h1>
            <div className="card p-6 bg-gray-800 rounded-lg shadow-xl">
                <p className="mb-4">
                    Welcome to OilQuest. Build your empire.
                </p>
                <button
                    className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded transition-colors"
                    onClick={() => setCount((count) => count + 1)}
                >
                    Turns: {count}
                </button>
            </div>
            <div className="mt-8 w-full max-w-4xl h-96 bg-gray-700 rounded border border-gray-600 flex items-center justify-center">
                <p className="text-gray-400">Map Placeholder (Leaflet)</p>
            </div>
        </div>
    )
}

export default App
