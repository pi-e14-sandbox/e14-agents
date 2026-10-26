export interface Order { id: string; customerId: string; totalCents: number }

export const listOrders = (): Promise<Order[]> => fetch('/api/orders').then((r) => r.json())

export const createOrder = (customerId: string, totalCents: number): Promise<Order> =>
  fetch('/api/orders', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ customerId, totalCents }) }).then((r) => r.json())

export const getOrder = (id: string): Promise<Order> => fetch(`/api/orders/${id}`).then((r) => r.json())
