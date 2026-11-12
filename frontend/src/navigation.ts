export type PageKey = 'upload' | 'map' | 'analytics' | 'reports'

export interface NavItem {
  key: PageKey
  label: string
  emptyTitle: string
  emptyText: string
}

export const NAV_ITEMS: NavItem[] = [
  {
    key: 'upload',
    label: 'Upload',
    emptyTitle: 'No file uploaded yet',
    emptyText: 'Upload a hyperspectral file to see its validation and metadata here.',
  },
  {
    key: 'map',
    label: 'Map',
    emptyTitle: 'No map layers yet',
    emptyText: 'Results appear on the map after a file has been analysed.',
  },
  {
    key: 'analytics',
    label: 'Analytics',
    emptyTitle: 'No analysis results yet',
    emptyText: 'Classification results and model confidence will be shown here.',
  },
  {
    key: 'reports',
    label: 'Reports',
    emptyTitle: 'No reports yet',
    emptyText: 'Exported summaries of completed analyses will be listed here.',
  },
]
