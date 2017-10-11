const ACTION_HANDLERS = {
}

// reducer
const initialState = {
}
export default function usersReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]

  return handler
    ? handler(state, action)
    : state
}
