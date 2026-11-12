import { NAV_ITEMS } from '../navigation'
import type { PageKey } from '../navigation'

interface SidebarProps {
  active: PageKey
  onSelect: (key: PageKey) => void
}

export default function Sidebar({ active, onSelect }: SidebarProps) {
  return (
    <aside className="sidebar">
      <div className="brand">TerraSpectra</div>
      <nav aria-label="Main navigation">
        {NAV_ITEMS.map((item) => (
          <button
            key={item.key}
            type="button"
            className={item.key === active ? 'nav-button active' : 'nav-button'}
            aria-current={item.key === active ? 'page' : undefined}
            onClick={() => onSelect(item.key)}
          >
            {item.label}
          </button>
        ))}
      </nav>
    </aside>
  )
}
