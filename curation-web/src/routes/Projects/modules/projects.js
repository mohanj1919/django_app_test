const ACTION_HANDLERS = {
}

//reducer
const initialState = {
}
export default function projectsReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]

  return handler
    ? handler(state, action)
    : state
}
