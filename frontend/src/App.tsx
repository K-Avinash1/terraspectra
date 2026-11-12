import { useState } from 'react'
import Sidebar from './components/Sidebar'
import { NAV_ITEMS } from './navigation'
import type { PageKey } from './navigation'
import './App.css'

export default function App() {
  const [page, setPage] = useState<PageKey>('upload')
  const current = NAV_ITEMS.find((item) => item.key === page) ?? NAV_ITEMS[0]

  return (
    <div className="app-shell">
      <Sidebar active={page} onSelect={setPage} />
      <div className="content">
        <header className="topbar">
          <h1>{current.label}</h1>
        </header>
        <main className="page">
          <section className="empty-state">
            <h2>{current.emptyTitle}</h2>
            <p>{current.emptyText}</p>
          </section>
        </main>
      </div>
    </div>
  )
}