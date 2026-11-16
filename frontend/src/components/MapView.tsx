import { useState } from 'react'
import DeckGL from '@deck.gl/react'
import { Map as MapLibreMap } from 'react-map-gl/maplibre'
import { setWorkerUrl } from 'maplibre-gl'
import type { StyleSpecification } from 'maplibre-gl'
import workerUrl from 'maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url'
import 'maplibre-gl/dist/maplibre-gl.css'

setWorkerUrl(workerUrl)

const INITIAL_VIEW_STATE = {
  longitude: 0,
  latitude: 20,
  zoom: 1.5,
  pitch: 0,
  bearing: 0,
}

const ONLINE_STYLE = 'https://tiles.openfreemap.org/styles/positron'

const PLAIN_STYLE: StyleSpecification = {
  version: 8,
  sources: {},
  layers: [
    {
      id: 'background',
      type: 'background',
      paint: { 'background-color': '#dfe7e1' },
    },
  ],
}

export default function MapView() {
  const [basemapError, setBasemapError] = useState<string | null>(null)

  return (
    <div className="map-container">
      {basemapError && (
        <div className="map-notice" role="alert">
          Basemap could not be loaded ({basemapError}).
          Showing a plain background.
        </div>
      )}

      <DeckGL
        initialViewState={INITIAL_VIEW_STATE}
        controller={true}
        layers={[]}
      >
        <MapLibreMap
          mapStyle={basemapError ? PLAIN_STYLE : ONLINE_STYLE}
          onError={(event) =>
            setBasemapError(event.error?.message ?? 'unknown error')
          }
        />
      </DeckGL>
    </div>
  )
}