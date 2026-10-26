export const getCustomer = (id: string): Promise<{ id: string; name: string }> =>
  fetch(`/api/customers/${id}`).then((r) => r.json())
